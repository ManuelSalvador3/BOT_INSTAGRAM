from time import sleep
from selenium import webdriver

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.driver = webdriver.Chrome("C:/Users/manus/PYTHON/chromedriver")
        self.driver.get('http://www.instagram.com/')
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/p/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name= \"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name= \"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Ahora no')]").click()
        sleep(2)
        

    def buscar_usuarios(self):
        buscador = "mariogil_27"
        self.driver.find_element_by_xpath("//input[@type=\"text\"]").send_keys(buscador)
        #self.driver.find_element_by_xpath("//a[contains(@href, '/mariogil_27')]").click()
        self.driver.find_elements_by_link_text("mariogil_27").click()

    #def get_unfollowers(self):
        #self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click() 
        #self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format('/following')).click()


#CHANGE USERNAME AND PASSWORD FOR YOUR OWN
my_bot = InstaBot('USERNAME', 'PASSWORD')
my_bot.buscar_usuarios()
#my_bot.get_unfollowers()

