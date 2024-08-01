from zohotoken import zoho
import requests
import datetime as dt
class zohoselect(zoho):
	# 获取模块的所有信息
	def SelectModules(self,modules):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.get(url, headers=headers)
		records = response.json()
		return records["data"]
	# 获取指定模块下的视图信息
	def SelectModulesCvid(self,modules,cvid:int):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}?&cvid={cvid}"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.get(url, headers=headers)
		records = response.json()
		# print(records)
		return records["data"]
	# 获取模块视图下的资料，超过200条使用
	def SelectModulesCvid_Page(self,modules,cvid:int,page:int,per_page:int):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}?&cvid={cvid}&page={page}&per_page={per_page}"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.get(url, headers=headers)
		records = response.json()
		return records["data"]
	# 获取相关列表的资料信息
	def related(self,modules,record_id:str,related_list_api_name:str):
		url = f"https://www.zohoapis.com.cn/crm/v2.1/{modules}/{record_id}/{related_list_api_name}"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.get(url, headers=headers)
		records = response.json()
		return records["data"]
	
if __name__ == "__main__":
	z = zohoselect()
	z.SelectModulesCvidtest("Deals",184223000010304099)

