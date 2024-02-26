# get input change amount from customer
startAmount = input("Remainder: ")
startAmount = int(startAmount)

# method to determine the number of each coin dispensed in change
def makeChange(amount):
    total = amount
    coinsInChange = [["Quarter", 0], ["Dime", 0], ["Nickle", 0], ["Penny", 0]]
    while amount >= 25:
        coinsInChange[0][1] += 1
        amount = amount - 25
    while amount >= 10:
        coinsInChange[1][1] += 1
        amount -= 10
    while amount >= 5:
        coinsInChange[2][1] += 1
        amount -= 5
    while amount >= 1:
        coinsInChange[3][1] += 1
        amount -= 1
      
  # display change amount and nymber/type of coins in change  
  print("Your change is: " + str(total))

  print("Dispensed coins: ")
  for i in coinsInChange:
      print(i)

makeChange(startAmount)
