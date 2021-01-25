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
		self.repeat = 0
		self.shuffle = 0

	def sign_in(self):
		sleep(2)
		iframe = self.driver.find_elements_by_tag_name('iframe')[1]
		self.driver.switch_to.frame(iframe)
		sleep(1)
		self.driver.switch_to.frame('aid-auth-widget-iFrame')
		sleep(1)
		self.driver.find_element_by_id('account_name_text_field').send_keys("<INSERT_USERNAME>")
		self.driver.find_element_by_id('sign-in').click()
		sleep(1.5)
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
			self.driver.find_element_by_css_selector("[id*='dont-trust-browser']").click()
			sleep(2)

	def search(self, song_name):
		sleep(5)
		self.driver.find_element_by_id('web-navigation-search-box').send_keys(song_name, Keys.ENTER)
		sleep(5)
		songs = self.driver.find_element_by_class_name('shelf-grid__body')
		ul = songs.find_element_by_xpath('//*[@id="web-main"]/div[5]/div/div[2]/div[4]/div/div[2]/ul')
		li = ul.find_elements_by_tag_name('li')
		print(len(li))
		sleep(1)
		outerdiv = li[0].find_element_by_class_name('viewport-renderer')
		sleep(1)
		id = outerdiv.get_attribute('id')
		for i in range(0, len(li)):

			# outerdiv = li[i].find_element_by_class_name('viewport-renderer')
			# sleep(1)
			# id = outerdiv.get_attribute('id')
			# print(id)
			innerdiv = outerdiv.find_element_by_xpath('//*[@id=' + '"' + id + '"' + ']/div')
			sleep(1)
			name = innerdiv.get_attribute('aria-label')
			print(name)
			num = int(float(id)) + 7
			id = str(num)

	def play(self):
		self.driver.find_element_by_xpath('//*[@id="web-main"]/div[3]/div/div[1]/div/div[2]/button[2]').click()

	def pause(self):
		self.driver.find_element_by_xpath('//*[@id="web-main"]/div[3]/div/div[1]/div/div[2]/button[1]').click()

	def back(self):
		self.driver.find_element_by_xpath('//*[@id="web-main"]/div[3]/div/div[1]/div/div[2]/button[1]').click()

	def forward(self):
		self.driver.find_element_by_xpath('//*[@id="web-main"]/div[3]/div/div[1]/div/div[2]/button[3]').click()

	def repeat(self):
		if self.repeat == 1:
			print('Repeating playlist')
			self.driver.find_element_by_xpath('//*[@id="web-main"]/div[3]/div/div[1]/div/div[3]')
			self.repeat = self.repeat + 1
		else:
			print('Repeating song')
			self.driver.find_element_by_xpath('//*[@id="web-main"]/div[3]/div/div[1]/div/div[3]')
			self.repeat = 0

	def shuffle(self):
		if self.shuffle == 0:
			print('Shuffling')
			self.driver.find_element_by_xpath('//*[@id="web-main"]/div[3]/div/div[1]/div/div[1]')
			self.shuffle = self.shuffle + 1
		else:
			print('Shuffling turned off')
			self.driver.find_element_by_xpath('//*[@id="web-main"]/div[3]/div/div[1]/div/div[1]')
			self.shuffle = 0

	def screenshot(self):
		self.driver.save_screenshot('applemusic.png')

	def quit(self):
		self.driver.quit()


if __name__ == "__main__":
	instance = AppleMusic()
	instance.sign_in()
	instance.search("get up far east movement")
	instance.screenshot()
	instance.quit()


