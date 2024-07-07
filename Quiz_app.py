
# List of Indian questions with options and correct answer
questions = [
    {
        "question": "Who is known as the 'Father of the Indian Constitution'?",
        "options": ["A. Mahatma Gandhi", "B. B. R. Ambedkar", "C. Jawaharlal Nehru", "D. Sardar Patel"],
        "answer": "B"
    },
    {
        "question": "In which year did India win its first Cricket World Cup?",
        "options": ["A. 1975", "B. 1983", "C. 1987", "D. 1996"],
        "answer": "B"
    },
    {
        "question": "What is the capital city of the Indian state of Meghalaya?",
        "options": ["A. Imphal", "B. Itanagar", "C. Shillong", "D. Aizawl"],
        "answer": "C"
    },
    {
        "question": "Which Indian classical dance form originated in Kerala?",
        "options": ["A. Bharatnatyam", "B. Kathak", "C. Kathakali", "D. Odissi"],
        "answer": "C"
    },
    {
        "question": "Who was the first Indian woman to win a Nobel Prize?",
        "options": ["A. Indira Gandhi", "B. Sarojini Naidu", "C. Mother Teresa", "D. Amartya Sen"],
        "answer": "C"
    },
    {
        "question": "What is the national animal of India?",
        "options": ["A. Lion", "B. Bengal Tiger", "C. Elephant", "D. Peacock"],
        "answer": "B"
    },
    {
        "question": "Which Indian festival is also known as the 'Festival of Lights'?",
        "options": ["A. Holi", "B. Diwali", "C. Eid", "D. Navratri"],
        "answer": "B"
    },
    {
        "question": "In which year did India gain independence from British rule?",
        "options": ["A. 1945", "B. 1947", "C. 1950", "D. 1952"],
        "answer": "B"
    },
    {
        "question": "What is the currency of India?",
        "options": ["A. Dollar", "B. Euro", "C. Rupee", "D. Yen"],
        "answer": "C"
    },
    {
        "question": "Who wrote the Indian national anthem 'Jana Gana Mana'?",
        "options": ["A. Bankim Chandra Chatterjee", "B. Rabindranath Tagore", "C. Sarojini Naidu", "D. Lata Mangeshkar"],
        "answer": "B"
    },
    {
        "question": "Which city is known as the 'Silicon Valley of India'?",
        "options": ["A. Mumbai", "B. Hyderabad", "C. Bangalore", "D. Pune"],
        "answer": "C"
    },
    {
        "question": "Who was the first Prime Minister of India?",
        "options": ["A. Mahatma Gandhi", "B. Sardar Patel", "C. Lal Bahadur Shastri", "D. Jawaharlal Nehru"],
        "answer": "D"
    },
    {
        "question": "Which river is considered the holiest in India?",
        "options": ["A. Yamuna", "B. Ganges", "C. Godavari", "D. Narmada"],
        "answer": "B"
    },
    {
        "question": "Who is the author of the book 'The God of Small Things'?",
        "options": ["A. Jhumpa Lahiri", "B. Arundhati Roy", "C. Chetan Bhagat", "D. Vikram Seth"],
        "answer": "B"
    },
    {
        "question": "Which Mughal emperor built the Taj Mahal?",
        "options": ["A. Akbar", "B. Aurangzeb", "C. Shah Jahan", "D. Humayun"],
        "answer": "C"
    },
    {
        "question": "What is the national flower of India?",
        "options": ["A. Rose", "B. Lotus", "C. Marigold", "D. Sunflower"],
        "answer": "B"
    },
    {
        "question": "In which Indian state are the Ajanta Caves located?",
        "options": ["A. Rajasthan", "B. Gujarat", "C. Maharashtra", "D. Karnataka"],
        "answer": "C"
    },
    {
        "question": "Who was the first Indian to travel in space?",
        "options": ["A. Kalpana Chawla", "B. Sunita Williams", "C. Rakesh Sharma", "D. Vikram Sarabhai"],
        "answer": "C"
    },
    {
        "question": "Which Indian city is famous for its Marine Drive?",
        "options": ["A. Chennai", "B. Kolkata", "C. Mumbai", "D. Kochi"],
        "answer": "C"
    },
    {
        "question": "What is the traditional Indian system of medicine called?",
        "options": ["A. Unani", "B. Allopathy", "C. Ayurveda", "D. Homeopathy"],
        "answer": "C"
    }
]

def run_quiz(questions):
    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {q['answer']}.\n")
    
    print(f"Your final score is {score}/{len(questions)}")

# Run the quiz
run_quiz(questions)

