import random as rand
import time
start = time.time()


for i in range(5000):
	number = rand.random()
	if number < 0.0001:
		print number
		print True

print str(time.time() - start)