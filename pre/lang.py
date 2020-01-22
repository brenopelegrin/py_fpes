import os
locale=''
localefile="locale/"
localefile+=locale
localefile+=".txt"
internalfile="locale/internal/"

def localeinternal(locale):
    global internalfile
    internalfile="locale/internal/"
    internalfile+=locale
    internalfile+=".txt"

def internal(line, script):
    linesinternal = []
    with open(internalfile) as f:
        linesinternal = f.read().splitlines()
    if script == 1:
        m=eval(linesinternal[line])
        return(m)
    else:
        return(linesinternal[line])

def definelocale():
    langavaliable = []
    with os.scandir("locale") as listOfEntries:
        for entry in listOfEntries:
            if entry.is_file():
                langavaliable.append(entry.name)
    langavaliable = [sub.replace('.txt', '') for sub in langavaliable]
    print("Languages avaliable:")
    for i in langavaliable:
        print("*", i)
    global locale
    global localefile
    locale=str(input("Please choose a language (case-sensitive): "))
    if locale in langavaliable:
        print("Selected language: ", locale)
        print("Continuing...")
        localefile = "locale/"
        localefile += locale
        localefile += ".txt"
        localeinternal(locale)
    else:
        print("\n[!] Language not found. Please type again.\n")
        definelocale()

def lang(line, script):
    localelines = []
    with open(localefile) as f:
        localelines = f.read().splitlines()
    if script == 1:
        n=eval(localelines[line])
        return(n)
    else:
        return(localelines[line])