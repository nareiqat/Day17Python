class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("That's Wrong!")
        print(f"The correct answer is {question_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}")

    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        return False

    def next_questions(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)







