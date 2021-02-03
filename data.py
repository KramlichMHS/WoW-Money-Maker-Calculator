# Key - Name of the final product (Must match an item in sellers list)
# Value - [Name of mats to get on AH, 
#          id of respective mats,
#          number of ah mats to make item,
#          cost of vendor items, 
#          crafting time per item, 
#          velocity (made up number that represents how easily the item sells),
#          item id]
sellersData = {
  "Tome of the Still Mind": [["Death Blossom"], [169701], [21], 2.68, 8.5, 9, 173049],
  "Heavy Desolate Armor Kit": [["Heavy Desolate Leather"], [172096], [8], 36, 1.5, 4, 172347],
  "Embalmer's Oil": [["Death Blossom"], [169701], [2], 0.05, 2, 8, 171286],
  "Shadowcore Oil": [["Death Blossom"], [169701], [2], 0.05, 2, 9, 171285],
  "Spectral Flask of Power": [["Nightshade", "Rising Glory", "Marrowroot", "Widowbloom", "Vigil's Touch"], [171315, 168586, 168589, 168583, 170554], [3, 4, 4, 4, 4], 0.05, 2, 5, 171276],
  "Spectral Flask of Stamina": [["Nightshade", "Rising Glory", "Marrowroot"], [171315, 168586, 168589], [1, 3, 3], 0.05, 2, 5, 171278],
  "Umbrahide Leggings (190)" : [["Enchanted Heavy Callous Hide", "Heavy Callous Hide", "Heavy Desolate Leather", "Desolate Leather"], [172438, 172097, 172096, 172089], [5, 5, 15, 50], 96.0, 2, 3, 172318],
  "Umbrahide Leggings (235)" : [["Enchanted Heavy Callous Hide", "Heavy Callous Hide", "Heavy Desolate Leather", "Desolate Leather"], [172438, 172097, 172096, 172089], [20, 20, 50, 225], 400.0, 2, 3, 172318]
}

#List of all items that can be simulated
#, "Umbrahide Leggings (190)","Umbrahide Leggings (235)"
sellers = ["Tome of the Still Mind", "Heavy Desolate Armor Kit", "Spectral Flask of Power", "Spectral Flask of Stamina", "Embalmer's Oil", "Shadowcore Oil"]