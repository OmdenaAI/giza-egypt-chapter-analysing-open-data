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


def download_image(download_path, url, file_name):
	try:
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)
		file_path = os.path.join(download_path,file_name)

		with open(file_path, "wb") as f:
			image.save(f, "JPEG")

		print("Success")
	except Exception as e:
		print('FAILED -', e)



path_landmk = 'C:\\Users\\htree\\Documents\\giza-egypt-chapter-analysing-open-data\\src\\tasks\\task_3_data_collection\\Landmarks'

pickle_off = open ("landmarks_search_urls.pkl", "rb")
landmarks_list = pickle.load(pickle_off)

for landmark, engine_url in landmarks_list[36:]:
    # create diretory for landmark images
    os.mkdir(landmark)
    
    # set path name 
    path_landmark = os.path.join(path_landmk,landmark)
    
    #wait before scraping again
    time.sleep(10)
    
    print('Now scraping {} images'.format(landmark))
    
    # get urls of many images for choosen landmark
    urls = get_images_from_google(wd, 2, 100, engine_url)
    images_url_dict = {}
    
    # download images using collected urls
    for i, url in enumerate(urls):
        print('image '+str(i) + ' '+url)
        images_url_dict[i] = url
        download_image(path_landmark, url, str(i) + ".jpg")
    
    file_name = landmark+'-images_url.pkl'
    print(file_name)
    #print(image_url_dict)
    with open(file_name,'wb') as f:
        pickle.dump(images_url_dict,f)
        
    
    #number of successfully downloaded files
    print('saved {} images '.format(len(os.listdir(path_landmark))))
    
wd.quit()