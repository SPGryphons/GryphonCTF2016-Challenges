#!/bin/sh

cd /opt
git clone https://github.com/keystone-engine/keystone.git
cd keystone
mkdir build
cd build
../make-share.sh
sudo make install
sudo ldconfig
cd ../bindings/python
sudo python setup.py install
