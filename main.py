from functions import *
from meraki import meraki
import ipaddress
import json
import time



source_address = "10.0.1.3/32"
customer = "EA"
destination_address = "10.0.2.0/24"

(username, password) = get_credentials()


if radius_challenge(username, password) == False:
   exit(code="Login Failure")

apply_acl(username, customer, source_address, destination_address)
time.sleep(60)
remove_acl(username, source_address)


network_id = 'L_638385247179767950'
check_activity(network_id)




print("Executed successfully...")