# Create a program capable of displaying questions to the user like KBC. 
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game. 


questions = [
    { 
        "level":1,
        "question": "What is the capital of India?",
        "options": 
        {
            "A": "Delhi",
            "B": "Mumbai",
            "C": "Kolkata",
            "D": "Chennai"
        },
        "Correct_answer": "A",
        "money": 1000
    },
    {    
        "level":2,
        "question": "Which planet is known as the Red Planet?",
        "options": {
            "A": "Earth",
            "B": "Mars",
            "C": "Jupiter",
            "D": "Venus"
        },
        "Correct_answer": "B",
        "money": 2000
    },
    {
        "level":3,
        "question": "Who wrote 'Ramayana'?",
        "options": {
            "A": "Valmiki",
            "B": "Tulsidas",
            "C": "Kalidasa",
            "D": "Ved Vyas"
        },
        "Correct_answer": "A",
        "money": 5000
    },
    {
        "level":4,
        "question": "Which is the largest ocean on Earth?",
        "options": {
            "A": "Atlantic Ocean",
            "B": "Indian Ocean",
            "C": "Pacific Ocean",
            "D": "Arctic Ocean"
        },
        "Correct_answer": "C",
        "money": 10000
    },
    {
        "level":5,
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon Dioxide",
            "D": "Hydrogen"
        },
        "Correct_answer": "C",
        "money": 20000
    },
    {
        "level":6,
        "question": "Who is known as the Father of Computers?",
        "options": {
            "A": "Charles Babbage",
            "B": "Alan Turing",
            "C": "Bill Gates",
            "D": "Steve Jobs"
        },
        "Correct_answer": "A",
        "money": 40000
    },
    {
        "level":7,
        "question": "What is H2O commonly known as?",
        "options": {
            "A": "Salt",
            "B": "Water",
            "C": "Oxygen",
            "D": "Hydrogen"
        },
        "Correct_answer": "B",
        "money": 80000
    },
    {
        "level":8,
        "question": "Which is the fastest land animal?",
        "options": {
            "A": "Lion",
            "B": "Cheetah",
            "C": "Horse",
            "D": "Tiger"
        },
        "Correct_answer": "B",
        "money": 160000
    },
    {
        "level":9,
        "question": "Which is the national currency of Japan?",
        "options": {
            "A": "Yuan",
            "B": "Won",
            "C": "Yen",
            "D": "Dollar"
        },
        "Correct_answer": "C",
        "money": 320000
    },
    {
        "level":10,
        "question": "Which programming language is used for AI/ML?",
        "options": {
            "A": "Python",
            "B": "C++",
            "C": "Java",
            "D": "PHP"
        },
        "Correct_answer": "A",
        "money": 640000
    },
    {
        "level":11,
        "question": "Which is the largest continent?",
        "options": {
            "A": "Africa",
            "B": "Asia",
            "C": "Europe",
            "D": "Australia"
        },
        "Correct_answer": "B",
        "money": 1250000
    },
    {
        "level":12,
        "question": "Who discovered Gravity?",
        "options": {
            "A": "Einstein",
            "B": "Newton",
            "C": "Galileo",
            "D": "Tesla"
        },
        "Correct_answer": "B",
        "money": 2500000
    },
    {
        "level":13,
        "question": "What is the square root of 144?",
        "options": {
            "A": "10",
            "B": "11",
            "C": "12",
            "D": "13"
        },
        "Correct_answer": "C",
        "money": 5000000
    },
    {
        "level":14,
        "question": "Which is the longest river in the world?",
        "options": {
            "A": "Amazon",
            "B": "Nile",
            "C": "Ganga",
            "D": "Yangtze"
        },
        "Correct_answer": "B",
        "money": 10000000
    },
    {
        "level":15,
        "question": "What is the national animal of India?",
        "options": {
            "A": "Elephant",
            "B": "Lion",
            "C": "Tiger",
            "D": "Leopard"
        },
        "Correct_answer": "C",
        "money": 70000000
    }
]
safe_points = {
    4: 10000,
    7: 80000,
    10: 640000,
    13: 5000000
}

 
def start():
    current_prize=0
    safe_money=0
    print("Game KBC Started")
    for question in questions:
     print(question["question"])
     for key,value in question["options"].items():
        print(f"{key}:-{value}")
     answer=input("Enter your Answer(in form a,b,c,d and 0 for quit)=").upper()
    
    # for quit 
     if answer == "0":
        print("quit from game")
        print("Safe Money which is you take for home=",current_prize)
        break
     if answer==question["Correct_answer"]:
        print("Your answer is correct")
        current_prize = question["money"]
        print(f"Your winning for Level {question['level']} is ₹{current_prize}")
        if question["level"] in safe_points:   
          safe_money = safe_points[question["level"]]
          print("Safe Money which is you take for home=",safe_money)
     else:
        print("wrong answer")
        print("Safe Money which is you take for home=",safe_money)
        break
    else:
       print("final money you take at home=",current_prize)


choice = input("Enter start to begin: ").lower()

if choice == "start":
    start()
else:
    print("Game not started")