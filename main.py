from replit import clear
from data import sellers, sellersData
import requests, json, sys
from requests.auth import HTTPBasicAuth

# generates access token for session
def create_access_token(client_id, client_secret, region = 'us'):
    url = "https://%s.battle.net/oauth/token" % region
    body = {"grant_type": 'client_credentials'}
    auth = HTTPBasicAuth(client_id, client_secret)

    response = requests.post(url, data=body, auth=auth)
    return response.json()

r = create_access_token('1fe7ccb6066c428a8f98c8630f251afb', 'UsqVMIryU8OqtS2ItmHQv2HsjbIe4R0X')

# WoW AH Data in JSON format pulled hourly
url = "https://us.api.blizzard.com/data/wow/connected-realm/76/auctions?namespace=dynamic-us&locale=en_US&access_token=" + r['access_token']

#Runs a single simulation for selected item
#Parameters:
#item - string - item from sellers list used to choose a key from the sellers dict
#data - list - value of key that matches the item input
#auto - boolean - value based on wether info comes from user of from WoW AH API
def calcSeller(item, data, auto):
  clear()
  totalAhMats = 0
  for i in range(len(data[0])):
    if auto:
      price = getPriceAuto(data[1][i])
      print("Current price of " + data[0][i] + ": " + str(price))
    else:
      price = getPrice(data[0][i])
    totalCost = price * data[2][i]
    totalAhMats += totalCost
  costForSingleItem = totalAhMats + data[3]
  print("Cost for 1 " + item + ": " + str(round(costForSingleItem, 2)) + " gold")
  print("Minimum sell price for profit: " + str(round(ahCutReverse(costForSingleItem), 2)) + " gold")
  if auto:
    sellPriceItem = getPriceAuto(data[6])
    print("Current price of " + item + ": " + str(sellPriceItem))
  else:
    sellPriceItem = getPrice(item)
  profit = ahCut(sellPriceItem) - costForSingleItem
  print("Profit per item selling at " + str(round(sellPriceItem, 2)) + ": " + str(round(profit, 2)) + " gold per item\n")
  if not auto:
    numMake = int(input("How many " + item + "s do you want to make: "))
    print("\n***Stats per " + str(numMake) + " items***")
    for i in range(len(data[0])):
      print(data[0][i] + " needed: " + str(int(data[2][i] * numMake)))
    print("Crafting time: " + str(int((data[4] * numMake) // 60)) + " minutes and " + str(int((data[4] * numMake) % 60)) + " seconds")
    print("Crafting cost: " + str(round(costForSingleItem * numMake, 2)) + " gold")
    print("Profit: " + str(round(profit * numMake, 2)) + " gold\n")
  percentProfit = round(profit / (costForSingleItem + profit) * 100, 1)
  if percentProfit >= 0:
    print("****************\n**" + str(percentProfit) + "% Profit**\n****************")
  else:
    print("****************\n**" + str(abs(percentProfit)) + "% Loss**\n****************")
  rating = round(profit / (data[4] / 2) * data[5], 2)
  if data[5] > 0:
    print("\nRob's Rating: " + str(rating))
  return [item, percentProfit, data[4], rating]

#Based on calcSeller but with all print statements removed. Used for running sims of all items in sellers
#Parameters:
#item - string - item from sellers list used to choose a key from the sellers dict
#data - list - value of key that matches the item input
#auto - boolean - value based on wether info comes from user of from WoW AH API
def runAll(item, data, auto):
  totalAhMats = 0
  for i in range(len(data[0])):
    if auto:
      price = getPriceAuto(data[1][i])
    else:
      price = getPrice(data[0][i])
    totalCost = price * data[2][i]
    totalAhMats += totalCost
  costForSingleItem = totalAhMats + data[3]
  if auto:
    sellPriceItem = getPriceAuto(data[6])
  else:
    sellPriceItem = getPrice(item)
  profit = ahCut(sellPriceItem) - costForSingleItem
  percentProfit = round(profit / (costForSingleItem + profit) * 100, 1)
  rating = round(profit / (data[4] / 2) * data[5], 2)
  return [item, percentProfit, data[4], rating]

def pickOne():
  for i, item in enumerate(sellers):
    print("[" + str(i + 1) + "] " + item)
  return int(input("[0] Auto Run All\nChoose what you would like to do: "))

def getPrice(name):
  return float(input("Enter the current price of " + name + ": "))

def getPriceAuto(id):
  curr = -1
  min = -1
  for i in range(len(itemsAll["auctions"])):
    if itemsAll["auctions"][i]["item"]["id"] == id:
      curr = itemsAll["auctions"][i]["unit_price"]
      if min == -1:
        min = curr
      if curr < min:
        min = curr
  return convertGold(min)

def ahCutReverse(price):
  return price / .95

def ahCut(price):
  price -= price * 0.05
  return price

def convertGold(raw):
  gold = raw / 10000
  return gold



try:
  res = requests.get(url)
  itemsAll = json.loads(res.text)
except:
  print("Error getting WoW AH data")
  sys.exit()

while True:
  clear()
  choice = pickOne()
  if choice ==  0:
    clear()
    tempList = []
    count = 1
    for item in sellers:
      output = runAll(item, sellersData[item], True)
      tempList.append(output)
    while len(tempList) > 0:
      high = 0
      index = 0
      for i, info in enumerate(tempList):
        if info[3] > high:
          high = info[3]
          index = i
      print("#" + str(count) + " " +tempList[index][0] + "\nPercent Profit: " + str(tempList[index][1]) + "%\nTotal Crafting Time: " + str(tempList[index][2]) + "\nRob's Rating: " + str(tempList[index][3]) + "\n")
      tempList.pop(index)
      count += 1
    input("Press 'Enter' to go back to the main menu")
    continue
  choice -= 1
  try:
    item = sellers[choice]
    autoOrManual = int(input("Would you like an automatic search or a manual search?\n[1] Auto\n[2] Manual\n"))
    if autoOrManual == 2:
      calcSeller(item, sellersData[item], False)
    else:
      calcSeller(item, sellersData[item], True)
  except ValueError:
    print("Invalid Choice!")
    continue
  again = int(input("\nRun another sim? \n[1] Yes\n[2] No\n"))
  if again == 0:
    break