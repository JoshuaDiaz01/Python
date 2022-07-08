import random

answers = []

def bridge_keeper():

    questions = ['what is your favorite color?', 'what is the air velocity of an unladen swallow',
    'what is the capital of assyria?']
    
    correct_answer = "African or European?"

    print('stop \n Those who approach the bridge of death must answer')

    name = input('what is your name')# input allows for string to be sent to terminal
    quest = input('what is your quest')
    random_question = random.randint(0,len(questions)-1)
    third = input(f'{questions[random_question]}\n')

    #what is your favorite color
    if random_question == 0:
        #sees if color has been guessed already
        if third in answers:
            print('You have been casted into george \n')
            return True
        else:
            answers.append(third)
            print("Right. off you go \n")
        return True
        #what is velocity of swallow
    elif random_question == 1:
        

