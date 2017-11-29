import functions

username = input("Enter username: ")
password = input("Enter password: ")

type = 0;

if functions.radius_challenge(username, password) :
    print("Accepted")
    functions.record(username, type)
else :
    print("Failed")
    type = 1;
    functions.record(username, type)

#functions.get_status()

print("Executed successfully...")