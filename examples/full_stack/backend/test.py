from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

import os

kwargs = {
    "model": "meta-llama/Llama-2-7b-hf",
    "temperature": 0,
    "max_tokens": 200,
    "model_kwargs": {},
}


if os.environ.get("OPENAI_API_BASE_URL"):
    kwargs["openai_api_base"] = "https://q91q37rzza.execute-api.us-east-1.amazonaws.com/inference/v1"

api_key = os.environ["OPENAI_API_KEY"]
kwargs["model_kwargs"]["top_p"] = 0.5

print(kwargs)
print(api_key)

chat = ChatOpenAI(**kwargs, api_key=api_key)

messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to French."
    ),
    HumanMessage(
        content="Translate this sentence from English to French. I love programming."
    ),
]

print(chat(messages))