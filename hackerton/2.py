from selenium import webdriver
from bs4 import BeautifulSoup
import time
from lxml
class InstagramCrawler:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.SCROLL_PAUSE_TIME = 1.0

    def get_post_html(self, post_url):
        self.driver.get(post_url)
        self.driver.implicitly_wait(10)
        post_page_string = self.driver.page_source
        return post_page_string

    def read_all_link(self, nContentCnt=0):
        reallink = []

        pageString = self.driver.page_source
        bsObj = BeautifulSoup(pageString, 'lxml')

        nContentSize = 0
        listcontentCnt = bsObj.select('span.g47SY')
        if len(listcontentCnt) != 0:
            strContentSize = str(bsObj.select('span.g47SY')[0].text)
            nContentSize = int(strContentSize.replace(',', ''))

        # 더이상 새로운 것들이 안 읽어지면 끝내준다.
        nCountCheck = 0
        nPrevlinkCnt = 0
        while True:
            if nContentCnt == len(reallink) and nContentCnt != 0:
                break

            pageString = self.driver.page_source
            bsObj = BeautifulSoup(pageString, 'lxml')

            for link1 in bsObj.find_all(name='div', attrs={"class": "Nnq7C weEfm"}):
                SelData = link1.select('a')
                for i in range(len(SelData)):
                    title = SelData[i]
                    real = title.attrs['href']
                    reallink.append(real)

            last_height = self.driver.execute_script('return document.body.scrollHeight')
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(self.SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                self.driver.execute_script("window.scrollTo(0, 100);")
                time.sleep(self.SCROLL_PAUSE_TIME)
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                last_height = new_height
                time.sleep(5)

            setlink = set(reallink)
            reallink = list(setlink)

            if nContentSize == len(reallink):
                break

            if nPrevlinkCnt == len(reallink):
                nCountCheck += 1
            else:
                nCountCheck = 0

            if nCountCheck > 10:
                break

            nPrevlinkCnt = len(reallink)

            print("Current Count =" + str(len(reallink)))

        print("AllSize = " + str(nContentSize) + "\tFinishCount =" + str(len(reallink)))

        return reallink

# 인스턴스 생성
crawler = InstagramCrawler()

# 인스타그램 계정 페이지로 이동
username = 'am.05_29'
account_url = f'https://www.instagram.com/{username}/'
crawler.driver.get(account_url)

# 게시물 링크들을 크롤링
reallink = crawler.read_all_link()

# 게시물 페이지의 HTML 코드를 가져옴
for post_link in reallink:
    post_page_string = crawler.get_post_html('https://www.instagram.com' + post_link)
    post_soup = BeautifulSoup(post_page_string, 'html.parser')
    # 이제 post_soup를 사용하여 필요한 정보 추출 및 처리

# WebDriver 종료
crawler.driver.quit()
