from resources.agent import llm
from resources.helper import show_response
response = llm.invoke("tell me about devops in 1 sentence")
print(show_response(response))