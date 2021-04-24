import pyttsx3 as ts
import PyPDF2

# get the pdf file in binary mode
book = open("II.pdf", 'rb')
#read the pdf file
pdfReader = PyPDF2.PdfFileReader(book)
#get the number of pages available
pages = pdfReader.numPages
print(pages)
# Intialize speaker
speaker = ts.init()
#iterate through all the pages and speak
voices = speaker.getProperty('voices')
# for male voice id = 0,female is 1
speaker.setProperty('voice', voices[1].id)
for num in range(8, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()