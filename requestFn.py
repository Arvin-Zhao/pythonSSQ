import requests

def getHtml(url):
    return requests.get(url).text

if __name__ == "__main__":
    r = getHtml("http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum=1")
    print(r.text)
