# initializing dictionary
test_dict = {
    '1': {
        'underHeaderHeading0': "value0",
        'underHeaderHeading1': "value1",
        'underHeaderHeading2': "value2"
    }
}

# initializing search key string 
search_key = 'underHeader'
result = []
# printing original dictionary
for key, value in test_dict.items():
    for subKey in test_dict.get(key, {}):
        print(test_dict[key][subKey])
# print(str(res))