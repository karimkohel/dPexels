"""
								dPexel  0.5
A simple app with a UI that allows users to download bulk images from Pexel (image wesbsite)

"""

############### Imports ###############

from appJar import gui

############### FX ###############


# handle buttons pressin'
def press(button):
	if button == 'Exit':
		app.stop()
	elif button == 'Accept':
		user_key = app.getEntry("User key")
		download_path = app.getEntry("Images path")
		print("key:", user_key, "download path:", download_path)
	else:
		pass

############### Config ###############

app = gui('Bulk from pexels', '640x480')
app.configure(bg='lightgray', fg='black', font={'size':14, 'family': 'Helvica'}, resizable='True')
app.buttonFont = 10
app.setTransparency(100)
app.setLocation('CENTER')

############### Main ###############

app.addLabel('title', 'Download all the images from PEXELS! :)')
app.addLabelEntry('User key')
app.addLabelEntry('Images path')
app.addButtons(["Accept", "Exit"], press)


app.go()