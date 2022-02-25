''' 
The code below comes is slight adjustment from code by Tech with Tim 
https://github.com/techwithtim/Image-Scraper-And-Downloader/blob/main/tutorial.py
Associated with https://www.youtube.com/watch?v=NBuED2PivbY
Tim's tutorial is great. Moreover, look for links below video 
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time
import os
import pickle


options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])

PATH = "C:\\Users\\htree\\Documents\\chromedriver.exe"

wd = webdriver.Chrome(chrome_options=options, executable_path=PATH)

def get_images_from_google(wd, delay, max_images, url):
	def scroll_down(wd):
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(delay)

	wd.get(url)

	image_urls = set()
	skips = 0

	while len(image_urls) + skips < max_images:
		scroll_down(wd)

		thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

		for img in thumbnails[len(image_urls) + skips:max_images]:
			try:
				img.click()
				time.sleep(delay)
			except:
				continue

			images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
			for image in images:
				if image.get_attribute('src') in image_urls:
					max_images += 1
					skips += 1
					break

				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
					image_urls.add(image.get_attribute('src'))
					print(f"Found {len(image_urls)}")

	return image_urls



path_landmk = 'C:\\Users\\htree\\Documents\\giza-egypt-chapter-analysing-open-data\\src\\tasks\\task_3_data_collection\\Landmarks'



pickle_off = open ("landmarks_search_urls.txt", "rb")
landmarks_list = pickle.load(pickle_off)

for landmark, engine_url in landmarks_list:

    image_url_dict = {}
    #wait before scraping again
    time.sleep(10)

    print('Now scraping {} images'.format(landmark))

    # get urls of many images for choosen landmark
    urls = get_images_from_google(wd, 2, 100, engine_url)

    # download images using collected urls
    for i, url in enumerate(urls):
        print('image '+str(i) +' '+url)
        image_url_dict[i] = url
        
        
    file_name = landmark+'-images_url.pkl'
    print(file_name)
    #print(image_url_dict)
    with open(file_name,'wb') as f:
        pickle.dump(image_url_dict,f)
        
wd.quit()