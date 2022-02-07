#!/bin/bash

echo "********Install Python********"
sudo apt-get update
sudo apt -y install libqtgui4
sudo apt -y install libqt4-test
sudo pip3 install --upgrade pip
sudo pip3 install wheel setuptools pySerial requests
sudo pip3 install numpy-1.18.5-cp35-cp35m-linux_aarch64.whl
sudo pip3 install opencv_python-4.1.1.26-cp35-cp35m-linux_aarch64.whl
echo "********Install Docker********"
sudo apt-get -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo add-apt-repository \
"deb [arch=arm64] https://download.docker.com/linux/debian \
$(lsb_release -cs) \
stable"

sudo apt-get update
sudo apt-get -y install docker-ce docker-ce-cli containerd.io
sudo usermod -aG docker $USER
sudo newgrp docker
