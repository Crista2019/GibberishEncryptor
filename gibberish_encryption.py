# import the 'tkinter' module
try:
    import Tkinter as tkinter
    from Tkinter import font
except ImportError:  # Python 3
    import tkinter
    from tkinter import font

# http://usingpython.com/python-widgets/

# create a new window
window = tkinter.Tk()

# defining data structures and variables
output = "Your Message Will Appear Here..."
textArray = []
vowels = ['a', 'e', 'i', 'o', 'u']
gibConsonants = ["t", "p", "d", "f", "chi"]
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# defining functions
def getEntryData():
    textArray = []
    rawText = inputEntry.get().lower()
    # cuts phrases into words stored in an array: ["one", "word", "at", "a", "time"]
    if len(rawText) > 0:
        words = rawText.split( )
        return words
    else:
        return ["Please", "type", "a", "message"]

def pigLatin():
    translatedArray = []
    text = getEntryData()
    for word in text:
        firstLetter = word[0]
        if firstLetter not in vowels:
            addWord = word[1:] + " " + firstLetter + "ay"
        else:
            addWord = word
        translatedArray.append(addWord)
    finalTranslation = " ".join(str(x) for x in translatedArray)
    showMessage(finalTranslation)

def compressed():
    translatedArray = []
    text = getEntryData()
    for word in text:
        for letter in word:
            if letter == word[0]:
                pass
            elif letter in vowels:
                word = word.replace(letter, "")
        translatedArray.append(word)
    finalTranslation = " ".join(str(x) for x in translatedArray)
    showMessage(finalTranslation)

def gibberish():
    translatedArray = []
    text = getEntryData()
    for word in text:
        for letter in word:
            if letter in vowels:
                word = word.replace(letter, letter + 'p' + letter)
        translatedArray.append(word)
    finalTranslation = " ".join(str(x) for x in translatedArray)
    showMessage(finalTranslation)

def verlan():
    translatedString = ""
    text = " ".join(str(x) for x in getEntryData())
    for i in text:
         translatedString = i + translatedString
    showMessage(translatedString)

def showMessage(newOutput):
    message = newOutput[0].upper() + newOutput[1:]
    translatedMsg.configure(text=message)

def display():
    # window title
    window.title("Translator")
    # resizing: width x height + x_offset + y_offset:
    window.geometry("900x620+30+30")
    # window.wm_iconbitmap("phone.ico")
    window.configure(background="#542344")
    # custom fonts
    instructionsFont = font.Font(family='Times', size=8)
    inputFont = font.Font(family='Helvetica', size=11)
    btnFont = font.Font(family='Courier', size=10, weight='bold')
    outputFont = font.Font(family='Helvetica', size=11, weight='bold')

# Widgets: essentially elements in the window

# Title
title = tkinter.Label(window, text="BSU Computer Science Principles\nCrista Falk\n 5/2018", fg="#EBF5EE", bg="#653455", font="outputFont")
title.place(relwidth = 0.5, relheight = 0.2, relx = 0.25, rely = 0.1)

# User input: message
inputEntry = tkinter.Entry(window, fg="#542344", font="inputFont")
inputEntry.place(relwidth = 0.4, relheight = 0.06, relx = 0.3, rely = 0.35)

# Adding "p" in the middle of vowels: "a" => "apa"
verlanBtn = tkinter.Button(window, text="Verlan", bg="#DAE4DD", command=verlan, font="btnFont")
verlanBtn.place(relwidth = 0.14, relheight = 0.08, relx = 0.44, rely = 0.45)

# First letter is put after each word with the suffix "-ay"
pigLatinBtn = tkinter.Button(window, text="Pig Latin", bg="#DAE4DD", command=pigLatin, font="btnFont")
pigLatinBtn.place(relwidth = 0.14, relheight = 0.08, relx = 0.44, rely = 0.55)

# All vowels except first letter are removed (text still readable)
compressedBtn = tkinter.Button(window, text="Compressed", bg="#DAE4DD", command=compressed, font="btnFont")
compressedBtn.place(relwidth = 0.14, relheight = 0.08, relx = 0.44, rely = 0.65)

# Adding "p" in the middle of vowels: "a" => "apa"
gibberishBtn = tkinter.Button(window, text="Jeringonza", bg="#DAE4DD", command=gibberish, font="btnFont")
gibberishBtn.place(relwidth = 0.14, relheight = 0.08, relx = 0.44, rely = 0.75)

# Output: changed message
translatedMsg = tkinter.Label(window, text=output, fg="#EBF5EE", bg="#653455", font="outputFont",)
translatedMsg.place(relwidth = 0.8, relheight = 0.1, relx = 0.1, rely = 0.85)

display()
# draw the window and begin application
window.mainloop()
