from meraki import meraki
from users import users
import datetime


# probably also need to return the IP address of the requester?
def get_credentials():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return (username, password)


# need to replace this with more robust database lookup
def radius_challenge(username, password):
    if username in users and password == users[username]:
        return True
    else:
        return False


# this will probably be sent to a logging server of some sort...
def record(username, type):
    print("{:%D} {:%H:%M:%S}  | Username: {} | Type: {}".format(datetime.datetime.now(), datetime.datetime.now(), username, type))
    log_file = open("log.txt", "a+")
    log_file.write("{:%D} {:%H:%M:%S} | Username: {} | Type: {}\n".format(datetime.datetime.now(), datetime.datetime.now(), username, type))
    log_file.close()
    return


# take user's IP address, apply ALC to firewall allowing access to that IP address
def apply_acl(api_key, org_id, username, ip_address, source, destination_address) :
    firewall_rules = meraki.getmxvpnfwrules(api_key, org_id, suppressprint=True)
    # want to be more specific in the comment
    new_rule = \
        [
            {'comment': 'Allow user "' + username + '" access to customer [insert customer]',
             'policy': 'allow',
             'protocol': 'any',
             'destPort': 'any',
             'destCidr': destination_address,
             'srcPort': 'Any',
             'srcCidr': ip_address,
             'syslogEnabled': True
             }]

    firewall_rules.insert(0, new_rule)

    meraki.updatemxvpnfwrules(api_key, org_id, firewall_rules, syslogDefaultRule=False, suppressprint=True)




    return



def remove_acl() :
    return

    #Retrieve list of networks in organization
    networks = meraki.getnetworklist(api_key, org_id, suppressprint=True)

    #iterate through each device in each network, check status of device/uplink and set variable 'network_status' to "Down" if applicable
    #if device/uplink is down, skip rest of loop, print findings, and continue with next network
    for network in networks :
        network_status = "Up";
        devices = meraki.getnetworkdevices(api_key, network['id'], suppressprint=True)
        for device in devices:
            if network_status == "Down" : break
            uplinks = meraki.getdeviceuplink(api_key, network['id'], device['serial'],suppressprint=True)
            for uplink in uplinks :
                if (uplink['status'] == "Failed") :
                    network_status = "Down"
                    break

        #print status of each network to console and output.txt
        print(network['name'] + " - " + network_status)
        output_file.write(network['name'] + " - " + network_status + "\n")

    output_file.close()

    return