# Zoho-CRM-API
#### 这是一个使用Python开发的对Zoho CRM 进行操作的API的简单封装

您需要更改以下文件内容：

##### 请更改refresh.txt文件

文件内容如下：<br>
client_id=1000.K2GGB45DM6GMVEE240J<br>
client_secret=1daa388f9ebe5c327394d93816a3e48f7<br>
refresh_token=1000.33bf23421520dcd81761c5f3.ddbca0c74b7e86ff451e283490a0fbd6<br>
请修改等号后面的，client_id、client_secret、和refresh_token，修改为自己的即可，
##### 使用


from zoho_select import zohoselect
z = zohoselect()
result = z.SelectModulesCvid("Deals",184223000010304099)
for i in result:
    print(i)
