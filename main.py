import openai
import configparser

#imports configuration file storing API key
#pulls API key from config file
def get_Key():
    config = configparser.ConfigParser()
    config.read('config.py')
    return config['KEYS']['api_key']

#Initializes the OpenAI API and sends a request to the GPT-3 Model
def askActif(whatup):
    openai.api_key = get_Key()
    actif8 = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = whatup,
        temperature = 0.7,
        max_tokens = 175
    )
    return print(actif8.choices[0].text)
#Infintely loops askActif, passing the user's input(myQuery) as the prompt
def main():
    while True:
        print('What would you like to ask Actif?\n')
        myQuery = input()
        askActif(myQuery)
        print('\n')

main()


