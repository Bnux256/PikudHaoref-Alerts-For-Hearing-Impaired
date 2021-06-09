# PikudHaoref-Alerts-For-Hearing-Impaired
Using a Raspberry Pi connected to the unoffical Pikud Haoref API to alert hearing imparied people of rocket alerts.
Made after Operation Guardian of the Walls.

Alerting using:
* a loud speaker
* a 3.3V buzzer
* a 3V eccentric vibrating motor - 45mA current - (bigger motors won't work).
* a powerful blinking LED - unsoldering usb desk light and connecting the 3V led to raspberry pi. 

Connecting to Pikud Haoref using the site API which uses a JSON files that shows the current alerts. For testing purpose the program checks for alerts every 5 seconds. 

