import bluetooth

print("looking for bluetooth connected device...")
nearby_devices=bluetooth.discover_devices(lookup_names=True)


for name in nearby_devices:
    #print("address :",addr)
    print("name :",name)