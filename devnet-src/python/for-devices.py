devices = ["R1","R2","R3","S1","S2", "L3S1"]
switches = []
routers = []
for item in devices:
    if "S" in item:
        switches.append(item)
        print(item)
    elif "R" in item:
        routers.append(item)
        print(item)

print(f"my switches are: {switches}")
print(f"my routers are: {routers}")
