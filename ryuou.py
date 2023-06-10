import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://live.shogi.or.jp/ryuou/')
assert 'TOPページ｜竜王戦中継' in driver.title

kif_url_list = driver.find_elements_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div[1]/p[1]/a")

try:
    if len(kif_url_list) == 0:
        print('本日の対戦はありません')
        exit(1)
    else:
        kif_list = []
        for kif in kif_url_list:
            kif_href = kif.get_attribute('href')
            kif_list.append(kif_href)
    for kif in kif_list:
        driver.get(re.sub(r".html", ".kif", kif))
        kif_text = driver.find_elements_by_tag_name("pre")[0].text
        print(kif_text)
        print ("")
except Exception as e:
    print(e)
    pass
finally:
    driver.quit()  # ブラウザーを終了する。
