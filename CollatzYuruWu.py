def collatz(num):
  
  if num % 2 == 0:
     num = num // 2
     print(num)
  elif num % 2 == 1:
     num = 3 * num + 1
     print(num)
  return num  
     
print("Enter number: ", end='')
number=input()
while True:
  try:
      number=int(number)
      number = collatz(number)
      if number == 1:
          break
  except ValueError:
      print('Oops, tried to type a non-integer value:(')
      break