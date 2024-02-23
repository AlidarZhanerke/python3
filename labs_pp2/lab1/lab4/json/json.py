import json
#load - это когда мы считываем файл json
# 'r' - для чтения файла
with open('sample-data.json', 'r') as file:
    data = json.load(file)
print("Interface status")
print("=" * 80)
print("DN", " " * 40, "Description"," " * 8, "Speed"," " * 1 ,"MTU")
print("-" * 41, "-" * 22, "-" * 7, "-" * 6)
for it in data["imdata"]:
    for i in it["l1PhysIf"]:
        for j in it["l1PhysIf"]["attributes"]:
            print(it["l1PhysIf"]["attributes"]["dn"], "\t", "\t", "\t" ,it["l1PhysIf"]["attributes"]["speed"], it["l1PhysIf"]["attributes"]["mtu"])
    