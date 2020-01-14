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

def definelocale():
    langavaliable = os.listdir("locale")
    langavaliable = [sub.replace('.txt', '') for sub in langavaliable]
    print("Languages avaliable:")
    for i in langavaliable:
        print("*", i)
    global locale
    global localefile
    locale=str(input("Please choose a language (case-sensitive): "))
    if locale in langavaliable:
        print("Defined language: ", locale)
        print("Continuing...")
        localefile = "locale/"
        localefile += locale
        localefile += ".txt"
    else:
        print("\n[!] Language not found. Please type again.\n")
        definelocale()

def lang(line, script):
    mylines = []
    mylines = np.loadtxt(localefile, comments="#", delimiter=";", unpack=False, dtype=str)
    if script == 1:
        n=eval(mylines[line])
        return(n)
    else:
        return(mylines[line])

def arraytostring(chosen):
    b=''
    for x in chosen:
        b = b + str(x) + ' '
    return (b)

def store(chosen, rq, t, choice, particlenumarray):
    print("\nStoring information about t = {} in the table...".format(t))
    #funcao do eixo x: f(x) = 2x + 3
    xaxis = 3+(2*t)
    if t > 1:
        namet="Charge in t="
        namet+=str(t)
        namef="Friction in t="
        namef+=str(t)
        xaxis2=int(xaxis)
        xaxis3=int((xaxis-1))
        value="NaN"
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
    print("Do you want to save this table as table_t{}.csv ?".format(t))
    choice2=str(input("Press Y or N (Y for Yes, N for No): "))
    if choice2 == "Y" or choice2 == 'y':
        print("Saving...")
        nametable="table_t"
        nametable+=str(t)
        nametable+=".csv"
        with open(nametable, 'w') as csv_file:
            df1.to_csv(path_or_buf=csv_file)
    else:
        print("Okay.")
        pass
    if choice == 'Y' or choice == 'y':
        t = int(t + 1)
        choose(particles, df1, t)
    else:
        pass

def colide(chosen, t, particlenumarray):
    print(clear)
    print("Particles selected at the instant t = {}: {}".format(t, chosen))
    print("Rubbing...")
    charges = float(0)
    listsize = len(chosen)
    for x in range(listsize):
        y = int((chosen[x]))
        value = float(dfavaliable.at[y, 'Charge'])
        charges = charges + float(value)
        #debug:#print("Actual value dfavaliable.at[y, 'Charge']: ", value)
        #debug:#print("Sum of charges(debug): ", charges)
    print("Sum of charges: ", charges)
    if listsize !=0:
        rq = float((charges / listsize))
    else:
        rq = int(0)
    print("Resultant charge: {}/{} = {}".format(charges, listsize, rq))
    print("Do you want to continue simulation?")
    choice=str(input("Press Y or N (Y for Yes, N for No): "))
    store(chosen, rq, t, choice, particlenumarray)

def choose(particles, df1, t):
    del avaliablearray[:]
    del particlenumarray[:]
    del chosen[:]
    print(clear)
    xaxis=int(1+(2*t))
    #debug:#print("x axis: {}".format(xaxis))
    print("Please choose the particles to friction on the time instant t =",t)
    if t == 0:
        for x in np.arange(1, particles+1):
            x=int(x)
            dfavaliable.loc[x, 'Particle number'] = x
            avaliablearray.append(x)
            dfavaliable.loc[x, 'Charge'] = df1.loc[x, 'Initial charge']

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
            dfavaliable.at[y, 'Particle number'] = y
            avaliablearray.append(y)
            #debug:#print("y: {}, x: {} ".format(y, xaxis))
            value = float(df1.iloc[[yindex], [xaxis]].values[0])
            #debug:#print("value: {}".format(value))
            dfavaliable.loc[y, 'Charge'] = value
    print(dfavaliable)
    a=''
    while a != '0':
        print("\n")
        print("Particles selected: ", chosen)
        print("Particles avaliable: ", avaliablearray)
        print('Type 0 at any moment to stop.')
        a=input("Select particles to friction: ")
        if a != '0':
            c = int(a)
            if c in avaliablearray:
                if (c in chosen):
                    print("\n[!] The particle {} has already been chosen. ".format(c))
                else:
                    chosen.append(c)
                    avaliablearray.remove(c)
            else:
                print("\n[!] The particle {} doesn't exist.".format(c))
    colide(chosen, t, particlenumarray)

definelocale()
print(clear)
print("-------------------------------------------------------------------------------")
print(lang(0,0))
particles=int(input(lang(1,1)))
print(lang(2,1).format(particles))
print("-------------------------------------------------------------------------------")
df1 = pd.DataFrame(index=np.arange(1, particles+1), columns=('Particle number', 'Initial charge', 'Friction', 'Charge in t=0', 'Friction in t=0','Charge in t=1') )
dfavaliable = pd.DataFrame(index=np.arange(1, particles+1), columns=('Particle number', 'Charge'))

for x in np.arange(1, particles+1):
    df1.loc[x, 'Particle number'] = x

for y in np.arange(1, particles+1):
    charge=input('Type the value of the initial charge of the particle {} in Coulombs (C): '.format(y))
    df1.loc[y, 'Initial charge'] = float(charge)
print(df1)
choose(particles, df1, t)