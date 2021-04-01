import argparse
import logging
import socket
from datetime import datetime
import time

import Adafruit_DHT
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


INTERVAL = 60
SENSOR = Adafruit_DHT.DHT22


def main(gpio, room, org, bucket):
    while True:
        client = InfluxDBClient.from_env_properties()
        write_api = client.write_api(write_options=SYNCHRONOUS)
        hum, temp = Adafruit_DHT.read_retry(SENSOR, gpio)
        if temp is not None:
            p = Point("temp").tag("room", room).field("degrees_c", temp).time(datetime.utcnow())
            logging.info("Writing %s", p.to_line_protocol())
            write_api.write(bucket, org, p)
        if hum is not None:
            p = Point("humid").tag("room", room).field("perc_rh", hum).time(datetime.utcnow())
            logging.info("Writing %s", p.to_line_protocol())
            write_api.write(bucket, org, p)
        write_api.close()

        time.sleep(INTERVAL)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Measure temperatures and send them to graphite')
    parser.add_argument('--gpio', type=int, help='GPIO port of temperature sensor', required=True)
    parser.add_argument('--room', type=str, help='Room name to use in metric names', required=True)
    parser.add_argument('--org', type=str, help='InfluxDB org to use')
    parser.add_argument('--bucket', type=str, help='InfluxDB bucket to use')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    
    main(args.gpio, args.room, args.org, args.bucket)
