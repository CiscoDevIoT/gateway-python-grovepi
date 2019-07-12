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


from cisco_deviot.thing import Thing
import grovepi


class Sensor(Thing):
    def __init__(self, tid, name, pin, kind=None):
        Thing.__init__(self, tid, name, kind)
        self.pin = pin

    def digital_write(self, data):
        try:
            grovepi.pinMode(self.pin, 'OUTPUT')
            grovepi.digitalWrite(self.pin, data)
        except IOError:
            pass

    def analog_write(self, data):
        try:
            grovepi.pinMode(self.pin, 'OUTPUT')
            grovepi.analogWrite(self.pin, data)
        except IOError:
            pass

    def digital_read(self):
        try:
            return grovepi.digitalRead(self.pin)
        except IOError:
            return None

    def analog_read(self, mode="analog"):
        try:
            if mode is 'analog':
                data = grovepi.analogRead(self.pin)
                if data > 1023:
                    return None
                return data
            elif mode == 'dht': # a humidity and temperature sensor
                temp, hum = grovepi.dht(self.pin, 0)
                return temp, hum
            elif mode == 'ultrasonic': # an ultrasonic distance sensor
                distance = grovepi.ultrasonicRead(self.pin)
                return distance
        except IOError:
            return None

    def update_state(self):
        pass
