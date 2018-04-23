#!/usr/bin/env python
# -- coding: utf-8 --

from selenium import webdriver
import time

browser = webdriver.Firefox()


def login(browser, email, password):
	try:
		# Fill the email field
		emailField = browser.find_element_by_id('email')
		emailField.send_keys(email)

		# Fill the password field
		passwordField = browser.find_element_by_id('pass')
		passwordField.send_keys(password)

		# Click 'เข้าสู่ระบบ' button
		# loginButton = browser.find_elements_by_id('Submit')[1]
		# loginButton.click()
		passwordField.submit()

		time.sleep(2)

		if browser.current_url == 'http://freeads.in.th/member/index.php':
			return True
		else:
			return False

	except Exception as e:
		print('Login Exception: %s' % e)
		return False

def show_current_url(browser):
	print('Current URL: %s' % browser.current_url)

def main():
	try:
		# Go to home page
		browser.get('http://freeads.in.th/')
		show_current_url(browser)

		# Go to login page
		goToLoginButton = browser.find_element_by_xpath('//a[@title="เข้าสู่ระบบ"]')
		goToLoginButton.click()
		show_current_url(browser)

		# We have to login all the time because
		# this web isn't remember cookies.
		if login(browser, 'my_email', 'my_password'):
			print('login pass...')
			show_current_url(browser)

			# Go to free post page
			goToFreePostButton = browser.find_element_by_xpath('//a[@title="ลงประกาศฟรี"]')
			goToFreePostButton.click()
			show_current_url(browser)

			titleTextFieldElem = browser.find_element_by_id('post_title')
			titleTextFieldElem.send_keys('กระเป๋าหนัง')

	except Exception as e:
		print('Exception: %s' % e)

if __name__ == '__main__':
	main()
