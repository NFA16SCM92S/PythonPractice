from multiple_choice_question import Question

question_prompts = [
    "What color are apples? \n a. Red/Green \n b. Purple\n c. Orange\n\n",
    "What color are Bananas? \n a. Teal \n b. Magenta\n c. Yellow\n\n",
    "What color are Strawberries? \n a. Yellow \n b. Red\n c. Blue\n\n"
]
#list of questions/ array
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0 # increment when user's answer is correct
    for ques in questions:
        answer = input(ques.prompt)
        if answer == ques.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)