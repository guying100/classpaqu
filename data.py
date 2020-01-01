import requests
from bs4 import BeautifulSoup
import pymysql

def chai_fen_data(oneli,j):
    input = oneli.select('input')
    imglink = oneli.select('dl dt a img')[j]
    childinfo = input[j]['value']
    child = childinfo.split(',')
    messege = {
        'id': child[3],
        'name': child[0],
        'birthday': child[1],
        'lostTime': child[2],
        'lostPlace': child[4]+child[5],#爬取首页时需要将child[5]去掉
        'registerTime': child[-1],
        'img': "https://www.baobeihuijia.com" + imglink['src']
    }
    return messege


# 解析网页获得信息函数
def get_data_index(html):
    soup = BeautifulSoup(html, 'lxml')
    info = soup.find(class_='loadpic')
    for oneli in info.find_all(name='li'):
        # 调用将数据存入数据库的方法
        save_data( chai_fen_data(oneli,0))

def get_date_page(html):
    soup = BeautifulSoup(html, 'lxml')
    info = soup.find_all(class_='pic_bota')
    i=0;
    for i in range(0,7):
        for j in range(0,5):
            save_data(chai_fen_data(info[i],j))


conn = pymysql.connect(host="localhost", user="root", password="lumengli722", database="niannian", charset="utf8")
cursor = conn.cursor()
print("执行3")
sql = 'insert into childinfo (id,childname,birthday,lostTime,lostPlace,registerTime,img) values (%s, %s, %s, %s, %s, %s, %s)'


# 将数据存入数据库
def save_data(messege):
    id=messege.get('id',4)
    name = messege.get('name',1)
    birthday = messege.get('birthday',2)
    lostTime = messege.get('lostTime',3)
    lostPlace = messege.get('lostPlace',5)
    registerTime = messege.get('registerTime',6)
    img = messege.get('img',7)
    values=(id, name, birthday, lostTime, lostPlace, registerTime, img)
    try:
        cursor.execute(sql,values)
        conn.commit()  # 把修改的数据提交到数据库
    except:
        conn.rollback()



def data_deal():
    # index_r = requests.get('https://www.baobeihuijia.com/Index.aspx')
    # index_html = index_r.text
    # get_data_index(index_html)
    for page in range(1,21):
        url="https://www.baobeihuijia.com/list.aspx?tid=1&sex=&photo=&page="+str(page)
        page_html=requests.get(url).text
        get_date_page(page_html)

if __name__ == "__main__":
   data_deal()