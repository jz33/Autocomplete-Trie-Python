# Trie-Autocomplete-Python-TTK
A string autocomplete implementation based on Trie data structure on python-ttk UI compents

## Usage

Put all files in same directory, then

    python Controller.py
    
When the dialog appear, click

    import
    
This will load 1 of the 2 test files. 

    words_109582.txt # 109582 words, 1.2 MB
    words_598153.txt # 598153 words, 7.5 MB

Default is the 2nd. This might take 10s.

Then type in words in text field, press enter will produce all completers.

Input of 'head' results all words with prefix of 'head':

    headline
    headling

Click 

    Prefix Only
    
will switch mode to "Prefix and Infix". 

Input of 'head' results all word contains 'head':

    headline
    headling
    skinhead
