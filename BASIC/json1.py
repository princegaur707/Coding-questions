import json #It makes dictionary of given string

#the JSON object must be str, bytes or bytearray, not dict
data='{"var1":"A","var2":"B"}'
print(data)
#print(data['var1']) #this will cause error as it is just string(string index must be zero)

parsed=json.loads(data)
print(parsed)
print(parsed['var1'])

data2={
    "channel_name":"codewith",
    "cars":['bmw','audi','ferrari'],
    "isbad": False #json use small f (false)
}

jscomp= json.dumps(data2) #it will convert data 2 to json format
print(jscomp)

#TASKS: json.load, sort_keys_parameter in dumps