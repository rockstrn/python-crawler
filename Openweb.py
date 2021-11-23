from selenium import webdriver
import time
import traceback

#打开谷歌浏览器
from selenium.webdriver.common.by import By
def getInfo(task_id):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Safari()
# #打开百度搜索主页
#     task_id = 'fa4317aa-3cc7-444b-bc81-dec0d19692a6'
    driver.get('https://iris.woa.com/#/record/task_info?task_id='+task_id)

# driver.switch_to.frame('logBtn')
#
# driver.find_element(By.TAG_NAME, 'button').click()
    time.sleep(1)
    driver.implicitly_wait(20)
    driver.find_element(By.ID, "btn_smartlogin").click()
    time.sleep(2)
    driver.implicitly_wait(20)
    filestatesoure = ''
    filestate = ''
    recordState = ''
    meetingId = ''
    meetingCode = ''
    try:
        filestatesoure = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/section/div[1]/div[3]/div/div[2]/div/span/div[6]/span[3]/div/span/div[3]/span[3]/div[5]/span[2]")
        filestate = filestatesoure.text
        recordState = driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/section/div[1]/div[3]/div/div[2]/div/span/div[4]/span[2]/span[2]").text
        meetingId = driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/section/div[1]/div[3]/div/div[2]/div/span/div[1]/span[3]/div[2]/span[2]").text
        meetingCode = driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/section/div[1]/div[3]/div/div[2]/div/span/div[1]/span[3]/div[3]/span[2]").text
    except:
        print(traceback.format_exc())
    print(filestate)
    driver.close()
    # meetingId.strip('"')
    # meetingCode.strip('"')
    # recordState.strip('"')
    # filestate.strip('"')
    return meetingId, meetingCode, recordState, filestate

# info = driver.find_elements(By.XPATH, "/html/body/div/div/div[2]/form/div[3]/div/div/div[3]/input").append()
# info = driver.find_elements(By.ID'btn_smartlogin').click()


# help(webdriver.Firefox)