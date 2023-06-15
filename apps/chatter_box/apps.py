from django.apps import AppConfig
from chatterbot import ChatBot

class ChatterBoxConfig(AppConfig):
    name = 'chatter_box'
    chatbot = ChatBot('Ares', trainer='chatterbot.trainers.ListTrainer')
    response = chatbot.get_response("Bot info.")
    print(response)
    
