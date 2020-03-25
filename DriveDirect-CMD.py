print('Welcome to the Google Drive Direct Download Link Generator!')

link = input('Please paste in your URL: ')

downloadLink = str('')

downloadLink = link.replace('file/d/', 'uc?export=download&id=')
downloadLink = downloadLink.replace('/view?usp=sharing', '')

print('Your URL is', downloadLink)

#Copy to clipboard
import pyperclip
pyperclip.copy(downloadLink)
pyperclip.paste()
print('Your URL has been copied to your clipboard.')
