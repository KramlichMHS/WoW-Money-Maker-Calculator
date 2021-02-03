# WoW Money Maker Calculator

**What is this?**
This program is a calculator that helps WoW AH scrubs make money.

## How to Use It 
This program has 2 main features:

1. **Enter any vaild number choice other than 0:** This option lets you choose one of the listed craftable items and run a profit simulation. This simulation will *output cost to make*, *minimum sell AH sell price for a profit*, and *current profitability of the choosen item* along with Rob's Rating (see further down). This feature will give you two options [1] Auto or [2] Manual.
    - *Auto* - This option will take the most recent AH scan from Sargeras-US (Option for all servers coming soon!) and calculate all of the values based on the current price of mats on AH and the current price of the crafted item.
    - *Manual* - This option will do the same as auto, but this option does not take current AH data. For this option, you are required to enter the current prices of each non-vendor mat along with the current price of the crafted item.
    - *FYI* - The auto option has its data updated only once per hour. This option is good for running quick sims to get and idea of the market price. The manual option is good for finding current profitability of items based on their current prices if you have access to them.
2. **Enter 0:** This option will run an automatic simulation that will calculate profitability of all items stored in the program. The output will be arranged by Rob's Rating with the highest at the top. This option is great for getting an idea of what items are currently profitable based on current market prices.

## Outputs
**Current Cost to Make Item:** This number is calculated by taking the prices of mats and multiplying them by the number required for the crafted item. Vendor mats are included in this calculation. All mats are pulled from base mats if applicable. For example, Tome of the Still Mind uses Death Blossom for its calculations and assumes that the user will craft their own inks.

**Minimum Sell Price for Profit:** This number is the minimum listing price for the item on the AH in order to make your money back. This value includes the 5% AH cut.

**Profit per Item:** This number is ca by taking the minimum sell price and subtracting it from the current sell price for the item.

**Profitability Percentage:** This is the percentage of profit or loss of the current item. This value is based off of the profit per item.

**Rob's Rating:** This is a custom rating forumla that ranks items based on their current *profitability*, *total time to craft item*, and *velocity* (How quickly or well the item sells)(This number is set Rob with a default value of 5)(Number can range from 1-10)
*Formula:* Profit / (Time to Craft / 2) * Velocity

**Have fun and make some money noob$!**