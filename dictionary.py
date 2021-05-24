#!/usr/bin/env python3
#module for creating desktop app
import tkinter as tk

#module for English Dictionary
from PyDictionary import PyDictionary
dictionary = PyDictionary()

# this function makes the button_meaning interactive
def meaning():
  part_of_speach_vowel = ["Adverb", "Adjective", "Interjection"]
  get_word = ent_word.get()
  word_meaning =  PyDictionary.meaning(get_word, disable_errors=True)
  if word_meaning == None:
    word_format = "word does not exist."
  else:
    dc = []
    for i, k in word_meaning.items():
      if i in part_of_speach_vowel:
        word_format = "Word is an {}{}Meaning: {}{}".format(i,"\n",'  '.join(k), "\n\n")
        dc.append(word_format)
      else:
        word_format = "Word is a {}{}Meaning: {}{}".format(i,"\n",'  '.join(k), "\n\n")
        dc.append(word_format)
    word_format = "".join(dc)
  txt_dic.insert("1.0", word_format)

# this function makes the button_synonym interactive
def synonym():
  get_word = ent_word.get()
  word_synonym =  PyDictionary.synonym(get_word)
  if word_synonym == None:
    word_format = "word does not exit."
  else:
    word_format = "{}".format("\n".join(word_synonym))
  txt_dic.delete("1.0", "end")
  txt_dic.insert("1.0", word_format)

# this function makes the button_antonym interactive
def antonym():
  get_word = ent_word.get()
  word_antonym =  PyDictionary.antonym(get_word)
  if word_antonym == None:
    word_format = "word does not exit."
  else:
    word_format = "{}".format("\n".join(word_antonym))
  txt_dic.delete("1.0", "end")
  txt_dic.insert("1.0", word_format)


window = tk.Tk()
window.title("English Dictionary")

window.rowconfigure(0, minsize=950, weight=1)
window.columnconfigure(2, minsize=950, weight=1)

txt_dic = tk.Text(window)
fr_word = tk.Frame(window) #this frame holds lbl_word label and ent_word Entry
lbl_word = tk.Label(fr_word, text="Word", fg="red", bg="black")
ent_word = tk.Entry(fr_word)
fr_button = tk.Frame(window) #this frame holds all the button.
button_meaning = tk.Button(fr_button, text="Meaning", command=meaning, fg="green")
button_synonym = tk.Button(fr_button, text="Synonym", command=synonym, fg="green")
button_antonym = tk.Button(fr_button, text="Antonym", command=antonym, fg="green")
lbl_word.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
ent_word.grid(row=1, column=0, sticky="ew", padx=5)
ent_word.focus()
button_meaning.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button_synonym.grid(row=1, column=0, sticky="ew", padx=5)
button_antonym.grid(row=2, column=0, sticky="ew", padx=5)
fr_word.grid(row=0, column=0, sticky="ns")
fr_button.grid(row=0, column=1, sticky="ns")
txt_dic.grid(row=0, column=2, sticky="nsew")

window.mainloop()
