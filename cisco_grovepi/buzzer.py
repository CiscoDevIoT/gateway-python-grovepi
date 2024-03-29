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

# The class for a buzzer (Grove - Buzzer)

import threading
import time
from cisco_deviot.thing import Action, Property, PropertyType
from cisco_grovepi.sensor import Sensor


class Buzzer(Sensor):
    ON = 1
    OFF = 0

    def __init__(self, tid, name, pin):
        Sensor.__init__(self, tid, name, pin, "buzzer")
        self.add_action(Action("turn_on"))
        self.add_action(Action("turn_off"))
        self.add_action(Action("beep").
                        add_parameter(Property(name="duration", type=PropertyType.INT, value=10, range=[10, 100])).
                        add_parameter(Property(name="interval", type=PropertyType.INT, value=1, range=[1, 10])))
        self.working_thread = None

    def turn_on(self):
        Sensor.digital_write(self, Buzzer.ON)

    def turn_off(self):
        Sensor.digital_write(self, Buzzer.OFF)

    def beep(self, duration, interval):
        if self.working_thread is None:
            self.working_thread = threading.Thread(target=Buzzer.__working_function, args=(self, duration, interval))
            self.working_thread.daemon = True
            self.working_thread.start()

    def __working_function(self, duration, interval):
        while duration > 0:
            self.turn_on()
            time.sleep(interval)
            duration -= interval
            self.turn_off()
            time.sleep(interval)
            duration -= interval
        self.working_thread = None
