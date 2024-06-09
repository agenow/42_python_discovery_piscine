#!/usr/bin/env python3

def array_of_names(names:dict):
	namelist = []
	for key, value in names.items():
		namelist.append(key.capitalize() + " " + value.capitalize())
	return namelist

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(array_of_names(persons))
