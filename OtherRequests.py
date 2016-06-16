import sys, apiaai, json
import os.path
import Messages as MSG

CLIENT_ACCESS_TOKEN = ''

def QueryApiAI(TextQuery):
    ApiAIInterface = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    ApiAIRequest = ApiAIInterface.text_request()
    ApiAIRequest.lang = 'en'
    ApiAIRequest.query = TextQuery

    ApiAIResponse = ApiAIRequest.getresponse()

    JSONResponse = json.loads(ApiAIResponse.read().decode('utf-8'))

    MSG.ProcessMessage(j['result']['fulfillment']['speech'])
        
        
