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

############### FX ###############

def accept():
	# function that executes the searching, gets variables from inputs
	execute_search(app.getEntry('User key:'), app.getEntry('Searching word:'), constant.search_pages)

def download():
	# function that executes the searching, gets variables from inputs
	num_of_photos = app.getScale("Number of photos")
	execute_search(app.getEntry('User key:'), app.getEntry('Searching word:'), constant.search_pages)

############### Define GUI components ##################

app = gui('dPexels', '640x480')

app.setPadding([20, 0])
app.setInPadding([0, 0])

app.setStretch('sides')
app.addLabel('title', 'Download all the images from PEXELS! :)',colspan=3)
app.addLabelEntry('User key:',colspan=3)
app.addLabel('description', 'You can find your key in this link',colspan=3)
app.addLabel('description_link', 'https://www.pexels.com/api/new/',colspan=3)
app.addLabelEntry('Searching word:',colspan=3)
app.addLabelEntry('Path',colspan=3)
app.addLabelScale("Number of photos",colspan=3)
app.addButton('Accept', accept,7,0)
app.addButton('Download',download,7,1)
app.addButton('Exit',app.stop,7,2)




############### Config ################################

minimum_photos = 0
max_photos = 100

app.configure(bg='lightgray', fg='black', font={'size':14, 'family': 'Helvica'}, resizable='True')
app.buttonFont = 10
app.setTransparency(100)  #Transparency isnt working apprently
app.setLocation('CENTER')
app.setLabelFg('description_link', 'blue')
app.setScaleRange("Number of photos", minimum_photos, max_photos, curr=10)
app.showScaleValue("Number of photos", show=True)

############## Run app #################################

app.go()
