#!/bin/sh

BRANCH_NAME="main"

rm -f /usr/local/cyberpanel_upgrade.sh
wget -O /usr/local/cyberpanel_upgrade.sh https://raw.githubusercontent.com/angvil911/justtesting/$BRANCH_NAME/cyberpanel_upgrade.sh 2>/dev/null
chmod 700 /usr/local/cyberpanel_upgrade.sh
/usr/local/cyberpanel_upgrade.sh
