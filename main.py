from tkinter import *
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
for voice in voices:
      engine.setProperty("rate", 175)
      engine.setProperty("voice", voices[1].id, )

def speak(text):
        engine.say(text)
        engine.runAndWait()

def audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

            try:
                statement = r.recognize_google(audio, language='en-in')  # en at hi for english

            except Exception:
                return "None"

            return statement

    
    
root = Tk()


root.title("Question App")
root.geometry('800x550')
root.resizable(False,False)
root.config(bg="black")


def run():
    card_no = entry.get()
    odd_sum = 0
    even_sum = 0
    double_value = []
    number = list(card_no)
    for (idx, val) in enumerate(number):
        if idx % 2 != 0:  # this is an odd number
            odd_sum += int(val)
        else:  # this is an even no.
            double_value.append(2 * int(val))

    # converting the list into string
    double_string = ""
    for x in double_value:
        double_string += str(x)

    # converting string into list
    double_value = list(double_string)
    for x in double_value:
        even_sum += int(x)

    # total sum
    sum = odd_sum + even_sum
    if sum % 10 == 0:
        speak("This is a Valid Card NUMBER")
    else:
        speak("Invalid Card NUMBER")


label1 = Label(root,text=" CREDIT CARD VALIDATOR ", fg="red",bg="black",font=("Arial",30))
label1.pack(ipadx=150,ipady=100)

label2 = Label(root,text=" Credit / Debit card Number",fg="Yellow",bg="black",font=("Arial",15))
label2.pack(ipadx=20,ipady=20)

entry = Entry(root,text=" Credit card Number ",fg="Green",bg="Orange",font=("Arial",15))
entry.pack(ipadx=10,ipady=10)
btn = Button(root,text=" Check ",fg="Black",bg="White",font=("Arial",15),command=lambda : run())
btn.place(x=350,y=400)

root.mainloop()