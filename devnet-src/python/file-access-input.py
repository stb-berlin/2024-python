#! /usr/bin/env python3

devices = []
while True:
    new_item = input("Enter device name or type 'exit' to quit: ")
    if new_item == 'exit':
        break

    print("work in progress")
    # alternate solution using "with"
    with open("devices.txt","r") as myfile:
        for item in myfile:
            devices.append(item.strip())
    print(f"total: {len(devices)} of {devices}")
