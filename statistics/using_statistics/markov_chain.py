import numpy as np

# A Markov chain is a model that explains a sequence
# of events where the next event depends only on
# the current occurrence, or current state. The same way
# the current state only depended of the last occurrence
# instead of the whole sequence of previous events occurred.
# In each move to a new state, there is a probability embed.

# Example: Every day you have to choose between two restaurants (A and B)
# to have lunch, using the following rule:

# If you ate at the restaurant A today, so tomorrow you have 85% chance of
# eating in the restaurant B.

# If you ate at restaurant B today, so tomorrow you have 73% chance of
# eating at restaurant A.

# Suppose that you know both restaurants menus for today and that there
# was 58% chance that you went to the restaurant A and 42% chance that
# you went to restaurant B, which is the probability you will go to
# resturant A tomorrow?

# probability (p) of going to A tomorrow given you went to B today
p_A_tomorrow_given_B_today = 0.73
p_B_tomorrow_given_B_today = 0.27

p_B_tomorrow_given_A_today = 0.85
p_A_tomorrow_given_A_today = 0.15

p_A = 0.58
p_B = 0.42

# Let's use the Bayes Theorem to calculate the probabilities of eating
# tomorrow at restaurants A and B

p_A_tomorrow = p_A*p_A_tomorrow_given_A_today + p_B*p_A_tomorrow_given_B_today
p_B_tomorrow = p_A*p_B_tomorrow_given_A_today + p_B*p_B_tomorrow_given_B_today

print('Probability of eating at restaurant A is {0:.2f}% and at restaurant B is {1:.2f}%'.format(
    p_A_tomorrow*100, p_B_tomorrow*100))

# The result shows that you are probably goint to restaurant B tomorrow.
# But what about in 10 days?

# We are going to represent the probabilities in a matrix
# [A_to_A, A_to_B]
# [B_to_A, B_to_B]

today = np.array([
    [0.15, 0.85],
    [0.73, 0.27]
])

# To calculate what this matrix will be in x days, we elevate
# the matrix to the power of x+1

# In this example we want to know what the matrix will be in
# 9 days from now, so we elevate it to the power of 10 (9+1)

nine_days_ahead = np.linalg.matrix_power(today, 10)

# Now let's define the prori again, as a matrix as well
# priori = [A B]

priori = np.array([[0.42], [0.58]])

# Now let's calculate the probability that, 10 days from now you
# go to restaurant A and B by multiplying the matrices

ten_days_ahead = np.matmul(nine_days_ahead, priori)
print('10 days from now you will have {0:.2f}% chance of eating at restaurant A and {1:.2f}% chance of eating at restaurant B'.format(
    ten_days_ahead[0][0]*100, ten_days_ahead[1][0]*100))
