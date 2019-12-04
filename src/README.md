# Setup instructions
All these instructions assume that you start from the same path, the path which
this README.md is in.

## Download all submodules
$ git submodule update --init

## Create a virtualenv
$ apt-get install python3 python3-virtualenv python3-pip virtualenv
$ virtualenv -p python3 labgrid-venv

## To install labgrid
$ source labgrid-venv/bin/activate
$ cd labgrid && pip install -r requirements.txt
$ python3 setup.py install

## To install uhubctl (for USB power control)
Note: skip this step if you have a different power control system. Or if you
prefer to use manual power control.

$ source labgrid-venv/bin/activate
$ apt install libusb-1.0-0-dev
$ cd uhubctl
$ make
$ cp uhubctl ../labgrid-venv/bin/
$ sed -e 's/XXXX/05e3/' 40-custom-hub.rules | sudo tee /etc/udev/rules.d/40-custom-hub.rules
$ sudo udevadm trigger --attr-match=subsystem=usb
