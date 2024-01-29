import Adafruit_DHT
import paho.mqtt.client as mqtt
import time

# Sensor type and GPIO pin
sensor = Adafruit_DHT.AM2302
pin = 14

# MQTT settings
mqtt_broker = "homeassistant"
mqtt_port = 1883
mqtt_topic_temperature = "home/gpio/sensor/temperature"
mqtt_topic_humidity = "home/gpio/sensor/humidity"

# Connect to MQTT Broker
client = mqtt.Client()
client.username_pw_set("username", "password")  # Replace with your MQTT credentials

while True:
    try:
        client.connect(mqtt_broker, mqtt_port, 60)
        client.loop_start()  # Start the network loop
        time.sleep(1)  # Wait a bit for the client to establish connection
        break  # Successful connection, exit the loop
    except:
        print("Connection to MQTT broker failed, retrying...")
        time.sleep(5)  # Wait for 5 seconds before retrying

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        if humidity is not None and temperature is not None:
            # Publishing the temperature and humidity data to MQTT topics
            client.publish(mqtt_topic_temperature, f"{temperature:.1f}")
            client.publish(mqtt_topic_humidity, f"{humidity:.1f}")
            print("Data published to MQTT broker.")
        else:
            print("Failed to retrieve data from the sensor")

        # Wait for 60 seconds before next reading
        time.sleep(60)
except KeyboardInterrupt:
    print("Stopping the script")

client.loop_stop()  # Stop the network loop
client.disconnect()
