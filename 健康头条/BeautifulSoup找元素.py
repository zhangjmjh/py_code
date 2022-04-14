
from bs4 import BeautifulSoup

path = 'D:/test_app/report/html/TestReport.html'

with open(path,encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(),'lxml')
    failureNum = soup.select('td[id = "failureNum"]')[0].get_text()

    responseTime_list = soup.select("#responseTime")  # 接口时间
    responseName_list = soup.select("#responseName")  # 接口名称
    interfaceUrl_list = soup.select("#interface")   # 接口url


    for i, j, k in zip(responseTime_list,responseName_list,interfaceUrl_list):
        # 找出时间
        time = i.get_text()
        a = time.strip('ms')
        new_time = a.strip(' ')
        print(new_time)

        # 找出接口名称
        name = j.get_text()
        print(name)

        # 找出接口url
        url = k.get_text()

        interface_set = []
        if int(new_time) > 3000 and url not in interface_set:
            interface_set.append(url)






    # print(responseTime)


    print(failureNum)