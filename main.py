from tkinter import *
import speech_recognition as sr
import sys
try:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        import random

        root = Tk()
        count = 0
        actual_number = random.randint(1, 100)


        def hint(number, ac_number):
            pass


        def working():
            try:
                global count
                count += 1
                Label(root,text="Speak again").grid(row=5,column=1)
                audio=r.listen(source)
                e1=r.recognize_google(audio)
                Label(root,text=f"Your number : {e1}").grid(row=1,column=1)
                number = int(e1)
                # Label(root,text=f"{actual_number}").grid(row=5,column=1)
                if type(number)=='string':
                    print("You are too high")

                elif (number > 101):
                    Label(root, text="In Limit", fg="red").grid(row=2, column=1)
                elif (number == 101):
                    if (number < actual_number):
                        Label(root, text="Go " + str(actual_number - number) + " high", fg="dark green").grid(row=2,
                                                                                                              column=1)
                    elif (actual_number < number):
                        Label(root, text="Go " + str(number - actual_number) + " low", fg="slate blue").grid(row=2,
                                                                                                             column=1)
                elif (number > actual_number):
                    Label(root, text="Go low", fg="Dodgerblue2").grid(row=2, column=1)
                elif (number < actual_number):
                    Label(root, text="Go high", fg="OrangeRed2").grid(row=2, column=1)
                elif (number == actual_number):
                    Label(root, text="Bingo!!! Right Answer", fg="sandy brown").grid(row=2, column=1)
                    Label(root, text="Number of counts were = " + str(count), fg="orange").grid(row=3, column=1)
                    sys.exit()
                    return
                else:
                    Label(root, text="Wrong Input").grid(row=2, column=1)
            except:
                Label(root, text="Wrong Input")


        root.title("Let's Guess")
        print("Please speak the number ranging between 1 and 100 = ")
        l1 = Label(root, text="Guess the number \n speak 101 for hint ", bg="lemon chiffon", fg="purple4")
        audio = r.listen(source)
        e1 = r.recognize_google(audio)
        Label(root, text=f"Your number {e1}", bg="lemon chiffon", fg="purple4").grid(row=1, column=1)
        b1 = Button(root, width=10, text="Guess", command=working, fg="dark turquoise", bg="LightCyan2")
        l1.grid(row=0, column=1)
        b1.grid(row=4, column=1)

        mainloop()
except sr.UnknownValueError:
    print("Could not recognize")
except sr.RequestError:
    print("Network Error")
except sr.WaitTimeoutError:
    print("Took too long")
