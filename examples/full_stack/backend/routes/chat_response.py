import os
import traceback

from flask import Blueprint, jsonify, make_response, request
from models import APIKey
from paths import DB_DIRECTORY_OPEN_AI

from embedchain import App

chat_response_bp = Blueprint("chat_response", __name__)


# Chat Response for user query
@chat_response_bp.route("/api/get_answer", methods=["POST"])
def get_answer():
    try:
        data = request.get_json()
        query = data.get("query")
        embedding_model = data.get("embedding_model")
        app_type = data.get("app_type")

        # if embedding_model == "open_ai":
        os.chdir(DB_DIRECTORY_OPEN_AI)
            # api_key = APIKey.query.first().key
            # os.environ["OPENAI_API_KEY"] = api_key
            # if app_type == "app":
        chat_bot = App.from_config("/usr/src/app/backend/config.yaml")

        response = chat_bot.chat(query)
        return make_response(jsonify({"response": response}), 200)

    except Exception as e:
        print(traceback.format_exc())
        return make_response(jsonify({"error": str(e)}), 400)
