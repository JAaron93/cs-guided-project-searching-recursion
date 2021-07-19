'''
For a given positive integer n determine if it can be represented as a sum of two Fibonacci numbers (possibly equal).

Example

For n = 1, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 1 = 0 + 1 = F0 + F1.

For n = 11, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 11 = 3 + 8 = F4 + F6.

For n = 60, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 60 = 5 + 55 = F5 + F10.

For n = 66, the output should be
fibonacciSimpleSum2(n) = false.
'''


def fibonacciSimpleSum2(n):
      sequence = [0, 1]

  # For loop for creating fibo sequence
  for f in range(2, n + 1):
      next_number = sequence[-1] + sequence[-2]
      if next_number > n:
          break
      sequence.append(next_number)
      
  # Using while loop to iterate through all elements of our list 
  counter = 0
  while counter < len(sequence):
      sum_of_two = n - sequence[counter]
      # Is an integer that is the sum of two fibonacci numbers in the sequence?
      if sum_of_two in sequence:
          return True
      # If not, go up to the next element within our list
      else: 
          counter += 1
  return False
