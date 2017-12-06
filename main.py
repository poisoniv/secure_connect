from functions import *
import time

source_address = "192.168.1.30/32"
customer = "EA"
destination_address = "any"

(username, password) = get_credentials()

if radius_challenge(username, password) == False:
   exit(code="Login Failure")

apply_acl(username, customer, source_address, destination_address)
time.sleep(60)
remove_acl(username, source_address)

print("Executed successfully...")