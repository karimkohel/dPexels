"""
								dPexel  0.5
A simple app with a UI that allows users to download bulk images from Pexel (image wesbsite)

"""

############### Imports ###############

from appJar import gui
from apiRequests import execute_search
from apiRequests import search_urls
from apiRequests import download_images
import constant

############### FX ###############


# handle buttons pressin'
def press(button):
	if button == 'Exit':
		app.stop()
	elif button == 'Accept':
		# function that executes the searching, gets variables from inputs
		execute_search(app.getEntry('User key:'), app.getEntry('Searching word:'), constant.search_pages)
	elif button == 'Download images':
		print(search_urls)		
		download_images(search_urls, app.getEntry('Path'))
	else:
		pass

############### Define GUI components ##################

app = gui('dPexels', '640x480')

app.setPadding([0, 0])
app.setInPadding([0, 0])

app.setStretch('sides')
app.addLabel('title', 'Download all the images from PEXELS! :)')
app.addLabelEntry('User key:', 1, 0, 2)
app.addLabel('description', 'You can find your key in this link', 4, 0)
app.addLabel('description_link', 'https://www.pexels.com/api/new/', 5, 0)
app.addLabelEntry('Searching word:', 6, 0, 2)
app.addLabelEntry('Path', 7, 0, 2)
app.addButtons(["Accept", "Download images", "Exit"], press, 20, 0)



############### Config ################################

app.configure(bg='lightgray', fg='black', font={'size':14, 'family': 'Helvica'}, resizable='True')
app.buttonFont = 10
app.setTransparency(100)  #Transparency isnt working apprently
app.setLocation('CENTER')
app.setLabelFg('description_link', 'blue')

############## Run app #################################

app.go()