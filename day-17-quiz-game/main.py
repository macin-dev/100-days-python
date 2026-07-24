from question_model import Question
from data import question_data
from quiz_brain import QuestionBrain

question_bank = []

# Load questions from data.py into the question_bank list
for question in question_data:
    new_q = Question(question["text"], question["answer"])
    question_bank.append(new_q)

quiz = QuestionBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")