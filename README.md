# Zoho-CRM-API
#### 这是一个使用Python开发的对Zoho CRM 进行操作的API的简单封装
####需要的第三方库
requests

您需要更改以下文件内容：
##### 请更改refresh.txt文件

文件内容如下：<br>
client_id=1000.K2GGB45DM6GMVEE240J<br>
client_secret=1daa388f9ebe5c327394d93816a3e48f7<br>
refresh_token=1000.33bf23421520dcd81761c5f3.ddbca0c74b7e86ff451e283490a0fbd6<br>
请修改等号后面的，client_id、client_secret、和refresh_token，修改为自己的即可，
##### 使用


```python
from zoho_select import zohoselect
z = zohoselect()
result = z.SelectModulesCvid("Deals",184223000010304099)
for i in result:
    print(i)
```
以上是简单的示例，SelectModulesCvid有两个参数，第一个是模块API名称，第二个是页面的ＩＤ<br>
如以上填写正确，运行则可以获取２００条资料<br>
zoho_select.py里面封装这部分对模块资料的增删改查，
因模块名称以及API名称不尽相同，故需要按照我写的进行更改即可，<br>
需要注意请求方式以及路径和字段ＡＰＩ名称。<br>
参考官网文档：https://www.zoho.com.cn/crm/help/api/v2/
#### 获取client_id以及client_secret
进入页面：https://api-console.zoho.com.cn/ 创建一个应用，会给你client_id以及client_secret<br>
#### 获取refresh_token
第一步：填写client_id和回调的URL地址。access_type=offline说明需要刷新令牌<br>
scope说明权限<br>
redirect_uri:回调地址<br>
```
https://accounts.zoho.com.cn/oauth/v2/auth?scope=ZohoCRM.modules.ALL,ZohoCRM.settings.ALL&client_id=
XXXXXXXXXXXXXXXXXXXXXXXX&response_type=code&access_type=offline&redirect_uri=http://www.baidu.com
```
第二步：<br>

将上一不重定向获取的code填入地址，并替换相应信息，即可，<br>

```
https://accounts.zoho.com.cn/oauth/v2/token?code=XXXXXXXXXXXXXXXXXXXX&client_id=XXXXXXXXXXXXXXXXXXXXX&client_secret=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX&redirect_uri=http://www.baidu.com&grant_type=authorization_code
```
## 技术一般，写的很烂
欢迎大家一起交流<br>
![411c6cbdb1a0410898c5ea0320ede6c](https://github.com/yigedaigua/Zoho-CRM-API/assets/52713163/03441e0f-9e7e-4d92-ab44-b3878fdade52)


