#MIni quiz app : 5 question with scoring
def quiz():
    questions = [
        ("Which planet is known as Red Planet?", "Mars"),
        ("Which planet we live on?", "Earth"),
        ("What is the capital of India?", "New Delhi"),
        ("How many days are there in a week?", "7"),
        ("How many hours are there in a day?", "24")
    ]
    
    score = 0
    
    for q, correct_answer in questions:
        user_answer = input(q + " ").strip().lower()     #.strip() is used to remove all leading and trailing whitespace characters(space,tabs newlines)from user answer
        
        if user_answer == str(correct_answer).lower():   #str() is used to converts correct_answer to string representation
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    
    print("\nFinal Score:", score, "/", len(questions))
quiz()
