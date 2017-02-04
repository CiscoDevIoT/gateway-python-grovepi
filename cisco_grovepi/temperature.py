# coding=utf-8
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


import math
from cisco_deviot.thing import Property
from cisco_grovepi.senor import Sensor


class Temperature(Sensor):
    def __init__(self, tid, name, pin):
        Sensor.__init__(self, tid, name, pin)
        self.add_property(Property(name="value", unit="°C", range=[0, 100]))
        self.value = 0

    def update_state(self):
        data = Sensor.analog_read(self)
        if data is not None and data is not 0:
            resistance = (1023 - data) * 10000.0 / data
            self.value = 1 / (math.log(resistance / 10000) / 4250 + 1 / 298.15) - 273.15 + 100
