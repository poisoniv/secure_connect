from functions import *

(username, password) = get_credentials()

if radius_challenge(username, password) :
    print("Accepted")
else :
    print("Failed")

print("Executed successfully...")