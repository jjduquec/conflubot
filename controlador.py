import random 

respuestas = [
    "Hi, how are you?",
    "Are you getting well?",
    "Could you just stop please?",
    "Im conflubot"


]

def get_answer():
    i=random.randint(0,3)
    return respuestas[i]