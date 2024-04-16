import random
from datetime import datetime

def get_random_response():
    responses = [
        "Many doubts,", 
        "So it will be,", 
        "Ask later", 
        "Yes", 
        "I can't answer now", 
        "Chances are good", 
        "Ask the question more precisely", 
        "Definitely", 
        "Now unknown,", 
        "No doubts, many doubts,", 
        "Definitely yes", 
        "Good chances", 
        "Repeat the question,", 
        "Maybe", 
        "Will come true,", 
        "A bad outlook", 
        "The stars say no", 
        "It should be so"
    ]
    return random.choice(responses)

random.seed = input("Ask your question: ") + str(datetime.now())
print(get_random_response())