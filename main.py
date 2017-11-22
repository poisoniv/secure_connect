from meraki import meraki

file = open("api_key.txt", "r")
api_key = file.read()
#api_key = [insert here]
#print(api_key)

file = open("org_id.txt", "r")
org_id = file.read()
#org_id = '316511'
#print(org_id)

networks = meraki.getnetworklist(api_key, org_id, suppressprint=True)

output_file = open("output.txt", "w")

for network in networks :
    print("Network - " + network['name'] + "\n" + "------------------")
    output_file.write("Network - " + network['name'] + "\n" + "------------------" + "\n")

    devices = meraki.getnetworkdevices(api_key, network['id'], suppressprint=True)
    for device in devices :
        uplinks = meraki.getdeviceuplink(api_key, network['id'], device['serial'],suppressprint=True)
        for uplink in uplinks :
            print(device['name'] + "\n" + "Interface: " + uplink['interface'] + "\n" + "Status: " + uplink['status'] + "\n")
            output_file.write(device['name'] + "\n" + "Interface: " + uplink['interface'] + "\n" + "Status: " + uplink['status'] + "\n" + "\n")

output_file.close()