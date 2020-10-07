import logging

from pushbullet import Pushbullet
import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        body = req_body['message']['text']
        title = req_body['eventType']
        api_key = os.getenv('PUSHBULLET_API_KEY')
        pb = Pushbullet(api_key)
        push = pb.push_note(title, body)
        logging.info(push)
        return func.HttpResponse(status_code=200)
    except:
        return func.HttpResponse(status_code=400)
