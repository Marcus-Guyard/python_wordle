import random
import requests
import collections
from collections import Counter


class Answer:
    answer: str
    correct: bool

    def __init__(self, answer, correct):
        self.answer = answer
        self.correct = correct


class Question:
    id: int
    prompt: str
    times_asked: int
    times_correct: int
    answers: list[Answer]

    def __init__(self, id, prompt, times_asked, times_correct, answers):
        self.id = id
        self.prompt = prompt
        self.times_correct = times_correct
        self.times_asked = times_asked
        self.answers = answers


class API:
    def get_questions(self) -> list[Question]:
        raise NotImplementedError

    def post_answer(self, question: Question, correct: bool):
        raise NotImplementedError


class User:
    def ask_question(self, question: Question) -> Answer:
        raise NotImplementedError


class ConsoleUser(User):
    def ask_question(self, question: Question) -> Answer:
        print(question.prompt)
        for i, ans in enumerate(question.answers):
            print(f"{i}: {ans.answer}")

        user_anser = int(input(">>"))
        return question.answers[user_anser]


class CheatingUser(User):

    def ask_question(self, question: Question) -> Answer:
        print(question.prompt)
        for i, ans in enumerate(question.answers):
            print(f"{i}: {ans.answer}")

        for i, ans in enumerate(question.answers):
            if ans.correct:
                print((f"Answering {i}"))
                return ans


class WebAPI(API):
    url: str

    def __init__(self, url):
        self.url = url

    def get_questions(self) -> list[Question]:
        questions = []
        for question in requests.get(self.url).json()["questions"]:
            _id = int(question["id"])
            prompt = question["prompt"]
            times_correct = int(question["times_correct"])
            times_asked = int(question["times_asked"])

            answers = []
            for answer in question["answers"]:
                ans = answer["answer"]
                correct = answer["correct"]
                answers.append(Answer(ans, correct))

            questions.append(Question(id, prompt, times_asked, times_correct, answers))
        return questions

    def post_answer(self, question: Question, correct: bool):
        print(f"Post answer{question.prompt}, correct {correct}")


class Quiz:
    api: API
    user: User
    max_num_question: int
    __questions: list[Question]

    def __init__(self, api, user, max_num_questions):
        self.api = api
        self.user = user
        self.__questions = random.sample(self.api.get_questions(), max_num_questions)

    def run(self):
        score = 0
        for question in self.__questions:
            ans = self.user.ask_question(question)
            if ans.correct:
                score += 1
                print("Correct!")
            else:
                print("Wrong")
            self.api.post_answer(question, ans.correct)

        print(f"You got a score of {score}")


if __name__ == '__main__':
    """api = WebAPI("https://bjornkjellgren.se/quiz/v2/questions")
    user = CheatingUser()
    quiz = Quiz(api, user, 5)
    quiz.run()
    print(api.get_questions()[0].prompt)"""

    # Lambda
    """d = [1,2,3,4,5,6,7,8,9]

    questions = requests.get("https://bjornkjellgren.se/quiz/v2/questions").json()["questions"]

    def min_key(q):
        return q["prompt"]
    print(sorted(questions, key=min_key))
    print(sorted(questions, key=lambda x: x["prompt"]))

    print(sorted(questions, key=lambda y: int(y["times_correct"]) / int(y["times_asked"]), reverse=True))

    for q in sorted(questions, key=lambda y:int(y["times_correct"]) / int(y["times_asked"])):
        print(int(q["times_correct"])/int(q["times_asked"]))"""

    # List comprehensions

    """a = [1,2,3,4,5,6,7,8,9,]

    new_list = []
    for e in a:
        new_list.append(e/2)

    print(new_list)
    print([e/2 for e in a])

    # samma sak fast endast med udda tal
    new_filtered_list = []
    for e in a:
        if e % 2:
            new_filtered_list.append(e/2)

    print(new_filtered_list)

    # samma sak fast med en list comprehension ist för en ifsats
    print([e/2 for e in a if e%2])


    print([(x, y) for x in [1,2,3] for y in [4,5,6] if x%2 if y%2 == 0])"""

    """
    # Counter

    c = Counter("gallad")
    print(c)
    c = Counter(["a", "b", "c"])
    print(c)
    e = Counter({"a": 1, "b": 2, "c": 3})
    print(e)
    d = Counter(cats=4, dogs=7)
    print(d)
    print(d["cats"])
    print(d["pet"])

    # c.elements
    print(list(d.elements()))

    # c.most_common
    print(c.most_common())
    """


    def removeDuplicates(nums: list[int]) -> int:
        x = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[x]:
                x += 1
                nums[x] = nums[i]
        return x + 1

    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))









