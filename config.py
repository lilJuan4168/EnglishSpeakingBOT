import json
from time import sleep
from os import system

print("\nCONFIGURATION\n")
openaiAPIkey = input("Set your 'openai API key'(required): ")

maxTokens = int(input("\nSet the amount of words your response will have [50(short) to 500(long)]: "))

seconds = int(input("\nSet amount of time in seconds the BOT will hear you [10 to 20]: "))

modelSet = input("\nSet model for the listening AI [base(recomended) or small]: ")

languages = input("\nSet language [es(spanish), en(english), en-uk(englishUK), fr-fr(french)]: ")
sleep(1)
system('clear')

variables = {}
variables['openaiAPIkey'] = openaiAPIkey
variables['maxTokens'] = maxTokens
variables['seconds'] = seconds
variables['modelSet'] = modelSet
variables['languages'] = languages
for key, value in variables.items():
    print(key,"--->",value)
commit = input("\nsave changes? [Y/n]: ")
    
if commit.upper() == 'Y':
    sleep(1)
    system('clear')
    with open("dataConfig.json", "w") as data:     
        json.dump(variables, data, indent=4)
    print("Saving...")
    sleep(2)
    print("Complete!")
else:
    print("changes do not saved...try again")
    sleep(2)