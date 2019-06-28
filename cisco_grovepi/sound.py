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


from cisco_grovepi.senor import Sensor
from cisco_deviot.thing import Property, PropertyType


class Sound(Sensor):
    def __init__(self, tid, name, pin):
        Sensor.__init__(self, tid, name, pin, "sound")
        self.add_property(Property(name="volume", type=PropertyType.INT, value=0, unit="dB"))

    def update_state(self):
        data = Sensor.analog_read(self)
        if data is not None:
            self.update_property(volume=data)
