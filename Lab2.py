import random as rand

rand.seed(109)

l = [1,2,3,4]

rand.shuffle(l)

print l

bingo = range(1,91)

#print bingo

sample = rand.sample(bingo, 3)

print sample


#print rand.randint(10,20)




'''
N=90

numbers = set()

def draw():
	select = 1 + int(rand.random()*90)
	if select not in numbers:
		numbers.add(select)
		return select
	else:
		return draw()



for i in range(N):
	print draw()



'''
'''
for i in range(5000):
	if rand.random() < 0.0001:
		print True

print numbers
print len(numbers)
'''
