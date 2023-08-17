import json
import requests
import datetime

class ultraChatBot():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['data']
        self.ultraAPIUrl = 'https://api.ultramsg.com/instance42492/'
        self.token = '7fuu2sy4an3dqgbo'

   
    def send_requests(self, type, data):
        url = f"{self.ultraAPIUrl}{type}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_message(self, chatID, text):
        data = {"to" : chatID,
                "body" : text}  
        answer = self.send_requests('messages/chat', data)
        return answer

    def send_image(self, chatID, image,caption):
        data = {"to" : chatID,
                "image" : image,
                "caption":caption} 
        answer = self.send_requests('messages/image', data)
        return answer

    def send_video(self, chatID):
        data = {"to" : chatID,
                "video" : "https://file-example.s3-accelerate.amazonaws.com/video/test.mp4"}  
        answer = self.send_requests('messages/video', data)
        return answer

    def send_audio(self, chatID):
        data = {"to" : chatID,
                "audio" : "https://file-example.s3-accelerate.amazonaws.com/audio/2.mp3"}  
        answer = self.send_requests('messages/audio', data)
        return answer


    def send_voice(self, chatID):
        data = {"to" : chatID,
                "audio" : "https://file-example.s3-accelerate.amazonaws.com/voice/oog_example.ogg"}  
        answer = self.send_requests('messages/voice', data)
        return answer

    def send_contact(self, chatID):
        data = {"to" : chatID,
                "contact" : "14000000001@c.us"}  
        answer = self.send_requests('messages/contact', data)
        return answer

    def time(self, chatID):
        t = datetime.datetime.now()
        time = t.strftime('%Y-%m-%d %H:%M:%S')
        return self.send_message(chatID, time)

    def welcome(self,chatID):
        welcome_string = "Hello!\nPlease type *Help* to see the list of commands.\n"
        return self.send_message(chatID, welcome_string)
    
    def not_found(self, chatID):
        not_found_string = "Command not Found\nPlease type *Help* to see the list of commands.\n"
        return self.send_message(chatID, not_found_string)
    
    def cdc(self,chatID):
        cdc_string = "https://www.cdccompanion.com"
        return self.send_message(chatID, cdc_string)

    def send_document(self, chatID, filename, document):
        data = {"to" : chatID,
                "filename": filename,
                "document" : document}  
        answer = self.send_requests('messages/document', data)
        return answer
    
    def finance(self, chatID):
        finance_string = "You are now subscribed to Finance updates. Please don't write Finance again, as it will subscribe you again\n*DAY 1:*\nFinancial Literacy: What it is and why is it needed?\nhttps://www.youtube.com/watch?v=4j2emMn7UaI"
        with open(f"Recurring/Finance/Day 1/numbers.txt", "a+") as outfile:
            # write the to_number in the outfile
            outfile.write(f"{chatID}\n")
        return self.send_message(chatID, finance_string)
    
    def quant(self, chatID):
        quant_string = "Quant Coming Soon"
        return self.send_message(chatID, quant_string)
    
    def software(self, chatID):
        software_string = "You are now subscribed to Software Development updates. Please don't write Software again, as it will subscribe you again\n*DAY 1:*\nIntro to HTML\nhttps://www.youtube.com/watch?v=UB1O30fR-EE&ab_channel=TraversyMedia"
        with open(f"Recurring/Software/Day 1/numbers.txt", "a+") as outfile:
            outfile.write(f"{chatID}\n")
        return self.send_message(chatID, software_string)
    
    def dsml(self, chatID):
        dsml_string = "You are now subscribed to Data Science / Machine Learning updates. Please don't write DS-ML again, as it will subscribe you again\n*DAY 1:*\nWhat is ML?\nhttps://www.youtube.com/watch?v=ukzFI9rgwfU\nWhat is DS?\nhttps://www.youtube.com/watch?v=X3paOmcrTjQ\nRevise the concepts of permutation, combination and probability taught for JEE Advance. You should be clear with the concepts of Mathematics I and Mathematics II (especially differential calculus and linear algebra) offered by IIT Kharagpur."
        with open(f"Recurring/DS-ML/Day 1/numbers.txt", "a+") as outfile:
            outfile.write(f"{chatID}\n")
        return self.send_message(chatID, dsml_string)
    
    def pm(self, chatID):
        pm_string = "You are now subscribed to Product Management updates. Please don't write PM again, as it will subscribe you again\n*DAY 1:*\nIntroduction to PM\nhttps://youtu.be/4yQtEx7-NQs"
        with open(f"Recurring/PM/Day 1/numbers.txt", "a+") as outfile:
            outfile.write(f"{chatID}\n")
        return self.send_message(chatID, pm_string)
    
    def consult(self, chatID):
        consult_string = "You are now subscribed to Consult updates. Please don't write Consult again, as it will subscribe you again\n*DAY 1:*\nIntroduction to Consultancy\nhttps://www.youtube.com/watch?v=-ZwQtICNbRc"
        with open(f"Recurring/Consult/Day 1/numbers.txt", "a+") as outfile:
            outfile.write(f"{chatID}\n")
        return self.send_message(chatID, consult_string)
    
    def help(self, chatID):
        help_string = "List of available commands:\n‣ *Life Fundae*: Gives you some basic fundae of life in KGP\n‣ *Finance*: Subscribes you to a 7 day mini course on finance.\n‣ *Quant*: Subscribes you to a 7 day mini course on Quantitative Finance.\n‣ *Software*: Subscribes you to a 7 day mini course on Software Development.\n‣ *DS-ML*: Subscribes you to a 7 day mini course on Data Science and Machine Learning.\n‣ *PM*: Subscribes you to a 7 day mini course on Product Management.\n‣ *Consult*: Subscribes you to a 7 day mini course on Consultancy.\n‣ *CDC Help*: Gives you information about CDC (Link to CDC Companion).\n‣ *Help*: Provides you with the list of commands this companion has and their explanations."
        return self.send_message(chatID, help_string)

    def Processingـincomingـmessages(self):
        if self.dict_messages != []:
            message = self.dict_messages
            text = message['body']
            if not message['fromMe']:
                chatID  = message['from'] 
                if text.lower() == 'hi':
                    return self.welcome(chatID)
                elif text.lower() == 'cdc help':
                    return self.cdc(chatID)
                elif text.lower() == 'life fundae':
                    return self.send_document(chatID, "Life Fundae.pdf", "https://drive.google.com/u/0/uc?id=1kBlD7nzxGPMzzHP90bFhnTmnKHmdVo5M&export=download")
                elif text.lower() == 'finance':
                    return self.finance(chatID)
                elif text.lower() == 'quant':
                    return self.quant(chatID)
                elif text.lower() == 'software':
                    return self.software(chatID)
                elif text.lower() == 'ds-ml':
                    return self.dsml(chatID)
                elif text.lower() == 'pm':
                    return self.pm(chatID)
                elif text.lower() == 'consult':
                    return self.consult(chatID)
                elif text.lower() == 'help':
                    return self.help(chatID)
                else:
                    return self.not_found(chatID)
            else: return 'NoCommand'