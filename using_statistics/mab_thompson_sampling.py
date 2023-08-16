from numpy.random import beta

# The Thompson Sampling algorithm is a type MAB (Multi Armed Bandit)
# reinforcement learning algorithm. A MAB tries to solve a problem
# where you have multiple choices and have the goal to maximize
# your reward in a winning choice. It was created with the slot
# machine and nowdays we use it in many different ways.

# The idea is that once the option that wins the most is identified,
# you keep choosing this option until a better one shows up.

# Thompson Sampling is a MAB that utilizes Bayesian statistics
# in a combination of priori with Bernoulli's distribution and
# a posteriori with Beta(a, b)'s distribution. That way:
# a = number of cases that a reward was obtained (successes) + 1
# b = number of cases that no reward was obtained (failures) + 1

# Therefore, each option will have its own Beta distribution with
# their own a and b. From that, we calculate a sample of size 1
# from each distribution and the one that shows the highest result
# will be chosen.
# The options with a higher success rate will have a higher
# probability of having bigger samples, therefore, will be
# chosen the most.

# In the example below a news website has published a report
# but they do not know which title to use in order to get the most
# accesses to that report. They came up with 4 different titles, and
# we are going to use Thompson Sampling to decide which one is the best
# and show it to the majority of users.

# In the first moment, a and b are equal to 1 for all 4 titles
# a represents the quantity of successes
# b represents the quantity of failures

title_1_a = 0+1
title_1_b = 0+1

title_2_a = 0+1
title_2_b = 0+1

title_3_a = 0+1
title_3_b = 0+1

title_4_a = 0+1
title_4_b = 0+1

# Now we show the Betas of each title

t1 = beta(a=title_1_a, b=title_1_b, size=1)
t2 = beta(a=title_2_a, b=title_2_b, size=1)
t3 = beta(a=title_3_a, b=title_3_b, size=1)
t4 = beta(a=title_4_a, b=title_4_b, size=1)

# print('Result for title 1: {}'.format(t1))
# print('Result for title 2: {}'.format(t2))
# print('Result for title 3: {}'.format(t3))
# print('Result for title 4: {}'.format(t4))

# Each time we collect a sample, we are going to show the highest result
# and register if it was a success (clicked) or failure (not clicked).

# After an hour in the website:
# Title 1 - 1000 clicks and 5000 not clicks
# Title 2 - 987 clicks and 4763 not clicks
# Title 3 - 1563 clicks and 7580 not clicks
# Title 4 - 804 clicks and 4503 not clicks

# Let's see what is the results now

title_1_a = 1000+1
title_1_b = 5000+1

title_2_a = 987+1
title_2_b = 4763+1

title_3_a = 1563+1
title_3_b = 7580+1

title_4_a = 804+1
title_4_b = 4503+1

t1 = beta(a=title_1_a, b=title_1_b, size=1)
t2 = beta(a=title_2_a, b=title_2_b, size=1)
t3 = beta(a=title_3_a, b=title_3_b, size=1)
t4 = beta(a=title_4_a, b=title_4_b, size=1)

print('Result for title 1: {}'.format(t1))
print('Result for title 2: {}'.format(t2))
print('Result for title 3: {}'.format(t3))
print('Result for title 4: {}'.format(t4))

# In this example, the titles 2 and 3 are the best
# we need to keep showing theses two until the better one
# stands out.
