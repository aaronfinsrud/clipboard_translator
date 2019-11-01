## Windows users can download autohotkey to launch
## this clipboard_translator.pyw using keyboard shortcut
###
## Instructions:
## 1) Save to C:\Python\keyboardScripts
###
## 2) Download autohotkey:
##      https://www.autohotkey.com/docs/Tutorial.htm#s11
###
## 3) Open C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
##    and right-click to create clipboard_translator.ahk file
###
## 4) Copy the 4 lines of code below into clipboard_translator.ahk
## ; SCRIPT NAME 
## ^!t::
## Run clipboard_translator.pyw, C:\Python\keyboardScripts\
## return
###
## 5) Save and double-click the .ahk file to make sure it's running
###
## 6) Select and copy text to translate
###
## 7) Press < ctrl + alt + t > to translate the copied text
###
## 8) Press < ctrl + v > to paste translated text from clipboard
###
# -*- coding: utf-8 -*-
# import dependencies
import os
import pandas
from googletrans import Translator
import pyperclip
import re

#import glossary.csv
cwd = os.getcwd()
glossary_abs_dir = os.path.join(cwd, "glossary.csv")
#convert glossary.csv columns to lists
glossary = pandas.read_csv(glossary_abs_dir, names=['ZH','EN'])
# establish translator function
translator = Translator()
# take clipboard as input_text
input_text = pyperclip.paste()
# detect input language
detected = translator.detect(input_text)
# if input lang == en 
if detected.lang == "en":
    # iterator to check input for matches with glossary.EN
    i = 0
    length = len(glossary.EN)
    while i < length:
        term_EN = glossary.EN[i]
        term_ZH = glossary.ZH[i]
        # find each occurence of term_EN
        ##delete "flags=re.IGNORECASE" to turn on case sensitivity##
        parts = re.split(term_EN, input_text, flags=re.IGNORECASE)
        # replace matches w/ term_ZH
        input_text = term_ZH.join(parts)
        i += 1   
    #translate modified input to EN
    output = translator.translate(input_text, src="en", dest="zh-CN")
    output = output.text
# if input lang == zh-CN
if detected.lang == "zh-CN":
    # iterator to check input for matches with glossary.EN
    i = 0
    length = len(glossary.ZH)
    while i < length:
        term_EN = glossary.EN[i]
        term_ZH = glossary.ZH[i]
        # find each occurence of term_ZH
        parts = input_text.split(term_ZH)
        # replace matches w/ term_ZH
        input_text = term_EN.join(parts) 
        i += 1
    #translate modified input to EN
    output = translator.translate(input_text, src="zh-CN", dest="en")
    output = output.text
# copy output to clipboard
pyperclip.copy(output)





