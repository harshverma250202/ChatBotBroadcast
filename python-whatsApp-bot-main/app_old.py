from flask import Flask, request, jsonify
from ultrabot import ultraChatBot
import json
from flask_apscheduler import APScheduler
import os

app = Flask(__name__)
apscheduler = APScheduler()

@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        bot = ultraChatBot(request.json)
        return bot.Processingـincomingـmessages()

def sendDaily():
    bot = ultraChatBot({'data': ''})
    folders = ['Consult', 'DS-ML', 'Finance', 'PM', 'Quant', 'Software']
    for folder in folders:
        days = [6, 5, 4, 3, 2, 1]
        for day in days:
            # check if numbers.txt present in the folder
            if os.path.exists(f"Recurring/{folder}/Day {day}/numbers.txt"):
                with open(f"Recurring/{folder}/Day {day}/numbers.txt", "r") as infile:
                    for line in infile:
                        number = line.rstrip(';\n')
                        with open(f"Recurring/{folder}/Day {day}/content.txt", "r") as content:
                            # read each line as a dict object
                            for line in content:
                                if line.split(')')[0] == "(text":
                                    text = line.split(')')[1].rstrip('\n')
                                    bot.send_message(number, text)
                                else:
                                    filename = line.split(')')[0].split('-')[1] + '.pdf'
                                    document = line.split(')')[1].rstrip('\n')
                                    bot.send_document(number, filename, document)
                                print(f"{folder} Day {day} sent to {number}")
                                
                    # shift this day's numbers to next day
                    if day < 6:
                        with open(f"Recurring/{folder}/Day {day+1}/numbers.txt", "w") as outfile:
                            with open(f"Recurring/{folder}/Day {day}/numbers.txt", "r") as new_infile:
                                for line in new_infile:
                                    outfile.write(line)

                # delete this day's numbers
                os.remove(f"Recurring/{folder}/Day {day}/numbers.txt")
                print(f"{folder} Day {day} done")

if __name__ == '__main__':
    apscheduler.add_job(id = 'Scheduled Task', func=sendDaily, trigger="interval", seconds = 5)
    # apscheduler.add_job(id = 'Scheduled Task', func=sendDaily, trigger = 'cron', hour = '11', minute = '45')
    apscheduler.start()
    app.run()
