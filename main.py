# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
import socket
import time
import argparse
import importlib
import traceback

from cisco_deviot.gateway import Gateway
from cisco_deviot import logger
from cisco_grovepi.sensor import Sensor


def class_for_name(mod_name, class_name):
    try:
        m = importlib.import_module(mod_name)
        c = getattr(m, class_name)
    except:
        logger.warn("There is no sensor class called {name}".format(name=mod_name)) 
        return Sensor
    return c


def load_configs(filename):
    with open(filename) as json_data:
        return json.load(json_data)

def is_number(text):
    try:
        int(text)
    except ValueError:
        return False
    return True

def pin_number(pin):
    if isinstance(pin, str):
        if is_number(pin):
            pin_value = int(pin)
        else:
            if pin[0] != 'A' and pin[0] != 'D':
                return None
            if not is_number(pin[1:]):
                return None
            pin_value = int(pin[1:]) + (14 if pin[0] == 'A' else 0)
    elif isinstance(pin, int):
        pin_value = pin
    else:
        return None
    return pin_value if (pin_value >= 0 and pin_value <= 19) else None
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gateway-python-starter-kit.')
    parser.add_argument('--deviot-server', dest='deviot_server', type=str, default='deviot.cisco.com',
                        help='url of deviot-server, eg: deviot.cisco.com')
    parser.add_argument('--mqtt-server', dest='mqtt_server', type=str, default='deviot.cisco.com:18883',
                        help='url of mqtt-server, eg: deviot.cisco.com:18883')
    parser.add_argument('--account', dest="account", type=str, default='')
    args = parser.parse_args()

    hostname = socket.gethostname()
    gateway = Gateway(name="rpi_" + hostname.lower(),
                      deviot_server=args.deviot_server,
                      connector_server=args.mqtt_server,
                      account=args.account)
    sensors = load_configs('sensors.json')
    for sensor in sensors:
        name = sensor["name"]
        pin = pin_number(str(sensor["pin"])) # str is the temporary solution for python 2
        stype = sensor["type"]
        if pin is None:
            logger.warn("The {type} {name} has the wrong pin number {pin}".format(type=stype, name=name, pin=sensor["pin"]))
            continue
        sid = stype.lower() + "_" + str(pin)
        klass = class_for_name("cisco_grovepi."+stype, stype.capitalize())
        instance = klass(sid, name, pin)
        if "options" in sensor:
            instance.options = sensor["options"]
        gateway.register(instance)

    gateway.start()
    while True:
        try:
            time.sleep(0.5)
            for instance in gateway.things.values():
                if getattr(instance, 'update_state', None):
                    instance.update_state()
        except:
            traceback.print_exc()
            break

    gateway.stop()
