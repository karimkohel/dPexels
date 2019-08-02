#"""
								#dPexel  0.5
#A simple app with a UI that allows users to download bulk images from #Pexel (image wesbsite)

#"""

############### Imports ###############

from appJar import gui
from apiRequests import execute_search
from apiRequests import search_urls
from apiRequests import download_images
import constant
from tempfile import TemporaryFile
import os

############### FX ###############

def set_():
	# function that executes the searching, gets variables from inputs
	execute_search(app.getEntry('User key:'), app.getEntry('Searching word:'), constant.search_pages)
	max_photos = len(search_urls)
	app.setScaleRange("Number of photos", minimum_photos, max_photos, curr=10)
	write_cached_data()

def download():
	# function that downloads desired amount of images from the requested array of urls
	num_of_photos = app.getScale("Number of photos")
	download_images(search_urls, app.getEntry('Path'), num_of_photos)

def quit_app():
	# function that executes when the exit button is pressed
	app.stop()

def write_cached_data():
	# function to write temporal data from current usage of the app
	data = open('temp.txt', 'w') 
	if (app.getEntry('User key:') != ''):
		data.writelines(app.getEntry('User key:') + '\n')
	else:
		data.writelines('key\n') 		
	if (app.getEntry('Path') != ''):
		data.writelines(app.getEntry('Path') + '\n')
	else:
		data.writelines('path\n')
	data.close()
	
def read_cached_data():
	# function to read temporal data from previous usages of the app 
	print('reading old data')
	if (os.path.exists('./temp.txt')):
		data = open('temp.txt', 'r') 
		data_ = data.readlines()
		print(data_)
		if (data_[0] != 'key\n'):
			user_key = data_[0].split('\n')[0]
			app.setEntry('User key:', user_key)
			print(user_key)
		if (data_[1] != 'path\n'):	
			path = data_[1].split('\n')[0]
			app.setEntry('Path', path)
			print(path)
	else:
		file = open('temp.txt', 'w')
		file.write('key\n')
		file.write('path\n')
	


############### Define GUI components ##################

app = gui('dPexels', '640x480')

app.setPadding([10, 0])
app.setInPadding([0, 0])

app.setStretch('sides')
app.addLabel('title', 'Download all the images from PEXELS! :)',colspan=3)
app.addLabelEntry('User key:',colspan=3)
app.addLabel('description', 'You can find your key in this link',colspan=3)
app.addWebLink('https://www.pexels.com/api/new/', 'https://www.pexels.com/api/new/',colspan=3)
app.addLabelEntry('Searching word:',colspan=3)
app.addLabelEntry('Path',colspan=3)
app.addLabelScale("Number of photos",colspan=3)
app.addButton('Set', set_,7,0)
app.addButton('Download',download,7,1)
app.addButton('Exit',quit_app,7,2)




############### Config ################################

minimum_photos = 0
max_photos = 0

app.configure(bg='lightgray', fg='black', font={'size':14, 'family': 'Helvica'}, resizable='True')
app.buttonFont = 10
app.setTransparency(100) # 100 means that it is not transparent
app.setLocation('CENTER')
app.setScaleRange("Number of photos", minimum_photos, max_photos, curr=0)
app.showScaleValue("Number of photos", show=True)

################ read if exists previous defined variables


read_cached_data()


############## Run app #################################

app.go()



