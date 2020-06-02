import pyperclip

print('Welcome to the Google Drive Direct Download Link Generator!')

downloadLink = (((input('Please paste in your URL: ').replace('file/d/', 'uc?export=download&id=')).replace('/view?usp=sharing', '')).replace('/view', ''))

print('Your URL is', downloadLink)

#Copy to clipboard
pyperclip.copy(downloadLink)
print('Your URL has been copied to your clipboard.')
