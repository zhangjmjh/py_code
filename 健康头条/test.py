



a = {
	"status": 0,
	"msg": 'null',
	"data": {
		"pageNum": 1,
		"pageSize": 10,
		"size": 10,
		"startRow": 1,
		"endRow": 10,
		"total": 19,
		"pages": 2,
		"list": [{
			"modifyItem": 4,
			"phoneNumber": "14560214831",
			"createTime": "2021-12-01 08:36:07",
			"id": 22201,
			"reviewer": "张建明",
			"userId": "hhid_A00032115",
			"content": "兼任中华医学会儿科心血管川崎病学组副组长",
			"reviewTime": "2021-12-01 08:36:09",
			"status": 1
		}, {
			"modifyItem": 1,
			"phoneNumber": "14560214831",
			"createTime": "2021-12-01 08:36:05",
			"id": 22199,
			"reviewer": "张建明",
			"userId": "hhid_A00032115",
			"content": "兼任中华医学会儿科心血管川崎病学组副组长",
			"reviewTime": "2021-12-01 08:36:07",
			"status": 1
		}]
	}
}

new_list = a["data"]["list"]
print(new_list)
for i in new_list:
	if i['modifyItem'] == 4:
		new_id = i["id"]
		print(new_id)




		# new_id = new_list["id"]
		# print(new_id)
