```sudo docker build -t custom-mqtt .```

```sudo docker run --name custom-mqtt-container -d --privileged --device /dev/mem:/dev/mem --device /dev/gpiomem:/dev/gpiomem --network host custom-mqtt```
