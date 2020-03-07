import pandas as pd

#Define colours for print
class colour:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    END = '\033[0m'

#Print Welcome statement
print(colour.BOLD, colour.BLUE, 'Welcome to the Google Drive Direct Download Link Generator!', colour.END)
#Start colour for input print
print(colour.BOLD, colour.PURPLE)
#Get URL
link = input('Please paste in your URL: ')
#End colour for input print
print(colour.END)
#Create downloadLink and make a string
downloadLink = str('')
#Create direct URL
downloadLink = link.replace('file/d/', 'uc?export=download&id=')
downloadLink = downloadLink.replace('/view?usp=sharing', '')
#Print URL
print(colour.BOLD, colour.GREEN, 'Your URL is', downloadLink, colour.END)
#Copy to clipboard
df = pd.DataFrame([downloadLink])
df.to_clipboard(index=False, header=False)
print(colour.GREEN, 'Your URL has been copied to your clipboard.', colour.END)
