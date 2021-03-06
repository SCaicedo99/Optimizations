import datetime


def recMC(coinValueList, change):  # Brute Forcing, Recursevely
   minCoins = change
   if change in coinValueList: # Checks to see if the change is in the array of coins, if it is, then returns 1
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:  # TODO Gotta know how this for loop works
         print(i)
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

print(datetime.datetime.now())
print(recMC([1,5,10,25],25))
print(datetime.datetime.now())

def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

print(recDC([1,5,10,25],63,[0]*64))
print(datetime.datetime.now())