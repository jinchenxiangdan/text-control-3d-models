from django.http import JsonResponse, HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('SJ',
    database_uri='sqlite:///db.sqlite3',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            # 'maximum_similarity_threshold': 0.7
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'help me',
            'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'where am i',
            'output_text': 'You are in a virtual world.'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'help',
            'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'who is author',
            'output_text': 'shawn'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'who is your dad',
            'output_text': 'shawn'
        },
        {
            'import_path' : 'chatterbot.logic.MathematicalEvaluation'
        },
        {
            'import_path' : 'chatterbot.logic.TimeLogicAdapter'  
        }

    ]

)

trainner = ChatterBotCorpusTrainer(bot)

trainner.train(
    'chatterbot.corpus.english'

)

def get_res(request):
    if request.method == 'GET':
        data = bot.get_response(request.body['input'])
        return JsonResponse(data)
    return 400

def test(request):
    return HttpResponse('Test')

def get_res2(request):
    if request.method == 'GET':
        question = request.GET.get('input', default='Hi')
        print(f'question: {question}')
        data = bot.get_response(question)
        return HttpResponse(data)
    return 400
