from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class AppleMusic:
	def __init__(self):
		self.display = Display(visible=0, size=(1600, 1200))
		self.display.start()
		self.driver = webdriver.Chrome('/Users/chrisdo/Desktop/chromedriver')
		self.driver.get('https://music.apple.com/login')

	def sign_in(self):
		print("Signing in...")
		sleep(1)
		seq = self.driver.find_elements_by_tag_name('iframe')
		print(len(seq), " iframes")
		iframe = self.driver.find_elements_by_tag_name('iframe')[1]
		self.driver.switch_to.frame(iframe)
		sleep(1)
		self.driver.switch_to.frame('aid-auth-widget-iFrame')
		sleep(1)
		self.driver.find_element_by_id('account_name_text_field').send_keys("<INSERT_USERNAME>")
		self.driver.find_element_by_id('sign-in').click()
		sleep(1)
		self.driver.find_element_by_id('password_text_field').send_keys("<INSERT_PASSWORD>")
		self.driver.find_element_by_id('sign-in').click()
		sleep(2)

		if self.driver.find_element_by_id('stepEl'):
			print("2FA Activated!")
			success = False
			code = input("Enter code: ")
			while not success:
				for i in range(0, 6):
					self.driver.find_element_by_id("char"+str(i)).send_keys(code[i])
				sleep(3)
				try:
					self.driver.find_element_by_xpath('//*[@id="stepEl"]/hsa2/div/verify-device/div/div/div[1]/div')
					print("Incorrect verification code")
					code = input("Enter code: ")
				except:
					success = True
			sleep(2)
			#self.driver.find_element_by_id('contains(not-now-trust-)').click()
			self.driver.find_element_by_css_selector("[id*='dont-trust-browser']").click()
			sleep(30)

	def screenshot(self):
		self.driver.save_screenshot('applemusic.png')

	def quit(self):
		self.driver.quit()


instance = AppleMusic()
instance.sign_in()
instance.screenshot()
instance.quit()


