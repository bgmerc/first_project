#number of digits before comma

number = float(input("Enter a number of your desired length:"))
number_storage = number
digit1 = 0
def new(number_storage):
    return number_storage // 10

while True:
    print(number_storage)
    if(number_storage >= 1):
          number_storage = new(number_storage)
          digit1 += 1
    else:
        break
print(digit1)
if (digit1 == 0):
    digit1 = 1
print("number of digits before comma: ", digit1)