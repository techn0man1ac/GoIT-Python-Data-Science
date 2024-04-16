import random
from datetime import datetime

responce = ["Many doubts,", "So it will be,", "Ask later", "Yes", 
            "I can't answer now", "Chances are good", 
            "Ask the question more precisely", "Definitely", 
            "Now unknown,", "No doubts, many doubts,", 
            "Definitely yes", "Good chances", "Repeat the question," , 
            "Maybe", "Will come true,", "A bad outlook", 
            "The stars say no", "It should be so"]

random.seed = input("Ask your question: ") + str(datetime.now())
print(random.choice(responce))