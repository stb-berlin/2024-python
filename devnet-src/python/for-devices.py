devices=["R1","R2","R3","S1","S2"]
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)
        print(item)

print(f"my switches are: {switches}")
