import azure.functions as func
import datetime
import json
import logging
from service.openai_service import get_response

app = func.FunctionApp()


@app.route(route="chat", auth_level=func.AuthLevel.ANONYMOUS)
def chat_completion(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    query = req.params.get('query')
    if not query:
       return func.HttpResponse("No query params provided.", status_code=400)

    if query:
        return func.HttpResponse(f"Hello, {query}. This HTTP triggered function executed successfully.")
    else:
        response = {
            "query": query,
            "model_response":"",
            "status":"completed"
        }

        return func.HttpResponse(
            body=json.dumps(response),
             status_code=200
        )