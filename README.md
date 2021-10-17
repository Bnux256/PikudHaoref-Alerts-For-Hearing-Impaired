# RedAlerts-For-Hearing-Impaired
Using a Raspberry Pi connected to the unoffical Pikud Haoref API to alert hearing imparied people of rocket alerts.
Made after Operation Guardian of the Walls.
## Download and Run: 

```  
git clone https://github.com/Bnux256/RedAlerts-For-Hearing-Impaired.git
cd RedAlerts-For-Hearing-Impaired
python3 main.py
```
Can also run from included Debian Dockerfile.

## Alerting using:
* a loud speaker - connected to headphone jack
* a 3.3V buzzer - connected to GPIO pin no. 17
* a 3V eccentric vibrating motor - 45mA current - (bigger motors won't work) - connected to GPIO pin no. 27.
* a powerful blinking LED - unsoldering usb desk light and connecting the 3V led to raspberry pi - connected to GPIO pin no. 4. 

Connecting to Pikud Haoref using the unoffical site API which uses a JSON files that shows the current alerts. For testing purpose the program checks for alerts every 5 seconds. Tested on a Raspberry Pi 4B 4gb, but should work on every pi.

## Demo Video: 

https://user-images.githubusercontent.com/80382873/121377995-79e96080-c94b-11eb-9548-1c13d9ebe573.mp4



## Dependencies: 
* Python3 - (comes on Raspbian and most other distros) - [Offical Python Site](https://www.python.org/downloads/)
* Python requests library - 
  `sudo pip3 install requests`
* Gpiozero library that connects to the pi's gpio headers - (comes on Raspbian)
  `sudo apt install python3-gpiozero` or `sudo pip3 install gpiozero`

This project is just a proof of concept, the delay of the API is unknown and could be long. This shouldn't be used as an alerting system. 

