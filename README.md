# iec61850_open_client

This is an open implementation of an IEC 61850 web based client. It uses flask with websockets for the webserver.
The backend is a python3 based iec61850 client implementation that uses ctypes for the wrapper.

The client is configured by using an svg-file
that describes the interface elements graphically, and connects to the datapoints using the id-element.
The format for referencing a datapoint is: iec61850://[IED-IP]:[port]/[LD]/[LN]/[Do]/[Da]

elements can be animated using the animate tag.


# getting started:

this client needs libiec61850.so installed in /usr/local/lib/libiec61850.so This can be done by doing:

get  the library
`$ git clone https://github.com/mz-automation/libiec61850.git`

cd into the directory
`$ cd libiec61850`

compile the library
`$ make`

install the library
`$ sudo make install`

cd to the client project dir.
`$ ../iec61850_open_client`

also the prerequesites for flask are needed;

`$ pip3 install -r requirements.txt`

then start the app;
`python3 app`

and browse to http://127.0.0.1:5000
