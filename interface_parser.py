import json

class Interface:
    def __init__(self, name, description, max_frame_size, config, port_channel_id):
        # Initialize an interface with the provided data.
        self.name = name
        self.description = description
        self.max_frame_size = max_frame_size
        self.config = config
        self.port_channel_id = port_channel_id

def parse_json_data(filename):
    # Load and parse the JSON data from the given file.
    with open(filename) as f:
        data = json.load(f)
        interfaces = parse_interface_data(data)
        return interfaces

def parse_interface_data(data):
    interfaces = []
    for interface in data["frinx-uniconfig-topology:configuration"]["openconfig-interfaces:interfaces"]["interface"]:
        # Check if the interface name includes "Ethernet" or "Port-channel".
        if "Ethernet" in interface["name"] or "Port-channel" in interface["name"]:
            name = interface["name"]
            config = interface["config"]
            
        # Extract the description and max frame size from the config, if they exist.
            description = config.get("description", None)
            max_frame_size = config.get("mtu", None)
            port_channel_id = None
        # Extract the port channel ID from the config, if it exists.
            if "Cisco-IOS-XE-ethernet:channel-group" in config:
                port_channel_id = config["Cisco-IOS-XE-ethernet:channel-group"]["number"]
                
        # Create a new Interface object and add it to the list of interfaces.
            new_interface = Interface(name, description, max_frame_size, config, port_channel_id)
            interfaces.append(new_interface)

    return interfaces
