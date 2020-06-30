import json

with open('replies.json') as f:
    replies = json.loads(f.read())

def chat(message):
    if message in replies:
        answer = replies[message]
    else:
        answer = "Sorry, I can't help you with that."
    return answer