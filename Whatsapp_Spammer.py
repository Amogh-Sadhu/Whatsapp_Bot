from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException as se

#Search Function for non-recent chats
def Search_chat(User):
    #Clickng search bar
    Search = driver.find_element_by_xpath('//div[@class="_2EoyP"]')
    Search.click()
    #Finding the User
    Search_user = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    Search_user.clear()
    Search_user.send_keys(User)
    sleep(1)
    Search_Bar = driver.find_element_by_xpath('//span[@class="matched-text _3Whw5"]')
    Search_Bar.click()
    sleep(2)  # Increase if browser is slow

QR_code = webdriver.ChromeOptions()
QR_code.add_argument('--user-data-dir=C:\\Users\\amogh\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
QR_code.add_argument('-profile-data-directory=Default')
QR_code.add_argument('start-maximized')
QR_code.add_argument('--disable-infobars')

# path for aur driver
Path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path, options=QR_code)
driver.get("http://web.whatsapp.com")
sleep(12)
User = input("Enter the number you want to spam : ")
Enter_msg = input("Enter the spam msg : ")
try:
    # Find user in recent chat
    Search_Box = driver.find_element_by_xpath('//span[@title="{}"]'.format(User))
    Search_Box.click()


except se:
    Search_chat(User)
for i in range(100) :
    # Find msg box windows and sends text
    msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    msg.send_keys(Enter_msg)

    # Find send button and click it
    send_button = driver.find_element_by_xpath("//button[@class='_1U1xa']")
    send_button.click()





