## Temperature sensure for Raspberry Pi Zero W

### Prerequisites:

```sh
sudo apt install python3-systemd libgpiod2 python3-pip
sudo pip3 install Adafruit_DHT
```

### Installation

```sh
sudo mkdir /usr/local/lib/temperature
sudo cp read_temp.py /usr/local/lib/temperature/
sudo chown root:root /usr/local/lib/temperature/read_temp.py
sudo chmod 644 /usr/local/lib/temperature/read_temp.py

sudo cp temperature/service /etc/systemd/system
sudo chown root:root /etc/systemd/system/temperature.service
sudo chmod 644 /etc/systemd/system/temperature.service

sudo systemctl daemon-reload
sudo systemctl edit temperature
```

In the editor:

```
[Service]
Environment="ROOM=<room name>"
Environment="GPIO=<gpio port number>"
Environment="HOST=<graphite host name>"
Environment="PORT=<graphite port number if not default>"
```

Then:

```sh
sudo systemctl enable temperature
sudo systemctl start temperature
sudo systemctl status temperature
```


```
