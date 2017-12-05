import functions

(username, password) = functions.get_credentials()

if functions.radius_challenge(username, password) :
    print("Accepted")
    functions.record(username, "Login Success")
else :
    print("Failed")
    functions.record(username, "Login Failure")

#functions.get_status()

print("Executed successfully...")