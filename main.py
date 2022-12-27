def get_four_digit_numbers(max_digit):
  result = []
  for a in range(max_digit+1):
    for b in range(max_digit+1):
      for c in range(max_digit+1):
        for d in range(max_digit+1):
          if a + b + c + d == 21:
            result.append(str(a) + str(b) + str(c) + str(d))
  return result

maxDigit = input('Digite um número de 1 a 9: ')
result = get_four_digit_numbers(maxDigit)
print(result)
