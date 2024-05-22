# importing the dependencies
import speech_recognition as sr
import pyttsx3
import time
from googletrans import Translator
ts=Translator()

i=0
# initialising the speech recognizer
r=sr.Recognizer()
print("Please speak line wise and wait for confirmation before proceeding to speak for the next line!")
print("\n")

# creating a delay  to make the above text readable and understandable
time.sleep(4)

print("You may start speaking now!")

# function for recording voice
def record():
    while 1:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2,duration=0.2)
                audio2=r.listen(source2)
                my_text=r.recognize_google(audio2)
                return my_text
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown Eroor Occured")
    return

# function for writing onto the file 
def output_text(text):
    f=open("content.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return
while(i<5):
    text=record()
    output_text(text)
    print("Wrote text")
    i=i+1
print("File created!")


# function for reading the file line wise and translating it 
def spanish():
    read_handle=open("content.txt","r")
    line=read_handle.read()
    result=ts.translate(line,dest='es')
    second=open("espanol.txt","w")
    second.write(result.text)
    second.close()
    print("Translation succesful, new file has been created!")

def russian():
    read_handle=open("content.txt","r")
    line=read_handle.read()
    result=ts.translate(line,dest='ru')
    second=open("russian.txt","w",encoding="utf-8")
    second.write(result.text)
    second.close()
    print("Translation succesful, new file has been created!")

def japanese():
    read_handle=open("content.txt","r")
    line=read_handle.read()
    result=ts.translate(line,dest='ja')
    second=open("japanese.txt","w",encoding="utf-8")
    second.write(result.text)
    second.close()
    print("Translation succesful, new file has been created!")


def german():
    read_handle=open("content.txt","r")
    line=read_handle.read()
    result=ts.translate(line,dest='de')
    second=open("german.txt","w")
    second.write(result.text)
    second.close()
    print("Translation succesful, new file has been created!")


def french():
    read_handle=open("content.txt","r")
    line=read_handle.read()
    result=ts.translate(line,dest='fr')
    second=open("french.txt","w")
    second.write(result.text)
    second.close()
    print("Translation succesful, new file has been created!")
    


# creating a translation menu
print("Please select a language to translate your text by pressing 1,2,3 or 4")
print("\n")

print("1. Spanish")
print("2. Russian")
print("3. Japanese")
print("4. German")
print("5. French")

lang=int(input("Enter the number"))
if lang==1:
    spanish()
elif lang==2:
    russian()
elif lang==3:
    japanese()
elif lang==4:
    german()
elif lang==5:
    french()
else:
    print("Incorrect input!")
    


