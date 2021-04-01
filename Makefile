
install:
	sudo install -v -C -D -g root -o root -m 644 read_temp.py /usr/local/lib/temperature/
	sudo install -v -C -D -g root -o root -m 644 temperature.service /etc/systemd/system/
