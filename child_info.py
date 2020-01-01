# # from selenium import webdriver
# # browser = webdriver.Chrome()
# import urllib.request
# import requests
# import re
# from lxml import etree
# from bs4 import BeautifulSoup
# if __name__=="__main__":
#     # response = urllib.request.urlopen('https://www.baobeihuijia.com/Index.aspx')
#     # print(response.read().decode('utf-8'))
#     r=requests.get('https://www.baobeihuijia.com/Index.aspx')
#     # with open('favicon.ico', 'wb') as f:
#     #     f.write(r.content)
#     # print(r.text)
#     # content='{"topicId":49475,"subject":"春运","cover":"https://s1.tuchong.com/content-image/201912/f6dcab5d194942df90dd13db90cfef1c.jpeg",'
#     # result=re.match('[a-zA-z]+://[^\s]*',content)
#     # print(result)
#     # html=etree.HTML(r.text)
#     # result=html.xpath('//div//input')
#     # print(result)
#     html=r.text
#     print(type(html))
#     soup = BeautifulSoup(html, 'lxml')
#     info=str(soup.find(class_='loadpic'))
#     soup = BeautifulSoup(info, 'lxml')
#     for oneli in soup.select('li'):
#         input=oneli.select('input')
#         imglink=oneli.select('dl dt a img')
#         childinfo=input['value']
#         img=imglink['src']
