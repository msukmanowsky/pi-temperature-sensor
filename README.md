# Raspberry Pi Temperature Sensor

Very tiny repo with code to support temperature detection with a
[Raspberry Pi](https://www.raspberrypi.org/) and the 
[DS18B20](https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf) temperature
sensor.

Big thank you to the folks at [Joy-IT](https://sensorkit.joy-it.net/) for their
excellent guides (including one for the 
[DS18B20](https://sensorkit.joy-it.net/en/sensors/ky-001)) that provide both
wiring instructions and sample code whichI adapted for my script.

# What this code does

Pretty simple, `sense.py` reads the current temperature, in Celsius and sends
it to ThingSpeak, an IoT measurement platform.

# Running the code

Requires Python 3.6 or higher.

1. Within a new virtual env, install requirements `pip install -r requirements.txt`
2. Create a `.env` file with a single entry `THING_SPEAK_API_KEY` which maps
   to the write API key for [ThingSpeak](https://thingspeak.com/channels/1867586/private_show)
3. Run `python sense.py` (or set it up to run via CRON), to measure and send 
   sensor readings to ThingSpeak
