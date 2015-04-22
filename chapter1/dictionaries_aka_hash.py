# when constructing a dictionary, each key is separated from its value by a colon, and we separate items by commas.
services = {'ftp':21,'ssh':22,'smtp':25,'http':80}
# adding .keys() to a dictionary value will display all keys.
print services.keys()
# adding .items() to a dictionary value will display all values
print services.items()
# adding has_key() will tell us if a certain key exists...
print services.has_key('ftp')
