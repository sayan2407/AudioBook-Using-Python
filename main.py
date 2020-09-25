import pyttsx3
import PyPDF2

#book=open('dbms.pdf','rb')
#pdfReader=PyPDF2.PdfFileReader(book)
#pages=pdfReader.numPages
#print(pages)
speaker = pyttsx3.init()
filename=input("Enter Text File Name :")
file=open(filename,"r")
#page=pdfReader.getPage(8)
#print(text)
#file = open("sample.txt", "r")
speaker.say(file.read())
speaker.runAndWait()
