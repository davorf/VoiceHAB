import sys, apiai, json
import os.path
import Settings
import Messages as MSG

def QueryApiAI(TextQuery):
    ApiAIInterface = apiai.ApiAI(Settings.ApiAIClientAccessToken)

    ApiAIRequest = ApiAIInterface.text_request()
    ApiAIRequest.lang = 'en'
    ApiAIRequest.query = TextQuery

    ApiAIResponse = ApiAIRequest.getresponse()

    JSONResponse = json.loads(ApiAIResponse.read().decode('utf-8'))

    MSG.ProcessMessage(JSONResponse['result']['fulfillment']['speech'])
        
        
