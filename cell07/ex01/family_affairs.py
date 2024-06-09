#!/usr/bin/env python3

def find_the_redheads(family:dict):
	return list(filter(lambda name: family[name] == "red", family.keys()))
    #return [name for name, color in family.items() if is_red(color)]

dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}

print(find_the_redheads(dupont_family))
