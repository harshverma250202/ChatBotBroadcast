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

@app.route('/send', methods=['POST'])
def sendDaily():
    bot = ultraChatBot({'data': ''})
    with open("database.txt", "r") as infile:
        for line in infile:
            number = '91' + line.rstrip(';\n') + '@c.us'
            text ="""Vote for *Digvijay Singh* for *GSec Tech* for actual change, driven by a vision to make IIT Kharagpur a technical pioneer in multiple domains and providing medium to achieve this milestone while bringing top placement options and avenues for the pupils.
*Veena Nikhita* for *GSec Student Welfare*
*Shreyansh Jha* for *VP*

http://tiny.cc/kgpvote """
            image = "https://digvijaygsec.s3.ap-south-1.amazonaws.com/IMG-20230404-WA0032.jpg"
            image2="https://digvijaygsec.s3.ap-south-1.amazonaws.com/IMG-20230404-WA0033+(2).jpg"
            # bot.send_message(number, text)
            bot.send_image(number, image,text)
            # bot.send_image(number, image2)
            print(f"{number} sent")
    return "done"

if __name__ == '__main__':
    # apscheduler.add_job(id = 'Scheduled Task', func=sendDaily, trigger = 'cron', hour = '17', minute = '36')
    # apscheduler.start()
    app.run()
