# RedAlerts-For-Hearing-Impaired
Using a Raspberry Pi connected to the unoffical Pikud Haoref API to alert hearing imparied people of rocket alerts.
Made after Operation Guardian of the Walls.

Alerting using:
* a loud speaker
* a 3.3V buzzer
* a 3V eccentric vibrating motor - 45mA current - (bigger motors won't work).
* a powerful blinking LED - unsoldering usb desk light and connecting the 3V led to raspberry pi. 

Connecting to Pikud Haoref using the unoffical site API which uses a JSON files that shows the current alerts. For testing purpose the program checks for alerts every 5 seconds.

Demo Video: 

https://user-images.githubusercontent.com/80382873/121377995-79e96080-c94b-11eb-9548-1c13d9ebe573.mp4



This project is just a proof of concept, the delay of the API is unknown and could be long. This shouldn't be used as an alerting system. 

