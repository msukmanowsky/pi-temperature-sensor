import contextlib
import datetime as dt
import glob
import os
import time
import functools

import RPi.GPIO as GPIO
import requests
from dotenv import load_dotenv


load_dotenv()

@contextlib.contextmanager
def one_wire_pin(bcm_pin_number=4, activate_pullup_resistor=True):
    # The One-Wire input pin is declared and the integrated PullUp resistor is activated
    GPIO.setmode(GPIO.BCM)
    if activate_pullup_resistor:
        GPIO.setup(bcm_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    try:
        yield
    finally:
        GPIO.cleanup()


@functools.cache
def get_wire1_device_filename() -> str:
    base_dir = "/sys/bus/w1/devices/"
    while True:
        try:
            device_folder = glob.glob(base_dir + '28*')[0]
            break
        except IndexError:
            time.sleep(0.5)
            continue
    return f"{device_folder}/temperature"


def read_temperature_celsius():
    device_filename = get_wire1_device_filename()
    with open(device_filename, "r") as fp:
        temperature = int(fp.read().strip())
    
    return temperature / 1000.0


def main():
    with one_wire_pin():
        timestamp = dt.datetime.utcnow()
        temperature = read_temperature_celsius()
        print(f"{timestamp.isoformat()} {temperature}")
        requests.post("https://api.thingspeak.com/update.json", data={
            "api_key": os.environ.get("THING_SPEAK_API_KEY"),
            "created_at": timestamp.isoformat(),
            "field1": temperature,
            "status": "OK",
        })


if __name__ == "__main__":
    main()