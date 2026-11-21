country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
 
# search dictionary for country code of India
print("Country code for USA -")
print(country_code.get('USA', 'Not Found'))
 
# search dictionary for country code of Japan
print("Country code for Australia -")
print(country_code.get('Australia', 'Not Found'))