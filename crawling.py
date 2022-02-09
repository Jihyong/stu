import urllib.request
# 다운로드 할 이미지 경로
# url = "https://www.google.co.kr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
# # 저장할 파일 경로 및 이름
# imgName = "c://Users//이지형/Desktop/google.png"
#
# # 파일 다운로드
# # urlretrieve(URL,저장할_파일_경로)
# urllib.request.urlretrieve(url,imgName)
# print("저장완료")

from bs4 import BeautifulSoup
html = """
    <html>
     <head>
        <title>파이썬 웹 크롤링</title>
     </head>
     <body>
        <h1 id ="title">안녕하세요.</h1>
        <p id ="name">정수아입니다</p>
     </body>
    </html>
"""
# html 태그 구성
# <시작태그> </종료태그>, html은 <head>와 <body> 두 개의 태그가 있음.
soup = BeautifulSoup(html,'html.parser')
# 데이터 위치 찾는 방법
h1 = soup.html.body.h1  # -> <h1>안녕하세요.</h1>
p = soup.html.body.p  # -> <p>정수아입니다</p>
print("h1 :" + h1.string) # h1.string 하면 태그와 태그사이에 있는 안녕하세요가 출력
print("p : " + p.string)

# 함수를 이용해서 태그 찾기
#find()함수 : 원하는 태그를 찾아서 반환, 태그의 이름,속성,속성 값을 이용함.
title = soup.find(id = "title")
name = soup.find(id = "name")
print("title : " + title.string)
print("name : " + name.string)


# find_all 함수: 리스트 형태로 반환
html = """
    <html>
     <head><title>find_all()</title></head>
     <body
        <ul>
            <li><a href = "http://www.naver.com">네이버</a></li>
            <li><a href = "http://www.google.com">구글</a></li>
        </ul>
     </body>
    </html>
"""
soup = BeautifulSoup(html,'html.parser')
list = soup.find_all("a")
for a in list:
    text = a.string  #--> <a> </a> 태그 사이에 있는 글자를 출력
    print(text)
# <태그이름 속성이름="속성의 값">
# 속성의 값을 출력하기 ex) www.naver.com
for a in list:
    href = a.attrs["href"] # attribute의 약자인 attrs["속성"]
    print(href)




'''웹사이트 분석 단계
1. 웹사이트 접속 -> req.urlopen(웹사이트 주소) -> 호출한 결과: html데이터
2. 웹사이트 분석 -> 데이터를 가져와야함
    BeautifulSoup(html 데이터,'파서정류')
3. 원하는 태그 찾기
ex) <title>기상청 이름</title>
    find("태그이름")
'''

import urllib.request as req
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# url 열기
result = req.urlopen(url)
# 데이터 분석하기
soup = BeautifulSoup(result,"html.parser")
# title 추출하기
title = soup.find("title").string
print(title)
print()


## 서울/ 경기 날씨 정보 분석
from urllib import request as req
# urlopen()
target = req.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
soup = BeautifulSoup(target,"html.parser")
# 분석하기전 태그 규칙을 찾아야함 직접.
# 기상청 사이트에서는:
# <location> city wf tmn tmx 모두 location 안에 있음.
# <city>
# <wf>
# <tmn>
# <tmx>
# soup.find("city") = soup.select("city")-> 이렇게 하면 제일 처음에 나오는 <city>만 출력 따라서 for문을 이용한다.
for location in soup.select("location"):
    print("도시:",location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()


# 뉴스 크롤링
'''
1. 부모(<strong class = "tit_g">) 태그를 찾는다.
    select(태그이름) 태그이름 뒤에.을 찍으면 class라는 속성이 있다는걸 의미
    ex) select("strong.tit_g") -> strong.(class)속성값,즉 class라는 속성만 찾을거면 .을 찍음
2. 자식(<a href="링크주소">기사제목</a>)
'''
from bs4 import BeautifulSoup
import urllib.request as req
url = "https://news.daum.net"
result = req.urlopen(url)
soup = BeautifulSoup(result,"html.parser")

news = soup.select("strong.tit_g") # 속성이름이 class 속성값: tit_g
file = open("news.txt","w")
for list in news:
    a = list.select_one("a")
    # print("링크:" + a.get('href'))
    #print("링크 :" + a.attrs['href']) 윗 줄이랑 같음.
    file.write("링크:" + a.get('href')+"\n") # write는 줄바꿈 \n 해야 띄어줌
    title = a.string
    # print("제목:" + title)
    file.write("제목:" + title + "\n")

file.close()

'''
1.파일 열기
변수(파일 객체) = open("파일 경로","모드")
모드:
- w : wirte 모드(새롭게 쓰기)
- a : append 모드(이어 쓰기)
- r : read 모드
2. 작업(읽기, 쓰기)
변수(파일 객체).write("쓰고 싶은 내용")

3. 파일 닫기
- 변수(파일 객체).close()
'''
# file = open("news.txt","w") # basic.txt가 현재 사용중인 디렉토리에 생성
# file.write("Hello Python Programming...!") # 읽기 read()
# file.close()

# 실행 파일 만들기 .exe 파일
