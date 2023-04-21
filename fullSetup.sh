#!/bin/bash

# Update package list
apt update && upgrade -y

pkg install tur-repo
pkg install x11-repo
pkg install root-repo
pkg install science-repo
pkg install game-repo
apt update && upgrade -y
# Install packages using apt
apt install -y openssh nano dlib python nodejs git curl wget python-pip python-numpy yarn python-pillow

# Install http-server using npm
npm install -g http-server

# Install wheel and setuptools using pip
pip install wheel setuptools

# Install Python packages using pip
pip install beautifulsoup4==4.12.0 bs4==0.0.1 face-recognition==1.3.0 Flask==2.2.2 pymongo==4.3.3 pypng==0.20220715.0 PyQRCode==1.2.1 requests==2.28.1 selenium==4.8.3 urllib3==1.26.15 webdriver-manager==3.8.5

# Output: Display completion message
echo "All packages have been installed successfully!"
