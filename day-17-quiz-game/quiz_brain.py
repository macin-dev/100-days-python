class QuestionBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """Retrieve the next question and ask the user for their answer."""
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(user_answer, question.answer)

    def still_has_question(self):
        """Return True if there are still questions left in the list, False otherwise."""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """Evaluate the user's answer against the correct answer and update score."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Wrong!")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.\n")