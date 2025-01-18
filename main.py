from tkinter import *
from tkinter import messagebox

def translate(languages,entry):
    word = entry.get()
    lang = language.get()
    translation = dictionary.get(lang, {}).get(word)
    messagebox.showinfo("Result" , f"{word.capitalize()} : {translation}")
dictionary = {
        "Yoruba":  {"wa": "come", "iwo": "you", "oruko": "name",  "omo": "child", "ile": "house",
    "oloye": "king",  "agbara": "strength", "omolode": "beautiful",  "eniyan": "person", "oko": "husband",
    "iyawo": "wife", "ounje": "food","omi": "water", "orun": "heaven", "aye": "earth", "okan": "heart", "owo": "hand",
    "oko": "farm", "ojo": "day", "orun": "sleep"
}
}

window = Tk()
window.title("Language Dictionary")

languages = ["Yoruba"]
language = StringVar(window)
language.set("Pick a Language")
language_menu = OptionMenu(window, language, *languages)
language_menu.pack()

words_label = Label(window, text="Enter Word:")
words_label.pack()

entry = Entry(window)
entry.pack(pady=10)

translate_button = Button(window, text="Translate",  command=lambda: translate(languages, entry))
translate_button.pack()

result_label = Label(window, text="")
result_label.pack()

window.mainloop()

