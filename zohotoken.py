import requests
import datetime
class zoho():
	def __init__(self):
		self.client_id = self.client()
		self.client_secret = self.secret()
		self.refresh_token = self.token()
	def client(self):
		with open("refresh.txt","r") as clientas :
			clienta = clientas.readlines()
			client_id = clienta[0].split("=")
			return client_id[1].strip()
	def secret(self):
		with open("refresh.txt","r") as secretfile:
			secretline = secretfile.readlines()
			client_secret = secretline[1].split("=")
			return client_secret[1].strip()
	def token(self):
		with open("refresh.txt","r") as t:
			ts = t.readlines()
			refresh_token = ts[2].split("=")
			return refresh_token[1].strip()
	def wirte_access_token(self):
		client_id = self.client_id
		client_secret = self.client_secret
		refresh_token = self.refresh_token
		# 构建请求
		url = "https://accounts.zoho.com.cn/oauth/v2/token"
		payload = {
			"grant_type": "refresh_token",
			"client_id": client_id,
			"client_secret": client_secret,
			"refresh_token": refresh_token
		}
		# 发送请求
		response = requests.post(url, data=payload)
		# 解析响应
		if response.status_code == 200:
			access_token = response.json()["access_token"]
			with open("access_token_file", "w") as f:
				current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				f.write(str(access_token) + "=" + str(current_time))
			f.close()
			return access_token
	def access_token(self):
		with open("access_token_file","r") as f:
			access = f.readline().split("=")
			# 文件中的日期
			olddatetime = access[1]
			# 对文件中的日期进行类型转换
			olddatetime_date = datetime.datetime.strptime(olddatetime,"%Y-%m-%d %H:%M:%S")
			# 现在的时间日期
			now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			# 转换现在日期的时间格式
			now_time_datatime = datetime.datetime.strptime(now_time,"%Y-%m-%d %H:%M:%S")
			# 给文件中的日期加上3600秒，因为access_token的有效期是3600，以此时间来判断
			olddatetime_three_thousand = olddatetime_date + datetime.timedelta(seconds=3600)
			if olddatetime_three_thousand > now_time_datatime:
				f.close()
				return access[0]
			else:
				f.close()
				return self.wirte_access_token()

