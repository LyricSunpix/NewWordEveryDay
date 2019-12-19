import csv
import telebot
import json

with open('example.csv', 'rt') as f:
    csv_reader = csv.reader(f)

data = [row for row in csv.reader(open('example.csv', 'rt'))]

bot_token = "MyToken"
bot_chatID = "MyChatID"
bot = telebot.TeleBot(bot_token)


def chooseword (liste,x):
    print(line)
    wordFR = liste[3+x][1]
    wordNO = liste[3+x][0]
    result = wordFR + " - " + wordNO
    print(result)
    bot.send_message(bot_chatID, result)

def load():
    json_file = open("data.json")
    data = json.load(json_file)
    return data #extraction de la variable

def updatejson(data_json):
    # data_json =  data_json['linenumber'] + 1 
    data_json['linenumber'] += 1
    json_file = open("data.json", "w")
    json.dump(data_json, json_file)



if __name__ == "__main__":
    print("Start")
    # print(bot.get_chat(bot_chatID).title)
    json_object = load()
    line = json_object['linenumber']
    print(line)
    chooseword(data, line)
    updatejson(json_object)
    # resultat = 123
    # print(multiply(resultat,4))
