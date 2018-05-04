def fib(n):
	if n == 0:
		return([0])
	elif n ==1:
		return([0,1])
	elif n == 2:
		return([0,1,1])
	else:
		return(fib(n-1) + fib(n-2))


def proba_two_sisters(k):
    offspring = fib(k)


def rand_kid():
	return random.choice(["boy", "girl"])

