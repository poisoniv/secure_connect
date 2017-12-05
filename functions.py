from meraki import meraki
import datetime

# probably also need to return the IP address of the requester?
def get_credentials():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return (username, password)


# need to replace this with more robust database lookup
def radius_challenge(username, password) :
    if username in ['admin'] and password in ['password'] :
        record(username, "Login Success")
        return True
    else :
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
def apply_acl(api_key, org_id, username, customer, source_address, destination_address) :
    firewall_rules = meraki.getmxvpnfwrules(api_key, org_id, suppressprint=True)
    new_rule = [
        {'comment': 'Allow user "' + username + '" access to ' + customer + '.', 'policy': 'allow', 'protocol': 'any',
         'destPort': 'any', 'destCidr': destination_address, 'srcPort': 'Any', 'srcCidr': source_address,
         'syslogEnabled': False}]
    firewall_rules.insert(0, new_rule)
    meraki.updatemxvpnfwrules(api_key, org_id, firewall_rules, syslogDefaultRule=False, suppressprint=True)
    record(username, "Session Start")
    return


def remove_acl(api_key, org_id, source_address) :
    firewall_rules = meraki.getmxvpnfwrules(api_key, org_id, suppressprint=True)
    firewall_rules.index(source_address)



    [1, 2, 3].index(2)  # => 1
    [1, 2, 3].index(4)  # => ValueError



    firewall_rules.insert(0, new_rule)
    meraki.updatemxvpnfwrules(api_key, org_id, firewall_rules, syslogDefaultRule=False, suppressprint=True)



    return
