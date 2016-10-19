#!/bin/python
'''
Python wrapper for
4DSystems' Diablo16 & Picaso Displays

Copyright (C) 2016 by Xose Perez <xose dot perez at gmail dot com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import paho.mqtt.client as mqtt
from DiabloSerial import DiabloSerial
from DiabloConstants import *

# ------------------------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------------------------

MQTT_BROKER = '192.168.1.10'
MQTT_PORT = 1883
MQTT_TOPIC = '/home/studio/lamp'

# ------------------------------------------------------------------------------

buttonState = BUTTON_UP

def on_connect(client, userdata, flags, rc):
    print("Connected to broker at %s" % MQTT_BROKER)
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    global buttonState
    if msg.topic == MQTT_TOPIC:
        '''
        I'm checking both conditions since I have a third option at home
        If payload[0] == '2' it means toggle
        '''
        if msg.payload[0] == '1':
            buttonState = BUTTON_DOWN
        if msg.payload[0] == '0':
            buttonState = BUTTON_UP
        show_button_state()

def callback(errcode, errbyte):
    print "ERROR: ", errcode, errbyte
    sys.exit(1)

def show_button_state():
    global buttonState
    diablo.gfx_Button(buttonState, 20, 40, GRAY if buttonState == BUTTON_UP else RED, WHITE, FONT3, 3, 3, "Press Me")
    diablo.txt_Width(2);
    diablo.txt_Height(2);
    diablo.gfx_MoveTo(50,120);
    diablo.putstr("Light %s" % ("OFF" if buttonState == BUTTON_UP else "ON "));

def send_state():
    global buttonState
    client.publish(MQTT_TOPIC, "1" if buttonState == BUTTON_DOWN else "0")

if __name__ == "__main__":

    # Initialize display
    diablo = DiabloSerial(500, True, callback)
    diablo.OpenComm('/dev/ttyUSB0', 9600)
    diablo.touch_Set(TOUCH_ENABLE)
    diablo.gfx_Cls()
    print "Model:", diablo.sys_GetModel()
    print "Version:", diablo.sys_GetVersion()
    show_button_state()

    # Initialize MQTT connection
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    x = y = 0

    while True:

        client.loop(timeout=0.1)
        state = diablo.touch_Get(TOUCH_STATUS)

        if ((state == TOUCH_PRESSED) or (state == TOUCH_MOVING)):
            x = diablo.touch_Get(TOUCH_GETX)
            y = diablo.touch_Get(TOUCH_GETY)

        if (state == TOUCH_RELEASED):
            if ((x>=20) and (x<=220) and (y>=40) and (y<=100)):
                buttonState = not buttonState
                show_button_state()
                send_state()
