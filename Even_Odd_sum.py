'''Q WAP to take an integer N and print the sum of all its even digits and sum of all its odd digits seperately?''' 

N = input()

odd_sum = 0
even_sum = 0

for i in N:
  digit = int(i)

  if digit % 2:
    odd_sum += digit
  else:
    even_sum += digit

print(even_sum , odd_sum)

