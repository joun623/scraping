from selenium import webdriver
driver = webdriver.PhantomJS(executable_path='C:/bin/phantomjs-2.1.1-windows/bin/phantomjs.exe')

driver.get('https://xxxxxxx')
driver.implicitly_wait(10)
csa_export = driver.find_element_by_id('xxxxx')
csa_export.click()
csa_txt = driver.find_element_by_css_selector('xxxx').text
