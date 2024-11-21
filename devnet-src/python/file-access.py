devices = []
myfile = open("devices.txt","r")
for item in myfile:
    devices.append(item.strip())
myfile.close()
print(f"total: {len(devices)} of {devices}")

# alternate solution using "with"
with open("new-devices.txt","a+") as myfile:
    for item in myfile:
        devices.append(item.strip())
print(f"total: {len(devices)} of {devices}")
