import argparse
import logging
import socket
import time

import Adafruit_DHT

INTERVAL = 60
KEY = 'home.%(room)s.%(metric)s'
SENSOR = Adafruit_DHT.DHT22


def write_graphite(host, port, key, value):
    logging.info("Sending %s => %s", key, value)
    message = '%s %.3f %d\n' % (key, value, int(time.time()))
    sock = socket.socket()
    sock.connect((host, port))
    sock.sendall(message.encode('ascii'))
    sock.close()


def main(gpio, room, graphite_host, graphite_port):
    while True:
        hum, temp = Adafruit_DHT.read_retry(SENSOR, gpio)
        if temp is not None:
            write_graphite(graphite_host, graphite_port, KEY % {'room': room, 'metric': 'temperature'}, temp)
        if hum is not None:
            write_graphite(graphite_host, graphite_port, KEY % {'room': room, 'metric': 'humidity'}, hum)
          
        time.sleep(INTERVAL)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Measure temperatures and send them to graphite')
    parser.add_argument('--gpio', type=int, help='GPIO port of temperature sensor', required=True)
    parser.add_argument('--room', type=str, help='Room name to use in graphite', required=True)
    parser.add_argument('--host', type=str, help='Graphite host to send metrics to', required=True)
    parser.add_argument('--port', type=int, help='Graphite port number', default=2003)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    
    main(args.gpio, args.room, args.host, args.port)
