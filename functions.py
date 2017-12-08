from meraki import meraki
from users import users
from config import config
import json
import ipaddress
import datetime

# probably also need to return the IP address of the requester?
def get_credentials():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return (username, password)


# need to replace this with more robust database lookup
def radius_challenge(username, password) :
    if username in users and password == users[username]:
        record(username, "Login Success")
        return True
    else:
        record(username, "Login Failure")
        return False


# this will probably be sent to a logging server of some sort...
def record(username, type) :
    print("{:%D} {:%H:%M:%S}  | Username: {} | Type: {}".format(datetime.datetime.now(), datetime.datetime.now(), username, type))
    log_file = open("log.txt", "a+")
    log_file.write("{:%D} {:%H:%M:%S} | Username: {} | Type: {}\n".format(datetime.datetime.now(), datetime.datetime.now(), username, type))
    log_file.close()
    return


# take user's IP address, apply ALC to firewall allowing access to that IP address
def apply_acl(username, customer, source_address, destination_address) :
    firewall_rules = meraki.getmxvpnfwrules(config['api_key'], config['org_id'], suppressprint=True)
    new_rule = {
        'comment': 'Allow {} access to {}.'.format(username, customer),
        'policy': 'allow',
        'protocol': 'any',
        'destPort': 'any',
        'destCidr': destination_address,
        'srcPort': 'Any',
        'srcCidr': source_address,
        'syslogEnabled': False
    }
    firewall_rules.insert(0, new_rule)
    firewall_rules.pop()
    meraki.updatemxvpnfwrules(config['api_key'], config['org_id'], firewall_rules, syslogDefaultRule=False, suppressprint=True)
    record(username, "Session Start")
    return


def remove_acl(username, source_address) :
    old_rule = meraki.getmxvpnfwrules(config['api_key'], config['org_id'], suppressprint=True)
    new_rule = []
    for rule in old_rule:
        if rule['srcCidr'] == source_address or rule['comment'] == 'Default rule':
            continue
        else:
            new_rule.append(rule)
    meraki.updatemxvpnfwrules(config['api_key'], config['org_id'], new_rule, syslogDefaultRule=False, suppressprint=True)
    record(username, "Session End")

def check_activity(network_id):
    analysis = meraki.getnetworktrafficstats(config['api_key'], network_id, timespan=86400, devicetype='combined', suppressprint=True)
    usage = (0, 0)
    print(usage)
    for app in analysis:
        try:
            if ipaddress.ip_address(app['destination']) in ipaddress.ip_network("8.8.8.0/24"):
                usage += (int(app['recv']), int(app['sent']))
        except ValueError:
            continue
    print(usage)


























