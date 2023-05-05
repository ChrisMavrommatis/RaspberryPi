# Temperature Controlled Fan With Poweroff Button

Place Main.py in /home/pi/services/tcfp/ or any other directory. 
Final path should be /home/pi/services/tcfp/main.py

Place tcfp.service in  /lib/systemd/system/
Final Path should be /lib/systemd/system/tcfp.service


sudo chmod 644 /lib/systemd/system/tcfp.service
chmod +x /home/pi/services/tcfp/main.py
sudo systemctl daemon-reload
sudo systemctl enable tcfp.service
sudo systemctl start tcfp.service