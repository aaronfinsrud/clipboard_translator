Windows users can download autohotkey to launch
this clipboard_translator.pyw with a keyboard shortcut
###
## Instructions:
1) Save clipboard_translator.pyw and glossary.csv to C:\Python\keyboardScripts
###
2) Download and install autohotkey:
     https://www.autohotkey.com/docs/Tutorial.htm#s11
###
3) Open C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
   and right-click to create clipboard_translator.ahk file
###
4) Copy the 4 lines of code below into clipboard_translator.ahk

; Clipboard_Translator # Script Name
^!t:: # <ctrl + alt + t > keystroke combination
Run clipboard_translator.pyw, C:\Python\keyboardScripts\ # directory of .pyw application
return

###
5) Save and double-click the .ahk file to make sure it's running
###
6) Select and copy the text you want to translate
###
7) Press < ctrl + alt + t > to translate the copied text
###
8) Press < ctrl + v > to paste translated text from clipboard!
###
