# time_tick_quiz.py

import requests
import html
import random
import threading
import time

CATEGORY_URL = "https://opentdb.com/api_category.php"
QUESTION_URL = "https://opentdb.com/api.php"
TIME_LIMIT = 15  # seconds per question

# ------------------ api functionss ------------------

def fetch_categories():
    """
    fetches trivia categories from the API.
    """
    r=requests.get(CATEGORY_URL)
    if r.ok:
        list=r.json()["trivia_categories"]
        for k in range(len(list)):
            print(list[k])
    else:
        print("Error fetching questions")
        

def fetch_questions(amount=10):
    """
    fetches the questions based on given filters.
    """

    r= requests.get(QUESTION_URL,params={'amount':amount,'category': select_category(),'difficulty':select_difficulty(),'type':select_question_type()})
    if r.ok:
        return r.json()['results']
    else:
        print("Error fetching questions")
        
    

# ------------------ user input selection ------------------

def select_category():
    """
    prompts user to select a category from the list.
    """
    cate=input("Enter category id or press 'r' for random: ")
    if cate.lower()=='r':
        id =random.randint(9,32)
    else:
        id=int(cate)
    return id

def select_difficulty():
    """
    prompts user to select question difficulty.
    """
    dif=input("Select difficulty (easy/medium/hard) or press 'r' for random: ")
    if dif.lower()=='r':
        difficulties=['easy','medium','hard']
        difficulty=random.choice(difficulties)
    else:
        difficulty=dif.lower()
    return difficulty

def select_question_type():
    """
    prompts the user to select type of questions (multiple/boolean).
    """
    type = input("Select type of question (multiple or boolean) or press 'r' for random:")
    if type.lower()=='r':
        types=['multiple','boolean']
        qtype=random.choice(types)
    else:
        qtype=type.lower()
    return qtype
# ------------------ quiz logicc ------------------
answer=""
options=[]
res=""
c=0
def ask_question(questionlist):
    """
    presents a question to the user with a countdown timer.
    """
    for i in range(len(questionlist)):
        question=questionlist[i]
        print('\n'+html.unescape(question['question']))
        global answer,options,res
        answer=html.unescape(question['correct_answer'])
        options=question['incorrect_answers']+[answer]
        random.shuffle(options)
        for q in options:
            print(q)
        t1 = threading.Thread(target=timer)
        t2 = threading.Thread(target=select_quiz_options)
        t1.start()
        res=input("Enter your answer:\n")
        t1.join()
        if not res:
            print(f"The correct answer is: {answer}")
            continue
        t2.start()
        t2.join()


def timer():
    for j in range(TIME_LIMIT,0,-1):
        time.sleep(1)
    print("\nTime's up!")
    
    
def select_quiz_options():
    """
    gathers all the quiz options and fetch questions accordingly.

    """
    if res==answer:
        print("Correct answer!")
        global c
        c+=1
        print(f"Your current score is: {c}")
    elif res in options:
        print(f"Wrong answer! The correct answer is: {answer}")
        print(f"Your current score is: {c}")
    else:
        print(f"The correct answer is: {answer}")
        print(f"Your current score is: {c}")
        
    

# ------------------ main fucntion ------------------

def main():
    """
    Entry point for the TimeTickQuiz game.
    
    """
    fetch_categories()
    ask_question(fetch_questions())
    
    

if __name__ == "__main__":
    print("Welcome to TimeTickQuiz!")
    main()
    print("Your final score is:", c)
    print("Thank you for playing TimeTickQuiz!")
    