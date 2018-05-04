import random as rand
import time

N=10000


def main():
	"""Example of probabilities verification from J. Grus' Data Science from Scratch, p. 71.
	"""
	both_girls = 0
	older_girl = 0
	either_girl = 0

	rand.seed(0)

	for _ in range(N):
		older = new_baby()
		younger = new_baby()

		if older == "girl":
			older_girl += 1

		if older == "girl" and younger == "girl":
			both_girls += 1

		if older == "girl" or younger == "girl":
			either_girl += 1

	print 'both_girls=', both_girls
	print 'older_girl=', older_girl
	print 'either_girl=', either_girl

	print "Pr[Both | Older]= ", float(both_girls) / (1 + older_girl)

	print "Pr[Both | Either]= ", float(both_girls) / (1 + float(either_girl))

def new_baby():
	return rand.choice(["boy", "girl"])

main()

#the one plus is added because they's is a risk that the demoninator could be zero - it prevents the program from crashing