from meraki import meraki
import datetime

def radius_challenge(username, password) :
    #need to replace this with database lookup
    if username in ['admin'] and password in ['password']: return True
    else : return False

def record(username, type) :
    # Create log file named log.txt
    #log_file = open("log.txt", "a+")
    #log_file.write("Action: " + type + ", User: " + username + ", Time: " + datetime.datetime.now())
    print("Action: " + type + ", User: " + username + ", Time: " + datetime.datetime.now())




    return



def get_status():
    file = open("api_key.txt", "r")
    api_key = file.read()
    # api_key = [insert here]
    # print(api_key)

    file = open("org_id.txt", "r")
    org_id = file.read()
    # org_id = '316511'
    # print(org_id)

    # Create output file named output.txt
    output_file = open("log.txt", "w")

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