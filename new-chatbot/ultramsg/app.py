from flask import Flask, request, jsonify
from ultrabot import ultraChatBot
import json
# from flask_apscheduler import APScheduler
import os

app = Flask(__name__)
# apscheduler = APScheduler()

# @app.route('/', methods=['POST'])
# def home():
#     if request.method == 'POST':
#         bot = ultraChatBot(request.json)
#         return bot.Processingـincomingـmessages()
@app.route('/send', methods=['GET'])
def sendDaily():
    bot = ultraChatBot({'data': ''})
    for i in range(50):
        with open("database.txt", "r") as infile:
            for line in infile:
                number = '91' + line.rstrip(';\n') + '@c.us'
                text ="""Every piece of the puzzle that doesn't fit gets you closer to the answer.
    - 𝗖𝘆𝗻𝘁𝗵𝗶𝗮 𝗟𝗲𝘄𝗶𝘀

    Hello everyone,
    Gear up and mark the dates for some fun-filled brainstorming and a wonderful evening as 𝗡𝗲𝗵𝗿𝘂 𝗛𝗮𝗹𝗹 𝗼𝗳 𝗥𝗲𝘀𝗶𝗱𝗲𝗻𝗰𝗲 brings to you, the 𝗣𝘂𝘇𝘇𝗹𝗲 𝗤𝘂𝗶𝘇
    𝗗𝗮𝘁𝗲: 31/03/2023
    𝗧𝗶𝗺𝗲: 7:15 pm
    𝗩𝗲𝗻𝘂𝗲: V2, Vikramshila

    The top three winners will be awarded cash prizes -
    1st - INR 5000
    2nd - INR 3000
    3rd - INR 1000
    Link for registration : https://forms.gle/T27zgaoS9evvqvrp7

    For any queries, contact -
    𝗗𝗶𝗴𝘃𝗶𝗷𝗮𝘆 𝗦𝗶𝗻𝗴𝗵  : 9960278772 """
                image = "https://drive.google.com/file/d/1V125dA-jDAKj1Pmb850x5kiKiQbmKPrd/view?usp=sharing"
                bot.send_message(number, text)
                bot.send_image(number, image)
                print(f"{number} sent")

if __name__ == '__main__':
    # apscheduler.add_job(id = 'Scheduled Task', func=sendDaily, trigger = 'cron', hour = '17', minute = '36')
    # apscheduler.start()
    app.run()
