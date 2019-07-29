from appJar import gui
import tkinter as tk

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


# basic configuration of app
app = gui('Bulk from pexels', '640x480')
app.configure(bg='lightgray', fg='black', font={'size':14, 'family': 'Helvica'}, resizable='True')
app.buttonFont = 10
app.setTransparency(100)
app.setLocation('CENTER')

# define labels and buttons
app.addLabel('title', 'Download all the images from PEXELS! :)')
app.addLabelEntry('User key')
app.addLabelEntry('Images path')
app.addButtons(["Accept", "Exit"], press)

# run app
app.go()