  # Author: Shawn Jin

import json

from typing import List
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class Chatbot:

    def __init__(self, adapters_file) -> None:
        # read adapters json file
        with open(adapters_file, 'r') as f:
            adapters = json.loads(f)
        # create a new chatbot
        self.chatbot = Chatbot('S Jin',
            logic_adapters  = adapters['logic_adapters'],
            storage_adapter = adapters['storage_adapter'])

    def answer(self, input_string:str) -> str:
        # let chatbot answer input
        response = self.chatbot.get_response(input_string)
        return response

    def train(self, training_data:List[str]):
        trainner = ListTrainer(self.chatbot)
        trainner.train(training_data)


    # Create a new instance of a ChatBot
    # bot = ChatBot(
    #     'Example Bot',
    #     storage_adapter='chatterbot.storage.SQLStorageAdapter',
    #     logic_adapters=[
    #         {
    #             'import_path': 'chatterbot.logic.BestMatch',
    #             'default_response': 'I am sorry, but I do not understand.',
    #             'maximum_similarity_threshold': 0.90
    #         },
    #         {
    #             'import_path': 'chatterbot.logic.SpecificResponseAdapter',
    #             'input_text': 'Help me!',
    #             'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
    #         },
    #         {
    #             'import_path': 'chatterbot.logic.SpecificResponseAdapter',
    #             'input_text': 'Where am i?',
    #             'output_text': 'You are in a magic world.'
    #         }

    #     ]
    # )

    # trainer = ListTrainer(bot)

    # # Train the chat bot with a few responses
    # trainer.train([
    #     'How can I help you?',
    #     'I want to create a chat bot',
    #     'Have you read the documentation?',
    #     'No, I have not',
    #     'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
    # ])
