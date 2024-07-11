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
	# 获取某一条资料信息
	def related_one(self,modules,record_id:str):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.get(url, headers=headers)
		records = response.json()
		return records["data"]
	# 更新模块下记录的信息
	def update(self,modules,record_id:int,field3,field6,field8,field10,field12,field,field2,register,CustomerAddress,City,field9,field11,field4,field13):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		update_data = {
			"data": [
				{
					"id": record_id,#记录ID
					"field3":field3 ,  # 法定代表人
					"field6":field6,#经营范围
					"field8":field8,#电子邮件
					"field10":field10,#工商号码
					"field12":field12,#信用代码
					"field":field,#经营状态
					"field2":field2,#注册日期
					"register":register,#注册资本
					"CustomerAddress":CustomerAddress,#注册地址
					"City":City,#所在城市
					"field9":field9,#組織代碼
					"field11":field11,#登记机关
					"field4":field4,#营业期限
					"field13":field13,#核准日期
				}
			]
		}

		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.put(url, headers=headers,json=update_data)
		records = response.json()
		return records
	def update_one(self,modules,record_id:int,field18):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		update_data = {
			"data": [
				{
					"id": record_id,  # 记录ID
					"field18": field18,  # 单条记录填写
				}
			]
		}

		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.put(url, headers=headers, json=update_data)
		records = response.json()
		return records

	def update_Deal_Name_one(self,modules,record_id:int,Deal_Name):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		update_data = {
			"data": [
				{
					"id": record_id,  # 记录ID
					"Deal_Name": Deal_Name,  # 单条记录填写
				}
			]
		}

		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.put(url, headers=headers, json=update_data)
		records = response.json()
		return records

	def searchexist(self,workProject:str):
		try:
			self.search(workProject)
			return "exist"
		except:
			return "absent"
	# 搜索记录
	def search(self,workProject:str):
		url = f"https://www.zohoapis.com.cn/crm/v2/Job_Management/search?criteria=((Name:equals:{workProject}))"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.get(url, headers=headers)
		records = response.json()
		return records["data"]
	def personinfo(self,mail:str):
		url = f"https://www.zohoapis.com.cn/crm/v2/Staff/search?criteria=((Email:equals:{mail}))"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.get(url, headers=headers)
		records = response.json()
		Depinfo=  records["data"]
		for Dep in Depinfo:
			userDep = Dep["Dep"]
		return userDep
	def create(self,workName,user:str):
		if user == "ta@morglory.com.tw" or user == "administrator@morglory.com.tw":
			user = "ted_chou@morglory.com.tw"
		print(user)
		Dep = self.personinfo(user)
		print(Dep)
		url = "https://www.zohoapis.com.cn/crm/v2/Job_Management"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		create_data = {
			"data": [
				{
					"Name": workName,
					"field11": "優先順序：重要不緊急",
					"Stage": "執行",
					"field6": "G01-工作日誌",
					"Owner": {'email': user},
					"Limited": "時效掌握：如預期完成",
					"Dep": Dep
				}
			]
		}
		response = requests.post(url, headers=headers,json=create_data)
		records = response.json()
		return records["data"]
	# 创建一条任务信息
	def createone(self,workName,Date:str,What_ID:str,owner:str):
		if owner == "ta@morglory.com.tw":
			owner = "ted_chou@morglory.com.tw"
		url = "https://www.zohoapis.com.cn/crm/v2/Tasks"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		create_data = {
			"data": [
				{
					'Subject': workName,
					'Due_Date': Date,
					'Priority': '高',
					'$se_module': 'Deals',
					'What_Id': {'id': What_ID},
					'Owner': {'email': owner},
				}
			]
		}
		response = requests.post(url, headers=headers,json=create_data)
		records = response.json()
		return records["data"]
	# 更新任务信息
	def updatecreateone(self,workName,Date:str,What_ID:str,owner:str):
		if owner == "ta@morglory.com.tw":
			owner = "ted_chou@morglory.com.tw"
		url = "https://www.zohoapis.com.cn/crm/v2/Tasks"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		create_data = {
			"data": [
				{
					'Subject': workName,
					'Due_Date': Date,
					'Priority': '高',
					'$se_module': 'Deals',
					'What_Id': {'id': What_ID},
					'Owner': {'email': owner},
				}
			]
		}
		response = requests.put(url, headers=headers,json=create_data)
		records = response.json()
		return records["data"]
	# 搜索并返回ID
	def searchID(self,workProject:str):
		url = f"https://www.zohoapis.com.cn/crm/v2/Job_Management/search?criteria=((Name:equals:{workProject}))"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.get(url, headers=headers)
		records = response.json()
		infoid = records["data"]
		for i in infoid:
			id = i["id"]
		return id
	# 搜索任务
	def secrchTask(self,taskname):
		url = f"https://www.zohoapis.com.cn/crm/v2/Tasks/search?criteria=((Subject:equals:{taskname}))"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.get(url, headers=headers)
		records = response.json()
		return records["data"]
	# 判断任务是否存在
	def searchexistTask(self,taskname:str):
		try:
			self.secrchTask(taskname)
			return "exist"
		except:
			return "absent"


	def update_one_name(self,modules,record_id:int,Deal_Name,describe):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		if describe==None  and describe== "null" and describe == "":
			update_data = {
				"data": [
					{
						"id": record_id,  # 记录ID
						"Deal_Name": Deal_Name,  # 案件名称
					}
				]
			}
		else:
			update_data = {
				"data": [
					{
						"id": record_id,  # 记录ID
						"Deal_Name": Deal_Name,  # 案件名称
						"describe": describe  # 案件描述
					}
				]
			}
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.put(url, headers=headers, json=update_data)
		records = response.json()
		return records


	def note(self,modules,record_id:int,Note_Content):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}/Notes"
		update_data = {
			"data": [
				{
					"Note_Title": Note_Content,
					"Note_Content": Note_Content
				}
			]
		}

		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.post(url, headers=headers, json=update_data)
		records = response.json()
		return records
	#创建共有专案
	def create_Project_Management(self,workName,count,user:str):
		if user == "ta@morglory.com.tw" or user == "administrator@morglory.com.tw":
			user = "ted_chou@morglory.com.tw"
		Dep = self.personinfo(user)
		url = "https://www.zohoapis.com.cn/crm/v2/Project_Management"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		create_data = {
			"data": [
				{
					"Name": workName,
					"field12": "優先順序：重要不緊急",
					"field9": "時效掌握：如預期完成",
					"field13": "專案進度    ：      00 - 49%",
					"Owner": {'email': user},
					"field3": count,
					"Dep": Dep
				}
			]
		}
		response = requests.post(url, headers=headers,json=create_data)
		records = response.json()
		return records["data"]



	def update_Project_Management(self,modules,record_id:int,Name,describe,start,end):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		if start == None or start =="":
			update_data = {
				"data": [
					{
						"id": record_id,  # 记录ID
						"Name": Name,  # 专案名称
						"field3": describe, #专案说明
						"field5":start,
						"field6":end
					}
				]
			}
		else:
			update_data = {
				"data": [
					{
						"id": record_id,  # 记录ID
						"Name": Name,  # 专案名称
						"field3": describe,  # 专案说明
						"field5": f"{start}+08:00",
						"field6": f"{end}+08:00"
					}
				]
			}
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.put(url, headers=headers, json=update_data)
		records = response.json()
		return records

	def close_update_Project_Management(self,modules,record_id:int,Name):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		newname = Name + "(已結案)"
		update_data = {
			"data": [
				{
					"id": record_id,  # 记录ID
					"Name": newname,  # 专案名称
				}
			]
		}

		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.put(url, headers=headers, json=update_data)
		records = response.json()
		return records


	def close_Project_Management(self,modules,record_id):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		update_data = {
			"data": [
				{
					"id": record_id,  # 记录ID
					"field13": "專案進度    ：     結案歸檔",

				}
			]
		}

		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.put(url, headers=headers, json=update_data)
		records = response.json()
		return records
# 	创建共有工作关联共有工作
	def create_Job_Management(self,workName,count,user:str,relationship,starttime,endtime):
		if user == "ta@morglory.com.tw" or user == "administrator@morglory.com.tw":
			user = "ted_chou@morglory.com.tw"
		Dep = self.personinfo(user)
		url = "https://www.zohoapis.com.cn/crm/v2/Job_Management"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		if count == None and count == "null" and count == "":
			create_data = {
				"data": [
					{
						"Name": workName,
						"field11": "優先順序：重要不緊急",
						"Limited": "時效掌握：如預期完成",
						"Stage": "執行",
						"field6": "G01-工作日誌",
						"Owner": {'email': user},
						"field": {'id': relationship},
						"Dep": Dep,
						"field4":f"{starttime}+08:00",
						"field5":f"{endtime}+08:00"
					}
				]
			}
		else:
			create_data = {
				"data": [
					{
						"Name": workName,
						"field11": "優先順序：重要不緊急",
						"Limited": "時效掌握：如預期完成",
						"Stage": "執行",
						"field6": "G01-工作日誌",
						"Owner": {'email': user},
						"field8": count,
						"field": {'id': relationship},
						"Dep": Dep,
						"field4": f"{starttime}+08:00",
						"field5": f"{endtime}+08:00"
					}
				]
			}
		response = requests.post(url, headers=headers,json=create_data)
		records = response.json()
		return records["data"]
	# 创建共有工作，与引合案件关联
	def Deal_create_Job_Management(self,workName,count,user:str,relationship,starttime,endtime):
		if user == "ta@morglory.com.tw" or user == "administrator@morglory.com.tw":
			user = "ted_chou@morglory.com.tw"
		Dep = self.personinfo(user)
		url = "https://www.zohoapis.com.cn/crm/v2/Job_Management"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		if count == None and count == "null" and count == "":
			create_data = {
				"data": [
					{
						"Name": workName,
						"field11": "優先順序：重要不緊急",
						"Limited": "時效掌握：如預期完成",
						"Stage": "執行",
						"field6": "G01-工作日誌",
						"Owner": {'email': user},
						"field2": {'id': relationship},
						"Dep": Dep,
						"field4": f"{starttime}+08:00",
						"field5": f"{endtime}+08:00"
					}
				]
			}
		else:
			create_data = {
				"data": [
					{
						"Name": workName,
						"field11": "優先順序：重要不緊急",
						"Limited": "時效掌握：如預期完成",
						"Stage": "執行",
						"field6": "G01-工作日誌",
						"Owner": {'email': user},
						"field8": count,
						"field2": {'id': relationship},
						"Dep": Dep,
						"field4": f"{starttime}+08:00",
						"field5": f"{endtime}+08:00"
					}
				]
			}
		response = requests.post(url, headers=headers,json=create_data)
		records = response.json()
		return records["data"]
	def create_Job_Management_one(self,workName,count,user:str,starttime,endtime):
		if user == "ta@morglory.com.tw" or user == "administrator@morglory.com.tw":
			user = "ted_chou@morglory.com.tw"
		Dep = self.personinfo(user)
		url = "https://www.zohoapis.com.cn/crm/v2/Job_Management"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		if count == None  and count == "null" and count == "":
			create_data = {
				"data": [
					{
						"Name": workName,
						"field11": "優先順序：重要不緊急",
						"Limited": "時效掌握：如預期完成",
						"Stage": "執行",
						"field6": "G01-工作日誌",
						"Owner": {'email': user},
						"Dep": Dep,
						"field4": f"{starttime}+08:00",
						"field5": f"{endtime}+08:00"
					}
				]
			}
		else:
			create_data = {
				"data": [
					{
						"Name": workName,
						"field11": "優先順序：重要不緊急",
						"Limited": "時效掌握：如預期完成",
						"Stage": "執行",
						"field6": "G01-工作日誌",
						"Owner": {'email': user},
						"field8": count,
						"Dep": Dep,
						"field4": f"{starttime}+08:00",
						"field5": f"{endtime}+08:00"
					}
				]
			}
		response = requests.post(url, headers=headers,json=create_data)
		records = response.json()
		return records["data"]


	def update_Job_Management(self,modules,record_id:int,Name,describe,starttime,endtime):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		if describe == None and describe == "null" and describe == "":
			update_data = {
				"data": [
					{
						"id": record_id,  # 记录ID
						"Name": Name,  # 工作名称
						"Stage": "執行",
						"field4": f"{starttime}+08:00",
						"field5": f"{endtime}+08:00"
					}
				]
			}
		else:
			update_data = {
				"data": [
					{
						"id": record_id,  # 记录ID
						"Name": Name,  # 工作名称
						"Stage": "執行",
						"field8": describe,  # 工作内容
						"field4": f"{starttime}+08:00",
						"field5": f"{endtime}+08:00"
					}
				]
			}
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.put(url, headers=headers, json=update_data)
		records = response.json()
		return records


	def update_status_Job_Management(self,modules,record_id):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		update_data = {
			"data": [
				{
					"id": record_id,  # 记录ID
					"Stage": "完成" #工作内容
				}
			]
		}

		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.put(url, headers=headers, json=update_data)
		records = response.json()
		return records


	def update_Job_Management_related(self,modules,record_id,related_list):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		update_data = {
			"data": [
				{
					"id": record_id,  # 记录ID
					"field": related_list #工作内容
				}
			]
		}

		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.put(url, headers=headers, json=update_data)
		records = response.json()
		return records
	# 创建会议
	def Eventscreateone(self,EventName,Content,What_ID:str,owner:str,Start_DateTime,End_DateTime):
		if owner == "ta@morglory.com.tw":
			owner = "ted_chou@morglory.com.tw"
		if Start_DateTime == None or End_DateTime == None:
			Start_DateTime = str(dt.datetime.now().date())+ "T08:30:00+08:00"
			End_DateTime = str(dt.datetime.now().date())+ "T17:30:00+08:00"
		url = "https://www.zohoapis.com.cn/crm/v2/Events"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		if Content == None and Content == "null" and Content == "":
			create_data = {
				"data": [
					{
						'Event_Title': EventName,
						'Owner': {'email': owner},
						'Start_DateTime':f"{Start_DateTime}+08:00",
						'End_DateTime':f"{End_DateTime}+08:00",
						'$se_module': 'Deals',
						'What_Id': {'id': What_ID},

					}
				]
			}
		else:
			create_data = {
				"data": [
					{
						'Event_Title': EventName,
						'Owner': {'email': owner},
						'Start_DateTime': f"{Start_DateTime}+08:00",
						'End_DateTime': f"{End_DateTime}+08:00",
						'Content': Content,
						'$se_module': 'Deals',
						'What_Id': {'id': What_ID},

					}
				]
			}
		response = requests.post(url, headers=headers,json=create_data)
		records = response.json()
		return records["data"]
	# 更新会议
	def Eventupdate_one(self,modules,record_id,EventName,Content,Start_DateTime,End_DateTime):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		if Content == None and Content == "null" and Content == "":
			update_data = {
				"data": [
					{
						"id": record_id,  # 记录ID
						'Event_Title': EventName,
						'Start_DateTime':f"{Start_DateTime}+08:00",
						'End_DateTime':f"{End_DateTime}+08:00"
					}
				]
			}
		else:
			update_data = {
				"data": [
					{
						"id": record_id,  # 记录ID
						'Event_Title': EventName,
						'Content': Content,
						'Start_DateTime': f"{Start_DateTime}+08:00",
						'End_DateTime': f"{End_DateTime}+08:00"
					}
				]
			}

		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.put(url, headers=headers, json=update_data)
		records = response.json()
		return records["data"]
	# 关闭会议
	def Event_close(self,modules,record_id):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		update_data = {
			"data": [
				{
					"id": record_id,  # 记录ID
					"field3": True,
				}
			]
		}

		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.put(url, headers=headers, json=update_data)
		records = response.json()
		return records["data"]
	def delerEntity(self,modules,record_id):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}/{record_id}"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.delete(url, headers=headers)
		records = response.json()
		return records

	def SelectModulesCvidtest(self,modules,cvid:int):
		url = f"https://www.zohoapis.com.cn/crm/v2/{modules}?&cvid={cvid}"
		headers = {
			"Authorization": f"Zoho-oauthtoken {zoho.access_token(self)}",
			"Content-Type": "application/json"
		}
		response = requests.get(url, headers=headers)
		# records = response.json()
		print(response)
		print(response.status_code)
		return response
if __name__ == "__main__":
	z = zohoselect()
	z.SelectModulesCvidtest("Deals",184223000010304099)

