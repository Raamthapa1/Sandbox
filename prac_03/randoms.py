import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# Answer Value between 5 and 20 (Inclusive)
# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest: 5, Largest:20

# What did you see on line 2?
# Answer: return a random number between 2 and 10, 10 is exclusive, step 2
# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest: 3, Largest:9
# Could line 2 have produced a 4?
# Answer: No because step 2 from 3
#
# What did you see on line 3?
# Answer: Random number between 2.5 and 5.5 inclusive
# What was the smallest number you could have seen, what was the largest?
# Answer: smallest: 2.5  Largest: 5.5
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
# Answer:
print(random.randint(1, 100))

for i in range(0, 100):
    print(random.randint(1, 100))
