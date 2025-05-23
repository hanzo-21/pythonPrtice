# replace ___ with your code

# define a function to add 1 to the number
# represented by the digits list
def add_one(digits):
  
  # adding 1 to last digit and
  # getting carry
  # also replacing last digit with remainder
  digits[len(digits)-1] += 1
  carry = digits[len(digits)-1] // 10
  digits[len(digits)-1] = digits[len(digits)-1] % 10

  # continue adding carry to
  # each digit from second last element
  # to first element
  for n in range( len(digits)-2,-1,-1):
    if carry:
      digits[n] += 1
      carry = digits[n] // 10
      digits[n] = digits[n] % 10

  # even after adding all carry
  # if one carry is still remaining
  # we need to add that digit
  # at beginning
  if carry ==1:
    digits.insert(0,1)
  
  # return the final list
  return digits


digits = [9,9,9,9]
added_digits = add_one(digits)
print(added_digits)