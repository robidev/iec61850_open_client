# iec61850_open_client

This is an open implementation of an IEC 61850 web based client. It uses flask with websockets for the webserver.
The backend is a python3 based iec61850 client implementation that uses ctypes for the wrapper.

![Alt text](screenshot.png?raw=true "Screenshot of client interface")

The client is configured by using an svg-file; static/mmi.svg
This file describes the interface elements graphically, and connects to the datapoints using the id-element.
The format for referencing a datapoint is: iec61850://[IED-IP]:[port]/[LD]/[LN]/[Do]/[Da]. 
class defines are used to indicate how the tag should be interacted with. MEAS is read, XCBR is animated and CSWI can be operated on

elements can be animated using the animate tag.

# getting started(docker):

build the container

`$ sudo docker build -f Dockerfile.libiec61850_client --tag client .`

run the container

`$ sudo docker run --rm -p 5000:5000 client`

and browse to 

http://127.0.0.1:5000

# getting started(localhost):

this client needs libiec61850.so installed in /usr/local/lib/libiec61850.so This can be done by doing:

get  the library

`$ git clone https://github.com/mz-automation/libiec61850.git`

cd into the directory

`$ cd libiec61850`

compile the library

`$ make dynlib`

install the library in the right place for the ctypes wrapper 
(you can modify this in lib61850.py if you prefer a different location)

`$ sudo cp build/libiec61850.so /usr/local/lib/`

cd to the client project dir.

`$ cd ../iec61850_open_client`

also the prerequesites for flask are needed;

`$ pip3 install -r requirements.txt`

then start the app;

`$ python3 app.py`

and browse to 

http://127.0.0.1:5000
