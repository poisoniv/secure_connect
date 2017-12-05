from functions import *

(username, password) = get_credentials()

if radius_challenge(username, password):
    print("Accepted")
    record(username, "Login Success")
else:
    print("Failed")
    record(username, "Login Failure")

print("Executed successfully...")