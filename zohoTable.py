from zoho_select import zohoselect
def print_info(id,Stage,Day,toDay):
	pass


if __name__ == "__main__":
	Owner = dict()
	count = dict()
	# 所有记录的ID
	iid = []
	business_count = 0
	record = []
	z = zohoselect()
	Date = z.SelectModulesCvid("Deals", 184223000002493690)
	for i in Date:
		iid.append(i["id"])
		name = i["Owner"]["name"]
		if name in Owner:
			continue
		else:
			Owner[name] = 0
			count[name] = 0
	for i in iid:
		result = z.related("Deals",i, "Stage_History")
		print(result)
		record.append(result)
	for info in record:
		# print(info)
		if len(info) == 1 :
			Stage = info[0]["Stage"]
			if Stage != "00.潛在商機":
				recode_id = info[0]["Potential_Name"]["id"]
				result_recode = z.related_one("Deals", recode_id)
				recode_name = result_recode[0]["Owner"]["name"]
				Owner[recode_name] = Owner[recode_name] + 1
				count[recode_name] = count[recode_name] + 1
			else:
				recode_id = info[0]["Potential_Name"]["id"]
				result_recode = z.related_one("Deals", recode_id)
				recode_name = result_recode[0]["Owner"]["name"]
				count[recode_name] = count[recode_name] + 1
		else:
			recode_id = info[0]["Potential_Name"]["id"]
			result_recode = z.related_one("Deals", recode_id)
			recode_name = result_recode[0]["Owner"]["name"]
			Owner[recode_name] = Owner[recode_name] + 1
			count[recode_name] = count[recode_name] + 1
	print(f"引合案件轉換數量{Owner}")
	print(f"引合案件數量{count}")
	# for key in Owner:
	# 	for countkey in count:
	# 		if key == countkey:
	# 			print(f"{key} 的潛客案件轉換比例{round(Owner[key]/count[countkey],2) * 100}%")
		# for item in info:


		# 	print(result_recode)





# 	li = []
# 	iid = i["id"]
# 	print(f"这条记录ID为{iid}")
# 	result = z.related("Deals", iid, "Stage_History")
# 	for info in result:
# 		li.append(info["Stage"])
# 	if len(li) == 1:
# 		if "00.潛在商機" != li[0]:
# 			count = count + 1
# 		else:
# 			business_count = business_count + 1
# 	else:
# 		count = count + 1
# print(f"引合案件不在潜客件数{count}")
# print(f"引合案件潜客件数{business_count}")
