from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests
from PIL import Image
import tesserocr

itr = 0
while (1):
	itr = itr + 1
	print("finish times:", itr)
	browser=webdriver.Safari()
	browser.implicitly_wait(10)
	browser.set_window_size(1920, 1080)
	browser.get("http://coursesel.umji.sjtu.edu.cn")

	#获取当前页面标题用于后面比较是否跳转页面
	# time.sleep(1)
	title1 = browser.title

	#输入用户名
	input_name = browser.find_element_by_id("user")
	input_name.send_keys("")

	#输入密码
	input_pass = browser.find_element_by_id("pass")
	input_pass.send_keys("")


	# #获取验证码图片 因为下载了之后验证码会换一张，所以只能截图
	# captcha = browser.find_element_by_id("captcha-img")
	# captcha_url = captcha.get_attribute('src')

	# r = requests.get(captcha_url)
	# # 将获取到的图片二进制流写入本地文件
	# with open('captcha.png', 'wb') as f:
	#     # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入captcha.png中
	#     f.write(r.content)

	#截图获取验证码
	browser.get_screenshot_as_file('screenshot.png')
	#获取验证码图片位置
	element = browser.find_element_by_id('captcha-img')
	left = int(element.location['x'])
	top = int(element.location['y'])
	right = int(element.location['x'] + element.size['width'])
	bottom = int(element.location['y'] + element.size['height'])
	#通过Image处理图像
	im = Image.open('screenshot.png')
	im = im.crop((left, top, right, bottom))
	im.save('captcha.png')
	#识别验证码
	img = Image.open('captcha.png')
	result = tesserocr.image_to_text(img)
	#输入验证码
	input_captcha = browser.find_element_by_id("captcha")
	input_captcha.send_keys(result)

	#判断是否输入了正确的验证码跳转了网页
	# time.sleep(1)
	browser.refresh()
	title2 = browser.title
	if (title1 == title2):
		browser.close()
		print('验证码错误')
		continue
		
	#进入选课界面
	browser.find_element_by_xpath('//*[@id="electTurn"]/div[1]/div[1]/div[1]/a').click()
	# time.sleep(1)
	browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div[5]/label[1]').click()
	browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]').click()
	
	# #判断勾选 (这里以VE280为例)
	# status = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[6]/div[2]/div[1]/div/div')
	# text = status.text
	# if (text == 'Full'):
	# 	print('没有名额')
	# 	continue
	# else:
	# 	browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[6]/div[3]/div[2]/label').click()
	# 	print('抢课成功')
	# 	browser.close()
	# 	break

	#判断勾选 (这里以VM335作为测试)
	status = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[23]/div[2]/div[1]/div/div')
	text = status.text
	if (text == 'Full'):
		print('没有名额')
		browser.close()	
		continue
	else:
		browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[23]/div[3]/div[2]/label').click()
		print('抢课成功')
		browser.close()
		break
	
	time.sleep(5)
	browser.close()
