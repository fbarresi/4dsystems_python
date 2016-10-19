# Python Wrapper for 4DSystems Diablo16 and Picaso Displays C Serial Libraries

This repository contains python wrapper classes for C Serial Library by [4DSystems][1] meant for their Picaso and Disablo16 displays.

This is still a work in progress and as such is delivered "**AS IS**". I'm testing some of the functions myself for my own projects. If you happen to find a bug or have any suggestion please contact me or file a bug report.

Thank you.

## Building the libraries

This python modules are wrapper classes around 4DSystem's C libraries. So you will first need these ones. I have included both libraries in the libs folder but they have been compiled on a Linux x86_64 machine so they might not suit your machine architecture.

Therefore, you should checkout the Picaso or Diablo16 serial libraries and compile them on your machine. Then edit the DiabloSerial.py or PicasoSerial.py modules to check if they are properly referenced. I might provide a more elegant solution in the future.

**NOTE**: to compile the libraries on my machine I had to add the -fPIC flag to my compiler options to generate a dynamic library (a \*.so). So I edited the Makefile to change the CCFLAGS line like this:

```
CFLAGS  = $(DEBUG) -Wall $(INCLUDE) -Winline -pipe -fPIC
```


## Example

The provided example displays a simple push button that sends an MQTT message to a local broker.

First you will need to wire the Interface Board (gen4-IB) to your favourite USB to UART adapter (and FTDI-like will do). Be sure to use 5V logic and cross RX and TX cables. You don't need to connect the RST pin.

![Connecting the gen4-IB to and FTDI adapter](/images/20161019_095810s.jpg)


To run the DiabloTest example you will need paho-mqtt module for python.
The recommended way is to use [virtualenv][5] to setup a python virtual environment.
You can easily install it with:

```
pip install virtualenv
```

Once installed create a virtual environment folder and activate it:

```
virtualenv .venv
source .venv/bin/activate
```

Now you can install the dependencies in this isolated environment:

```
pip install -r requirements.txt
```

Edit the DiabloTest.py file to match your requirements in the CONFIGURATION section.
And finally:

```
python DiabloTest.py
```

## Links

* [4DSystems website][1]
* [4DSystems gen4 HMI Display Modules][2]
* [Diablo16 Serial Linux Library repository][3]
* [Picaso Serial Linux  Library repository][4]


[1]: http://www.4dsystems.com.au/
[2]: http://www.4dsystems.com.au/products
[3]: https://github.com/4dsystems/Diablo16-Serial-Linux-Library
[4]: https://github.com/4dsystems/Picaso-Serial-Linux-Library
[5]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
