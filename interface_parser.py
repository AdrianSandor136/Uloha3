import json

class Interface:
    def __init__(self, name, description, max_frame_size, config, port_channel_id):
        self.name = name
        self.description = description
        self.max_frame_size = max_frame_size
        self.config = config
        self.port_channel_id = port_channel_id

def parse_json_data(filename):
    with open(filename) as f:
        data = json.load(f)
        interfaces = parse_interface_data(data)
        return interfaces

def parse_interface_data(data):
    interfaces = []
    for interface in data["frinx-uniconfig-topology:configuration"]["openconfig-interfaces:interfaces"]["interface"]:
        if "Ethernet" in interface["name"] or "Port-channel" in interface["name"]:
            name = interface["name"]
            config = interface["config"]

            description = config.get("description", None)
            max_frame_size = config.get("mtu", None)
            port_channel_id = None
            if "Cisco-IOS-XE-ethernet:channel-group" in config:
                port_channel_id = config["Cisco-IOS-XE-ethernet:channel-group"]["number"]

            new_interface = Interface(name, description, max_frame_size, config, port_channel_id)
            interfaces.append(new_interface)

    return interfaces
