import json

with open('C:\\Users\\z0041r0f\\Downloads\\onboardingKey.json') as file:
    data = json.load(file)

serialNumber = data['device']['serialNumber']
deviceIdentifier = data['device']['deviceIdentifier']
nwStatics = []
host = data['proxies']['agentProxy']['host']
clientID = data['agents'][0]['security']['clientId']
for nwinterface in data['device']['networkInterfaces']:
    nwStatics.append((nwinterface['static']['IPv4']))



print("Device serial number is: " + serialNumber)
print("Static IPv4's are: " + str(nwStatics))
print("Device identifier is : " + deviceIdentifier)
print("Secuirty clinetID is : " + clientID)
print("AgentProxy host is : " + host)
