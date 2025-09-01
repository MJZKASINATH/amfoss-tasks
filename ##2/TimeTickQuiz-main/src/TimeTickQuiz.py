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
        for i in range(len(list)):
            print(list[i])
    else:
        print("Error fetching questions")
        

def fetch_questions(amount=10):
    """
    fetches the questions based on given filters.
    """

    r= requests.get(QUESTION_URL,params={'amount':amount})
    

# ------------------ user input selection ------------------

def select_category():
    """
    prompts user to select a category from the list.
    """
    fetch_categories()
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
    type = input("Select type of question (multiple/True or False) or press 'r' for random:")
    if type.lower()=='r':
        types=['multiple']
# ------------------ quiz logicc ------------------

def ask_question():
    """
    presents a question to the user with a countdown timer.
    """
    pass

def select_quiz_options(categories):
    """
    gathers all the quiz options and fetch questions accordingly.
    """
    pass

# ------------------ main fucntion ------------------

def main():
    """
    Entry point for the TimeTickQuiz game.
    
    """
    #print(fetch_categories()) #Initializing the game by fetching categories
    fetch_categories()
    pass

if __name__ == "__main__":
    main()
