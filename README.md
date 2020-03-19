## Dependencies:
1. pandas
2. googletrans 
3. pyperclip
4. python 3.8

Windows users can download autohotkey to launch
this clipboard_translator.pyw with a keyboard shortcut
###
## Instructions:
1) Save clipboard_translator.pyw and glossary.csv to C:\Python\keyboardScripts
###
2) Download and install autohotkey:
     https://www.autohotkey.com/docs/Tutorial.htm#s11
###
3) Go to your desktop and right-click to create an .ahk file named clipboard_translator.ahk file 
     (right-click -> New -> AutoHotKey Script)
###
4) Open the .ahk using notepad (right-click -> Edit Script) and replace the existing code with the 4 lines of code below:


       ; Clipboard_Translator

       ^!t:: 

       Run clipboard_translator.pyw, C:\Python\keyboardScripts\

       return


###
5) Save and double-click the .ahk file to make sure it's running
###
6) Move the .ahk file to C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup 
###
7) Select and copy the text you want to translate
###
8) Press < ctrl + alt + t > to translate the copied text
###
9) Press < ctrl + v > to paste translated text from clipboard!
###
