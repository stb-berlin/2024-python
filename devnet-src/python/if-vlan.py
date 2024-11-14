nativeVLAN = 1
dataVLAN = 100
if nativeVLAN == dataVLAN:
    print(f"The native and data VLAN's are the same: {dataVLAN}")
else:
    print(f"The native {nativeVLAN} and data {dataVLAN} VLAN's are different")
