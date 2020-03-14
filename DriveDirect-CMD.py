import pandas as pd

#Print Welcome statement
print('Welcome to the Google Drive Direct Download Link Generator!')
#Get URL
link = input('Please paste in your URL: ')
#Create downloadLink and make a string
downloadLink = str('')
#Create direct URL
downloadLink = link.replace('file/d/', 'uc?export=download&id=')
downloadLink = downloadLink.replace('/view?usp=sharing', '')
#Print URL
print('Your URL is', downloadLink)
#Copy to clipboard
df = pd.DataFrame([downloadLink])
df.to_clipboard(index=False, header=False)
print('Your URL has been copied to your clipboard.')
