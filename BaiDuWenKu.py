from selenium import webdriver

options1 = webdriver.ChromeOptions()
options1.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) ' 'AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(options = options1)
driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')
page = driver.find_elements_by_xpath("//body/div[2]/div[2]/div[@class='sf-edu-wenku-id-container wrap xreader-container reader-xreader']/div[2]/div[@class='foldpagewg-root']/div/div/div")
driver.execute_script('arguments[0].scrollIntoView();', page[-1]) #拖动到可见的元素去
nextpage = driver.find_elements_by_xpath("//body/div[2]/div[2]/div[@class='sf-edu-wenku-id-container wrap xreader-container reader-xreader']/div[2]/div[@class='foldpagewg-root']/div/div/div")
nextpage.click()
# 剩余工作即使用BeautifulSoup爬取文档内容，之前有便不写了