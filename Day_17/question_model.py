class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def print_question_data(self):
        print(f"Question: {self.text}")
        print(f"Answer: {self.answer}")