# Get All Result of SSQ
from requestFn import getHtml
from xpathFn import getHtmlSpecData


def getData(url, conditionPath):
    #1.get html from url
    html = getHtml(url)
    #2.get data from html
    data = getHtmlSpecData(html, conditionPath)
    result = list()
    while len(data['title']) > 0:
        result.append({"periodical":data['title'][0],
        "redBalls":data['Balls'][:6],
        "blueBall":data['Balls'][6]
        })
        data['title'] = data['title'][1:]
        data['Balls'] = data['Balls'][7:]
    
    return result


prefixUrl = "http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum="
condition = {
        "title": "//tr[position()>2 and position()<last()]/td[2]/text()",
        "Balls": "//tr[position()>2 and position()<last()]/td[3]/em/text()"
    }
# print({key:value for key,value in condition.items()})  
urls = {prefixUrl + str(x) for x in range(1, 3)}

result = [getData(url, condition) for url in urls]

data = list()
for item in result:
    data.extend(item)

for item in data:
    print(item)
