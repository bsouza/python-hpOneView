# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2016) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from pprint import pprint
from hpOneView.oneview_client import OneViewClient
from hpOneView.exceptions import HPOneViewException
from config_loader import try_load_from_file

config = {
    "ip": "",
    "credentials": {
        "userName": "administrator",
        "password": ""
    }
}

# Try load config from a file (if there is a config file)
config = try_load_from_file(config)

oneview_client = OneViewClient(config)

# Get the first two Interconnects
print("Get the first two interconnects")
try:
    interconnects = oneview_client.interconnects.get_all(0, 2)
    pprint(interconnects)
except HPOneViewException as e:
    print(e.msg['message'])

# Get Interconnects Statistics
print("Get an interconnect statistics")
try:
    interconnect_statistics = oneview_client.interconnects.get_statistics("ad28cf21-8b15-4f92-bdcf-51cb2042db32")
    pprint(interconnect_statistics['moduleStatistics'])
except HPOneViewException as e:
    print(e.msg['message'])

# Get the Statistics from a port of an Interconnects
print("Get the port statistics for downlink port 1 on the interconnect "
      "that matches ID ad28cf21-8b15-4f92-bdcf-51cb2042db32")
try:
    statistics = oneview_client.interconnects.get_statistics("ad28cf21-8b15-4f92-bdcf-51cb2042db32", "d1")
    pprint(statistics)
except HPOneViewException as e:
    print(e.msg['message'])

# Get the subport Statistics from a port of an Interconnects
print("Get the subport statistics for subport 1 on downlink port 2 on the interconnect "
      "that matches ID ad28cf21-8b15-4f92-bdcf-51cb2042db32")
try:
    statistics = oneview_client.interconnects.get_subport_statistics("ad28cf21-8b15-4f92-bdcf-51cb2042db32", "d2", 1)
    pprint(statistics)
except HPOneViewException as e:
    print(e.msg['message'])

# Get by ID
print("Get Interconnect that matches ID 66fd5e22-5a71-4605-a7e9-b6ead772ea4d")
try:
    interconnect = oneview_client.interconnects.get('66fd5e22-5a71-4605-a7e9-b6ead772ea4d')
    pprint(interconnect)
except HPOneViewException as e:
    print(e.msg['message'])

# Turn the power off
print("Turn the power off and the UID light to 'Off' for interconnect " +
      "that matches ID 66fd5e22-5a71-4605-a7e9-b6ead772ea4d")
try:
    interconnect = oneview_client.interconnects.patch(
        id_or_uri='e542bdab-c75f-4cf2-b89e-9a566849e292',
        operation='replace',
        path='/powerState',
        value='Off'
    )
    pprint(interconnect)
except HPOneViewException as e:
    print(e.msg)

port = {
    "type": "port",
    "bayNumber": 1,
    "pairedPortName": None,
    "subports": None,
    "connectorType": "absent",
    "associatedUplinkSetUri": None,
    "available": True,
    "portStatusReason": "Unknown",
    "vendorSpecificPortName": None,
    "portRunningCapabilityType": None,
    "neighbor": None,
    "lagId": 0,
    "interconnectName": "Encl2, interconnect 1",
    "lagStates": None,
    "portTypeExtended": "External",
    "enabled": False,
    "vlans": None,
    "dcbxInfo": None,
    "portStatus": "Unlinked",
    "portName": "Q1.1",
    "portType": "Uplink",
    "fcPortProperties": None,
    "portId": "ad28cf21-8b15-4f92-bdcf-51cb2042db32:Q1.1",
    "portMonitorConfigInfo": "NotMonitored",
    "portHealthStatus": "Disabled",
    "capability": [
        "EnetFcoe",
        "Ethernet"
    ],
    "operationalSpeed": "Speed_0M",
    "configPortTypes": [
        "EnetFcoe",
        "Ethernet"
    ],
    "portSplitMode": "NotApplicable",
    "description": None,
    "name": "Q1.1",
    "state": None,
    "status": "Disabled",
    "category": "ports",
    "created": None,
    "modified": None,
    "eTag": None,
    "uri": "/rest/interconnects/ad28cf21-8b15-4f92-bdcf-51cb2042db32/ports/ad28cf21-8b15-4f92-bdcf-51cb2042db32:Q1.1"
}

# Updates an interconnect port.
print("Update the interconnect port")
try:
    updated = oneview_client.interconnects.update_port(port, "ad28cf21-8b15-4f92-bdcf-51cb2042db32")
    pprint(updated)
except HPOneViewException as e:
    print(e.msg['message'])

# Reset of port protection.
print("Trigger a reset of port protection of the interconnect hat matches ID ad28cf21-8b15-4f92-bdcf-51cb2042db32")
try:
    result = oneview_client.interconnects.reset_port_protection("ad28cf21-8b15-4f92-bdcf-51cb2042db32")
    pprint(result)
except HPOneViewException as e:
    print(e.msg['message'])

# Get name servers
print("Get name servers that matches ID ba4d2df2-a8d9-4fdc-928f-c47703382738")
try:
    interconnect_ns = oneview_client.interconnects.get_name_servers('ba4d2df2-a8d9-4fdc-928f-c47703382738')
    pprint(interconnect_ns)
except HPOneViewException as e:
    print(e.msg['message'])
