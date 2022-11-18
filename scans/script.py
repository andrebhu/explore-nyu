#!/usr/bin/env python3


subdomains = {

}

with open("subfinder.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        l = line.strip()
        chunks = l.split(".")
        try:
            if subdomains.get(chunks[-3]) == None:
                subdomains[chunks[-3]] = 1
            else:
                subdomains[chunks[-3]] += 1
        except:
            pass

for k, v in subdomains.items():
    print(k, v)
