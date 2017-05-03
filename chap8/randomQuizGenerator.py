#! python3

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# Generate 35 quiz files
for quizNum in range(1):


    # TODO: Create the quiz and answer key files
    with open("captialsquiz{0}.txt".format(quizNum+1), "w") as quizFile, open("captialsquiz_answers{0}".format(quizNum+1), "w") as answerKeyFile:

        # TODO: Write out the header for the quizNum
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((" "*20) + "State Capitals Quiz (Form {0})".format(quizNum + 1))
        quizFile.write("\n\n")

        # TODO: Shuffle the order of the states.
        states = list(capitals.keys())
        random.shuffle(states)

        # TODO: Loop through all 50 states, making a question for each
        for questionNum in range(50):
            correctAnswer = capitals[states[questionNum]]
            wrongAnswers = list(capitals.values())
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers, 3)
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)
            quizFile.write("{0} What is the capital of {1}?\n".format(questionNum + 1, states[questionNum]))
            for i in range(4):
                quizFile.write(" {0}. {1}\n".format("ABCD"[i], answerOptions[i]))

            answerKeyFile.write("{0}. {1}\n".format(questionNum +1, "ABCD"[answerOptions.index(correctAnswer)]))
