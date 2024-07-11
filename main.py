from zoho_select import zohoselect
import time
z = zohoselect()
result = z.SelectModulesCvid("Deals",184223000010304099)
for i in result:
    print(i)
