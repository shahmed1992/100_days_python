class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.correct_answers = 0
    def next_question(self):

        ques_list = self.question_list
        temp = ques_list[self.question_number]
        self.question_number+=1
        user_input = input(f"Q.{self.question_number}: {temp.text} (True/False)?:")
        self.check_answer(user_input, temp.answer.lower())

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer:
            self.correct_answers += 1
            print("You got it right!!")
        else:
            print("You got it wrong!!")
        print(f"your Current Score is: {self.correct_answers}/{self.question_number} ")
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

