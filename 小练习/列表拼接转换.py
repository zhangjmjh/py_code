ret = {"statusReview":1,"endDate":"2021-10-14","terms":"","videoType":-1,"pageSize":20,"category":-1,"pageNum":1,"startDate":"2019-09-12","status":-1}

new_res = "&".join(sorted([str(key)+"="+str(value) for key, value in ret.items()]))
print(new_res)

a = []
for key, value in ret.items():
    x = str(key) + "=" + str(value)
    a.append(x)

b = "&".join(sorted(a))
print(b)

