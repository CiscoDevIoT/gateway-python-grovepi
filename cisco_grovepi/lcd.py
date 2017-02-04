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


from cisco_deviot.thing import Action, PropertyTypeString
from cisco_grovepi.helper.grove_rgb_lcd import setText
from cisco_grovepi.senor import Sensor


class Lcd(Sensor):
    def __init__(self, tid, name, pin):
        Sensor.__init__(self, tid, name, pin)
        self.add_action(Action("display", message=PropertyTypeString))

    def display(self, message):
        setText(message)
