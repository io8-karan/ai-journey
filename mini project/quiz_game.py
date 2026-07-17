
questions = [
    {
        "question": "What is the Capital of India?",
        "A": "Delhi",
        "B": "Mumbai",
        "C": "Punjab",
        "D": "Chandigarh",
        "Correct_Answer": "A",
        "Prize": 1000
    },
    {
        "question": "What is the capital of Punjab?",
        "A": "Delhi",
        "B": "Mumbai",
        "C": "Patna",
        "D": "Chandigarh",
        "Correct_Answer": "D",
        "Prize": 1000
    },
    {
        "question": "What is the Capital of UP?",
        "A": "Lucknow",
        "B": "Mumbai",
        "C": "Punjab",
        "D": "Chandigarh",
        "Correct_Answer": "A",
        "Prize": 1000
    },
    {
        "question": "What is the Capital of Bihar?",
        "A": "Delhi",
        "B": "Mumbai",
        "C": "Patna",
        "D": "Chandigarh",
        "Correct_Answer": "C",
        "Prize": 1000
    }
]
Total_prize=0
print("🎮 Welcome to KBC Game!\n")

for q in questions:
    print(q["question"])
    print("A:", q["A"])
    print("B:", q["B"])
    print("C:", q["C"])
    print("D:", q["D"])
    answer=str(input("Enter Your Answer")).upper()

    if q["Correct_Answer"]==answer:
        print("correct Answer")
        Total_prize += q["Prize"]
        print("You Won=",Total_prize)

    else:
        print("Wrong Answer")
        print("You Loss ")
        break;

print("Total Winning Prize=",Total_prize)