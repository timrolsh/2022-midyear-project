city_list = open("data/city_list.txt")
idk = {}
for line in city_list:
    temp = line.split()
    idk[temp[0]] = temp[1]

print(idk)
