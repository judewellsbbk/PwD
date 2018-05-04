import random as rand
import math
import time

n1k_list = []
rand.seed(1)
n1k_list.append(rand.randint(0,10))
for n in range(999):
    rand.seed(1)
    n1k_list.append(n1k_list[-1]+rand.randint(0,10))

n2k_list = []
rand.seed(1)
n2k_list.append(rand.randint(0,10))
for n in range(1999):
    rand.seed(1)
    n2k_list.append(n2k_list[-1]+rand.randint(0,10))

n4k_list = []
rand.seed(1)
n4k_list.append(rand.randint(0,10))
for n in range(3999):
    n4k_list.append(n4k_list[-1]+rand.randint(0,10))

n8k_list = []
n8k_list.append(rand.randint(0,10))
rand.seed(1)
for n in range(7999):
    n8k_list.append(n8k_list[-1]+rand.randint(0,10))

n1k_keys = []
rand.seed(1)
range1k = int(round(2 * math.log(1000, 2), 0))
print(range1k)
for k in range (range1k):
    n1k_keys.append(n1k_list[rand.randint(0,1000)])

n2k_keys = []
rand.seed(1)
range2k = int(round(2 * math.log(2000, 2), 0))
print(range2k)
for k in range (range2k):
    n2k_keys.append(n2k_list[rand.randint(0,1000)])

n4k_keys = []
range4k = int(round(2 * math.log(4000, 2), 0))
print(range4k)
for k in range (range4k):
    n4k_keys.append(n4k_list[rand.randint(0,1000)])

n8k_keys = []
range8k = int(round(2 * math.log(4000, 2), 0))
print(range8k)
for k in range (range8k):
    n8k_keys.append(n8k_list[rand.randint(0,1000)])

print(n8k_keys)

print(n1k_keys)
print(n2k_keys)

print(len(n1k_list))
print(len(n2k_list))
print(len(n4k_list))
print(len(n8k_list))




def binarySearch(listy, target):
	first = 0
	last = len(listy)-1
	found = False

	while first <= last and not found:
		midpoint = (first + last) // 2
		if listy[midpoint] == target:
			found = True
		else:
			if target < listy[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1
	return found


times = []
thousand_times = []
for i in range(1000):
    start = time.time()
    for key in n1k_keys:
        binarySearch(n1k_list, key)
    times.append((time.time() - start))
thousand_times.append(sum(times))

times = []
for i in range(1000):
    start = time.time()
    for key in n2k_keys:
        binarySearch(n2k_list, key)
    times.append((time.time() - start))
thousand_times.append(sum(times))

times = []
for i in range(1000):
    start = time.time()
    for key in n4k_keys:
        binarySearch(n4k_list, key)
    times.append((time.time() - start))
thousand_times.append(sum(times))

times = []
for i in range(1000):
    start = time.time()
    for key in n8k_keys:
        binarySearch(n8k_list, key)
    times.append((time.time() - start))
thousand_times.append(sum(times))

values = thousand_times

print(values)

from matplotlib import pyplot as plt

plt.plot(values, color='green', marker='o', linestyle='solid')

plt.title("Visualization of my list")

plt.xlabel('position')
plt.ylabel('value')

plt.show()