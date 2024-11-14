nativeVLAN = input("enter the number of the native VLAN: ")
dataVLAN = input("enter the number of the data VLAN: ")
if nativeVLAN == dataVLAN:
    print(f"The native and data VLAN's are the same: '{dataVLAN}'")
else:
    print(f"The native '{nativeVLAN}' and data '{dataVLAN}' VLAN's are different")
