'''
finding prime numbers
using erastothenes' sieve.

erastothenes' sieve is not a
particularly fast algorithm
for finding prime numbers,
but it is one of the simpler
ones (i know, i also wonder
what the more complicated
look like!)
'''
for p in range(2, 10):
  for q in range(2, p):
    if p % q == 0:
      print("{0} equals {1} * {0}/{1}".format(p, q))
      break
  else:
    print("{} is prime number".format(p))
