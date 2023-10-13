from selenium import webdriver
from bs4 import BeautifulSoup
def ReadAllLink(self, nContentCnt=0):
    SCROLL_PAUSE_TIME = 1.0
    reallink = []

    pageString = self.driver.page_source
    bsObj = BeautifulSoup(pageString, 'lxml')

    nContentSize = 0
    listcontentCnt = bsObj.select('span.g47SY')
    if len(listcontentCnt) != 0:
        strContentSize = str(bsObj.select('span.g47SY')[0].text)
        nContentSize = int(strContentSize.replace(',', ''))

    # 더이상 새로운것들이 안 읽어지면 끝내준다.
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
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = self.driver.execute_script("return document.body.scrollHeight")

        # 여기 들어오는게 리프래시가 잘 안되는경우..??일것임..
        if new_height == last_height:
            # 리프레시가 잘 안되는 경우가 있어서 처음으로 한번 갔다가 오면 잘되는듯하다!!
            self.driver.execute_script("window.scrollTo(0, 100);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            last_height = new_height
            time.sleep(5)

        ##링크데이터 중복을 제거해준다!! -> 크롤링하며 얻어오는 과정에서 중복으로 입력되는 것!(스크롤내리면서 똑같은게 보일수 잇으니)
        setlink = set(reallink)
        reallink = list(setlink)

        if nContentSize == len(reallink):
            break

        # 얻은 개수와 똑같아 지면 브레이크! -> 너무 많은 경우는 개수가 없다..
        if nPrevlinkCnt == len(reallink):
            nCountCheck += 1
        else:
            nCountCheck = 0

        if nCountCheck > 10:
            break

        # 얻은 개수와 똑같아 지면 브레이크!
        nPrevlinkCnt = len(reallink)

        print("Current Count =" + str(len(reallink)))

    print("AllSize = " + str(nContentSize) + "\tFinishCount =" + str(len(reallink)))

    return reallink;
# Selenium WebDriver 설정
driver = webdriver.Chrome()

# 게시물 페이지로 이동하는 함수
def get_post_html(post_url):
    driver.get(post_url)
    driver.implicitly_wait(10)
    post_page_string = driver.page_source
    return post_page_string


# Selenium WebDriver 설정
driver = webdriver.Chrome()

# 페이지 로딩을 위한 시간을 준다 (적절한 대기 시간으로 조정)
driver.implicitly_wait(10)

# 인스타그램 계정 페이지로 이동
username = 'am.05_29'
account_url = f'https://www.instagram.com/{username}/'
driver.get(account_url)

# 게시물 링크들을 크롤링
reallink = ReadAllLink(driver)

# 게시물 페이지의 HTML 코드를 가져옴
for post_link in reallink:
    post_page_string = get_post_html('https://www.instagram.com' + post_link)
    post_soup = BeautifulSoup(post_page_string, 'html.parser')
    # 이제 post_soup를 사용하여 필요한 정보 추출 및 처리

# WebDriver 종료
driver.quit()



