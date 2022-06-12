#/bin/bash

echo "Bringing down ip feedback service and script"
wget https://raw.githubusercontent.com/slowrunner/GoPiGo3-Bullseye_32-bit/main/etc_systemd_system.ip_feedback.service
wget https://raw.githubusercontent.com/slowrunner/GoPiGo3-Bullseye_32-bit/main/ip_feedback.sh
chmod 777 ip_feedback.sh
chmod 777 setup_ip_feedback.sh

echo "copying ip_feedback.sh to /home/pi"
cp ip_feedback.sh /home/pi

echo "copying ip_feedback.service to /etc/systemd/system"
sudo cp ./etc_systemd_system.ip_feedback.service /etc/systemd/system/ip_feedback.service
sudo systemctl daemon-reload
sudo systemctl enable ip_feedback
sudo service ip_feedback start
