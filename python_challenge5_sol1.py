'''Day 5: Jina2 templates
Using the Jinja2 templating language, create a template from the below router configuration parameterising hostname, domain name, username, password, ip address and mask.
Create a dictionary to hold the template values so that they can be used to parse the template and write the output to a file using the hostname to ensure the file is unique.
Enhance the data model to incorporate two (2) additional devices that can also be parsed using the same template.
hostname csr1kv-1
!
aaa new-model
!
aaa authentication login default local
aaa authorization exec default local 
!
ip name-server 8.8.8.8
!
ip domain name example.net
!
username admin privilege 15 secret cisco123
!
interface GigabitEthernet1
 description *** Management Interface ***
 vrf forwarding Mgmt-vrf
 no ip address
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 negotiation auto
 ip address 10.0.0.1 255.255.255.0
 no ipv6 redirects
 no ipv6 unreachables
 no mop enabled
 no mop sysid
 no shutdown
!
'''
from jinja2 import Template

ios_template = """
hostname {{ hostname }}
!
aaa new-model
!
aaa authentication login default local
aaa authorization exec default local 
!
ip name-server 8.8.8.8
!
ip domain name {{ domain_name }}
!
username {{ username }} privilege 15 secret {{ password }}
!
interface GigabitEthernet1
 description *** Management Interface ***
 vrf forwarding Mgmt-vrf
 no ip address
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 negotiation auto
 ip address {{ ipv4_address_1 }} {{ ipv4_netmask_1 }}
 no ipv6 redirects
 no ipv6 unreachables
 no mop enabled
 no mop sysid
 no shutdown
!
"""

device_dict = {
    'asr1k-1': {
        'hostname': 'asr1k-1',
        'username': 'admin',
        'password': 'C1sco123',
        'domain_name': 'cisco.com',
        'ipv4_address_1': '10.0.0.1',
        'ipv4_netmask_1': '255.255.255.252'
    },
    'asr1k-2': {
        'hostname': 'asr1k-2',
        'username': 'admin2',
        'password': 'S4f3rth4nU',
        'domain_name': 'cisco.com',
        'ipv4_address_1': '10.0.0.5',
        'ipv4_netmask_1': '255.255.255.252'
    },
    'asr1k-3': {
        'hostname': 'asr1k-3',
        'username': 'admin3',
        'password': 'cr4zystUf5',
        'domain_name': 'cisco.com',
        'ipv4_address_1': '10.0.0.9',
        'ipv4_netmask_1': '255.255.255.252'
    }
}
for host, device in device_dict.items():
    t = Template(ios_template)
    config_out = t.render(device)
    filename = '{}.cfg'.format(device_dict['hostname'])
    with open(filename, "w") as fh:
        fh.write(config_out)
    print(config_out)