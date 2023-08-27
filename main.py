# -*- coding: utf-8 -*-
from selenium import webdriver
# from webdriver_maniger.chrome import ChromeDriverManager

# driver = webdriver.Chrome("chromedriver-mac-arm64/chromedriver") # Webdriver 파일의 경로를 입력
driver = webdriver.Chrome() # we don't need to get chromedriver anymore due to update of selenium, just leave that parentheses blank
driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do') # 이동을 원하는 페이지 주소 입력 