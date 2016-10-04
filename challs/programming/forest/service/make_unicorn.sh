#!/bin/sh

cd /opt
git clone https://github.com/unicorn-engine/unicorn.git
cd unicorn
UNICORN_ARCHS="x86" ./make.sh
./make.sh install
cd bindings/python
sudo python setup.py install
