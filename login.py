# Const
import const as CONST
import chromedriver_binary # ChromeDriver

# library & module
from selenium import webdriver # Smodule elenium webdriver
from selenium.webdriver.support.ui import WebDriverWait

# arguments from comand line
import sys 
args = sys.argv

# Open browser
# /Users/Kenta/Desktop/Selenium/chromedriver
driver = webdriver.Chrome()

# Seeting of Timeout
wait = WebDriverWait(driver, 10)

# Try login
def login_to_time_records(args):

	url = args[1]
	login = args[2]

	# URL
	if url == 'dev':
		driver.get(CONST.URL_LOGIN['DEV'])
	elif url == 'stg':
		driver.get(CONST.URL_LOGIN['STG'])
	elif url == 'prd':
		driver.get(CONST.URL_LOGIN['PRD'])


	# ID, PW
	login_id = ''
	login_pw = ''

	if login == 'master':
		login_id = CONST.MASTER['ID']
		login_pw = CONST.MASTER['PW']
	elif login == 'fc1':
		login_id = CONST.FC1['ID']
		login_pw = CONST.FC1['PW']
	elif login == 'fc2':
		login_id = CONST.FC2['ID']
		login_pw = CONST.FC2['PW']
	elif login == 'fc3':
		login_id = CONST.FC3['ID']
		login_pw = CONST.FC3['PW']

	input_id = driver.find_element_by_name('email')
	input_password = driver.find_element_by_name('password')

	input_id.send_keys(login_id)
	input_password.send_keys(login_pw)

	button_login = driver.find_element_by_class_name('form__submit--login')
	button_login.click()

	## Transfer to Time records page
	print('-------Complete login-------')

login_to_time_records(args)
