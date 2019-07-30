"""
								dPexel  0.5
A simple app with a UI that allows users to download bulk images from Pexel (image wesbsite)

"""

############### Imports ###############

from appJar import gui

############### FX ###############

def accept():
	user_key = app.getEntry("User key")
	download_path = app.getEntry("Images path")
	print("key:", user_key, "download path:", download_path)

############### Config ###############

app = gui('Bulk from pexels', '640x480')
app.configure(bg='lightgray', fg='black', font={'size':14, 'family': 'Helvica'}, resizable='True')
app.buttonFont = 10
app.setTransparency(100)
app.setLocation('CENTER')

############### Main ###############

app.addLabel('title', 'Download all the images from PEXELS!',colspan=2)
app.addLabelEntry('User key',colspan=2)
app.addLabelEntry('Images path',colspan=2)
app.addButton("Accept", accept,row=3,column=0)
app.addButton("Exit",app.stop,row=3,column=1)

app.go()