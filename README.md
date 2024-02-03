```sudo docker build -t custom-mqtt .```

```
sudo docker run --name custom-mqtt-container -d --restart always --privileged --device /dev/mem:/dev/mem --device /dev/gpiomem:/dev/gpiomem --network host -e TZ=Europe/Vilnius custom-mqtt
```
