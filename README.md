## Temperature sensure for Raspberry Pi Zero W

This is developed and tested on a Raspberry Pi Zero W, with a DHT22 temperature and humidity sensor.

### Prerequisites:

```sh
sudo apt install python3-systemd libgpiod2 python3-pip
sudo pip3 install Adafruit_DHT influxdb-client
```

### Installation

```sh
sudo make install

sudo systemctl daemon-reload
sudo systemctl edit temperature
```

In the editor:

```
[Service]
Environment="ROOM=<room name>"
Environment="GPIO=<gpio port number>"
Environment="INFLUXDB_V2_URL=https://url.to.influxdb.com"
Environment="INFLUXDB_V2_ORG=<influxdb organization>"
Environment="INFLUXDB_V2_BUCKET=<influxdb bucket>"
Environment="INFLUXDB_V2_TOKEN=<infludb token>"

```

Then:

```sh
sudo systemctl enable temperature
sudo systemctl start temperature
sudo systemctl status temperature
```

