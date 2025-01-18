from tkinter import *
from tkinter import messagebox

def translate(languages,entry):
    word = entry.get()
    lang = language.get()
    translation = dictionary.get(lang, {}).get(word,"Word not found")
    messagebox.showinfo("Result" , f"{word.capitalize()} : {translation}")
dictionary = {
        "Yoruba":  {"wa": "come", "iwo": "you", "oruko": "name",  "omo": "child", "ile": "house",
    "oloye": "king",  "agbara": "strength", "omolode": "beautiful",  "eniyan": "person", "oko": "husband",
    "iyawo": "wife", "ounje": "food","omi": "water", "orun": "heaven", "aye": "earth", "okan": "heart", "owo": "hand",
    "oko": "farm", "ojo": "day", "orun": "sleep"
                    }, "Igbo": {
                        "aga m": "I am going", "ebe a": "Here", "ebe ahu": "There",
    "ee": "Yes", "mba": "No", "aha m bu": "My name is", "kedu aha gi?": "What is your name?", "nri": "Food",
    "mmiri": "Water", "ulo": "House", "nwoke": "Man/Male", "ndewo": "Hello", "daalu": "Thank you", "biko": "Please", "ezigbo ututu": "Good morning",
    "ezigbo ehihie": "Good afternoon", "ezigbo mgbede": "Good evening", "Ka o di": "How are you?",
    "o di mma": "I am fine", "bia": "come" }, "Spanish": { 
   "bueno": "good", "malo": "bad", "perro": "dog", "amor": "love", "gate": "cat", "feliz": "happy", "cielo": "heaven", "traducir": "translate", "fuego": "fire", "hola": "hello", "gracias": "thank you", "adios": "goodbye", "si": "yes"}
}

window = Tk()
window.title("Language Dictionary")

languages = ["Spanish","Yoruba","Igbo"]
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

