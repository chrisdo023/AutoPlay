from pyvirtualdisplay import Display
	from selenium import webdriver
	

	class AppleMusic:
	    def __init__(self):
	        self.display = Display(visible=0, size=(1600, 1200))
	        self.display.start()
	        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
	        self.driver.get('https://music.apple.com/us/browse')
	

	    def screenshot(self):
	        self.driver.save_screenshot('applemusic.png')
	

	    def quit(self):
	        self.driver.quit()
	

	instance = AppleMusic()
	instance.screenshot()
	instance.quit()


