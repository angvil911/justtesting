#!/bin/sh

# DevaSystem Installer Bootstrap
# This script detects the OS and launches the main installer

REPO_USER="angvil911"
REPO_NAME="justtesting"
BRANCH="main"
RAW_BASE="https://raw.githubusercontent.com/${REPO_USER}/${REPO_NAME}/${BRANCH}"
INSTALL_DIR="/tmp/cyberpanel"

OUTPUT=$(cat /etc/*release)
if  echo $OUTPUT | grep -q "CentOS Linux 7" ; then
        echo "Checking and installing curl and wget"
yum install curl wget git -y 1> /dev/null
yum update curl wget git ca-certificates -y 1> /dev/null
                SERVER_OS="CentOS"
elif echo $OUTPUT | grep -q "CentOS Linux 8" ; then
        echo -e "\nDetecting Centos 8...\n"
        SERVER_OS="CentOS8"
yum install curl wget git -y 1> /dev/null
yum update curl wget git ca-certificates -y 1> /dev/null
elif echo $OUTPUT | grep -q "AlmaLinux 8" ; then
        echo -e "\nDetecting AlmaLinux 8...\n"
        SERVER_OS="CentOS8"
yum install curl wget git -y 1> /dev/null
yum update curl wget git ca-certificates -y 1> /dev/null
elif echo $OUTPUT | grep -q "AlmaLinux 9" ; then
        echo -e "\nDetecting AlmaLinux 9...\n"
        SERVER_OS="CentOS8"
yum install curl wget git -y 1> /dev/null
yum update curl wget git ca-certificates -y 1> /dev/null
elif echo $OUTPUT | grep -q "AlmaLinux 10" ; then
        echo -e "\nDetecting AlmaLinux 10...\n"
        SERVER_OS="CentOS8"
yum install curl wget git -y 1> /dev/null
yum update curl wget git ca-certificates -y 1> /dev/null
elif echo $OUTPUT | grep -q "CloudLinux 7" ; then
        echo "Checking and installing curl and wget"
yum install curl wget git -y 1> /dev/null
yum update curl wget git ca-certificates -y 1> /dev/null
                SERVER_OS="CloudLinux"
elif echo $OUTPUT | grep -q "CloudLinux 8" ; then
        echo "Checking and installing curl and wget"
yum install curl wget git -y 1> /dev/null
yum update curl wget git ca-certificates -y 1> /dev/null
                SERVER_OS="CloudLinux"
elif echo $OUTPUT | grep -q "Ubuntu 18.04" ; then
apt install -y -qq wget curl git
                SERVER_OS="Ubuntu"
elif echo $OUTPUT | grep -q "Ubuntu 20.04" ; then
apt install -y -qq wget curl git
                SERVER_OS="Ubuntu"
elif echo $OUTPUT | grep -q "Ubuntu 22.04" ; then
apt install -y -qq wget curl git
                SERVER_OS="Ubuntu"
elif echo $OUTPUT | grep -q "openEuler 20.03" ; then
        echo -e "\nDetecting openEuler 20.03...\n"
        SERVER_OS="openEuler"
yum install curl wget git -y 1> /dev/null
yum update curl wget git ca-certificates -y 1> /dev/null
elif echo $OUTPUT | grep -q "openEuler 22.03" ; then
        echo -e "\nDetecting openEuler 22.03...\n"
        SERVER_OS="openEuler"
yum install curl wget git -y 1> /dev/null
yum update curl wget git ca-certificates -y 1> /dev/null
else

                echo -e "\nUnable to detect your OS...\n"
                echo -e "\nDevaSystem is supported on Ubuntu 18.04, Ubuntu 20.04 Ubuntu 22.04, AlmaLinux 8, AlmaLinux 9, AlmaLinux 10 and CloudLinux 7.x...\n"
                exit 1
fi

# Clone the repo directly instead of downloading from CDN
echo -e "\nDownloading DevaSystem installer...\n"
rm -rf "$INSTALL_DIR"
git clone https://github.com/${REPO_USER}/${REPO_NAME}.git "$INSTALL_DIR"
cd "$INSTALL_DIR" || exit

# Run the main installer script
chmod +x cyberpanel.sh
./cyberpanel.sh $@