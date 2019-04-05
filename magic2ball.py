import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'it is certain'
	elif answerNumber == 2:
		return 'yeet'

r = random.randint(1, 2)
fortune = getAnswer(r)
print(fortune)

print(getAnswer(random.randint(1, 2)))
