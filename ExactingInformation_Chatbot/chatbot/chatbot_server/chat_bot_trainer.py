from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('S J',
	database_uri='sqlite:///db.sqlite3',
	storage_adapter='chatterbot.storage.SQLStorageAdapter'
)

trainner = ChatterBotCorpusTrainer(chatbot)

trainner.train(
	'chatterbot.corpus.english'

)