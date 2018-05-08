import json
from pprint import pprint

json_file = raw_input("Json file you'd like to Pretty Print: ")
with open(json_file) as f:
    data = json.load(f)

pprint(data)