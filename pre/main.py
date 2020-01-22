import pandas as pd
import numpy as np
import os
t=int(0)
clear = "\n" * 100
avaliablearray = []
particlenumarray = []
chosen = []
locale=''
localefile="locale/"
localefile+=locale
localefile+=".txt"
internalfile="locale/internal/"

def localeinternal(locale):
    global internalfile
    internalfile = "locale/internal/"
    internalfile += locale
    internalfile += ".txt"

def internal(line, script):
    linesinternal = []
    with open(internalfile) as f:
        linesinternal = f.read().splitlines()
    if script == 1:
        m = eval(linesinternal[line])
        return (m)
    else:
        return (linesinternal[line])

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
    locale = str(input("Please choose a language (case-sensitive): "))
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
        n = eval(localelines[line])
        return (n)
    else:
        return (localelines[line])

def arraytostring(chosen):
    b=''
    for x in chosen:
        b = b + str(x) + ' '
    return (b)

def storedecision():
    choice2 = str(input(lang(19,1)))
    if choice2 == lang(20,1) or choice2 == lang(21,1):
        print(lang(22,1))
        nametable=internal(7,1)
        nametable+=str(t)
        nametable+=".csv"
        with open(nametable, 'w') as csv_file:
            df1.to_csv(path_or_buf=csv_file)
    elif choice2 == lang(26,1) or choice2 == lang(27,1):
        print(lang(23,1))
    else:
        print(lang(28,1))
        storedecision()

def store(chosen, rq, t, choice, particlenumarray):
    print(lang(17,1).format(t))
    #funcao do eixo x: f(x) = 2x + 3
    xaxis = 3+(2*t)
    if t > 1:
        namet=internal(10,1)
        namet+=str(t)
        namef=internal(9,1)
        namef+=str(t)
        xaxis2=int(xaxis)
        xaxis3=int((xaxis-1))
        value=internal(8,1)
        df1.insert(xaxis3, namef, value) #insert friction column
        df1.insert(xaxis2, namet, value) #insert time column
        print(df1)
    listsize = len(chosen)
    listsize2 = int(0)
    indexzero=int(0)
    xaxisf = int((xaxis-1))
    xaxisminust= int((xaxis-2))
    xaxisincharge=int(1)
    storearray=arraytostring(chosen)
    df1.iloc[[indexzero], [xaxisf]] = storearray
    for i in range(listsize):
        particlenumber=int(chosen[i])
        index=int((particlenumber-1))
        df1.iloc[[index], [xaxis]] = float(rq)
        particlenumarray.remove(particlenumber)
        listsize2 = int(len(particlenumarray))
    if t != 0:
    #em caso de t ser diferente de zero, fazer aqui uma estrutura que substitui
    #os valores nao definidos de cargas na coluna t=x para os valores das cargas na coluna t=x-1
    #debug:#print("particlenumarray: ",particlenumarray)
    #debug:#print("listsize2: ", listsize2)
    # debug:#print("t diferente de zero")
        for i in range(listsize2):
            #debug:#print("i:", i)
            particlenumber=int(particlenumarray[i])
            index=int((particlenumber-1))
            oldvalue = df1.iloc[[index], [xaxisminust]].values[0]
            df1.iloc[[index], [xaxis]] = oldvalue
    else:
    # em caso de t ser igual a zero, fazer aqui uma estrutura que substitui
    # os valores nao definidos de cargas na coluna t=0 para os valores das cargas na coluna de cargas iniciais
        #debug: print("particlenumarray: ",particlenumarray)
        #debug:#print("t igual a 0")
        #debug:#print("listsize2: ", listsize2)
        for i in range(listsize2):
            #debug:#print("i: ", i)
            particlenumber=int(particlenumarray[i])
            #debug:#print ("particlenumber: ",particlenumber)
            index=int(particlenumber-1)
            oldvalue = df1.iloc[[index], [xaxisincharge]].values[0]
            df1.iloc[[index], [xaxis]] = oldvalue
    print(df1)
    print(lang(18,1).format(t))
    storedecision()
    if choice == lang(20,1) or choice == lang(21,1):
        t = int(t + 1)
        choose(particles, df1, t)
    else:
        pass

def colidedecision(chosen, rq, t, particlenumarray):
    choice=str(input(lang(16,1)))
    if choice == lang(20,1) or choice == lang(21,1) or choice == lang(26,1) or choice == lang(27,1):
        store(chosen, rq, t, choice, particlenumarray)
    else:
        print(lang(28,1))
        colidedecision(chosen, rq, t, particlenumarray)

def colide(chosen, t, particlenumarray):
    print(clear)
    print(lang(11,1).format(t, chosen))
    print(lang(12,1))
    print(lang(25,1))
    charges = float(0)
    listsize = len(chosen)
    for x in range(listsize):
        y = int((chosen[x]))
        value = float(dfavaliable.at[y, internal(6,1)])
        charges = charges + float(value)
        #debug:#print("Actual value dfavaliable.at[y, 'Charge']: ", value)
        #debug:#print("Sum of charges(debug): ", charges)
    print(lang(13,1).format(charges))
    if listsize !=0:
        rq = float((charges / listsize))
    else:
        rq = int(0)
    print(lang(14,1).format(charges, listsize, rq))
    print(lang(15,1))
    colidedecision(chosen, rq, t, particlenumarray)

def choose(particles, df1, t):
    del avaliablearray[:]
    del particlenumarray[:]
    del chosen[:]
    print(clear)
    xaxis=int(1+(2*t))
    #debug:#print("x axis: {}".format(xaxis))
    print(lang(4,1).format(t))
    if t == 0:
        for x in np.arange(1, particles+1):
            x=int(x)
            dfavaliable.loc[x, internal(0,1)] = x
            avaliablearray.append(x)
            dfavaliable.loc[x, internal(6,1)] = df1.loc[x, internal(1,1)]

            y=int(x)
            #create array with particle numbers
            particlenumarray.append(y)
    else:
        for x in np.arange(1, particles+1):
            y = int(x)
            yindex=int((y-1))

            #create array with fixed particle numbers
            particlenumarray.append(y)

            #transform dataframe particle numbers in editable array
            dfavaliable.at[y, internal(0,1)] = y
            avaliablearray.append(y)
            #debug:#print("y: {}, x: {} ".format(y, xaxis))
            value = float(df1.iloc[[yindex], [xaxis]].values[0])
            #debug:#print("value: {}".format(value))
            dfavaliable.loc[y, internal(6,1)] = value
    print(dfavaliable)
    a=''
    while a != '0':
        print("\n")
        print(lang(5,1).format(chosen))
        print(lang(6,1).format(avaliablearray))
        print(lang(7,1))
        a=input(lang(8,1))
        if a != '0':
            c = int(a)
            if c in avaliablearray or c in chosen:
                if (c in chosen):
                    print(lang(9,1).format(c))
                else:
                    chosen.append(c)
                    avaliablearray.remove(c)
            else:
                print(lang(10,1).format(c))
    colide(chosen, t, particlenumarray)

definelocale()
print(clear)
print(lang(24,1))
print(lang(0,1))
particles=int(input(lang(1,1)))
print(lang(2,1).format(particles))
print(lang(24,1))
df1 = pd.DataFrame(index=np.arange(1, particles+1), columns=(internal(0,1), internal(1,1), internal(2,1), internal(3,1), internal(4,1),internal(5,1)))
dfavaliable = pd.DataFrame(index=np.arange(1, particles+1), columns=(internal(0,1), internal(6,1)))

for x in np.arange(1, particles+1):
    df1.loc[x, internal(0,1)] = x

for y in np.arange(1, particles+1):
    charge=input(lang(3,1).format(y))
    df1.loc[y, internal(1,1)] = float(charge)
print(df1)
choose(particles, df1, t)