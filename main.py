import json
import requests
from time import sleep
from raspberryPiBlinker import gpioAlert


def getRedAlerts():
    # get red alerts
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.oref.org.il/11088-13708-he/Pakar.aspx",
    }
    host = "https://www.oref.org.il/WarningMessages/alert/alerts.json"
    response = requests.get(host, headers=headers)
    if response.content == b'':  # if empty, return is null
        return None
    # parse the json response
    json_response = json.loads(response.content.decode('utf8'))["data"]
    # check if there is no alerts - if so, return is null.
    if len(json_response) == 0:
        return None
    return json_response


def main():
    # main listener function that check
    while True:  # always checking for alerts
        sleep(5)  # be nice to their servers
        red_alerts = getRedAlerts()
        if red_alerts is None:
            print("[-] No alerts for now, keep checking ...")
        else:  # if there is an alert right now
            print("Alert! Alert!")
            gpioAlert()    # making raspberry pi alert the user


if __name__ == '__main__':
    main()
