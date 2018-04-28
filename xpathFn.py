from lxml import etree
from io import StringIO

def getHtmlSpecData(htmlData,condition):
    html = etree.HTML(htmlData) 
    if isinstance(condition,dict):
        return { key:html.xpath(value) for key,value in condition.items()}
    if isinstance(condition,list):
        return {html.xpath(x) for x in condition }
    if isinstance(condition,str):
        return html.xpath(condition)
        