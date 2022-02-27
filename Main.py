import csv
import random
from tkinter import *
from tkinter import messagebox as ms
import time
from functools import partial
import tkinter
from PIL import Image, ImageTk
from os.path import exists
from Class import *
import copy 

def ClosePreviousWindow():
    try:
        LoginWindow.destroy()
    except:
        pass
    try:
        RegisterWindow.destroy()
    except:
        pass
    try:
        CharacterSelectionWindow.destroy()
    except:
        pass
    try:
        InitialWindow.destroy()
    except:
        pass
    try:
        GamemodeWindow.destroy()
    except:
        pass
    try:
        DetailsWindow.destroy()
    except:
        pass
    try:
        FightWindow.destroy()
    except:
        pass

def SetupWindow(tkInstance,size,title,bgcolor,icon):
    tkInstance.geometry(size)
    tkInstance.title(title) # editar el titulo
    tkInstance.config(bg=bgcolor) # editar el background
    tkInstance.iconbitmap(icon) # editar el icono de la aplicacion

def OpenInitialWindow():
    global InitialWindow
    InitialWindow = Tk() # instanciar
    SetupWindow(InitialWindow,"400x300","La Guerra De Los Mejores","#C1B9B9","images/VamohIcon.ico")

    LoginButton = Button(InitialWindow, text="Iniciar sesión", command=OpenLoginWindow)
    LoginButton.place(relx=0.5,rely=0.4,anchor=CENTER)

    RegisterButton = Button(InitialWindow, text="Usuario nuevo", command=OpenRegisterWindow)
    RegisterButton.place(relx=0.5,rely=0.6,anchor=CENTER)

    Label(InitialWindow, text="La Guerra De Los Mejores",bg="#C1B9B9",font=("Arial",14)).place(relx=0.5,rely=0.1,anchor=CENTER)

    InitialWindow.mainloop()


def OpenLoginWindow():
    ClosePreviousWindow()
    global LoginWindow
    LoginWindow = Tk() # instanciar
    SetupWindow(LoginWindow,"400x300","La Guerra De Los Mejores","#C1B9B9","images/VamohIcon.ico")

    Label(LoginWindow, text="Identifícate",bg="#C1B9B9").place(relx=0.5,rely=0.1,anchor=CENTER)

    Label(LoginWindow, text="Usuario",bg="#C1B9B9").place(relx=0.5,rely=0.3,anchor=CENTER)

    UsernameTextBox = Entry(LoginWindow)
    UsernameTextBox.place(relx=0.5,rely=0.4,anchor=CENTER)

    Label(LoginWindow, text="Contraseña",bg="#C1B9B9").place(relx=0.5,rely=0.6,anchor=CENTER)

    PasswordTextBox = Entry(LoginWindow,show="*")
    PasswordTextBox.place(relx=0.5,rely=0.7,anchor=CENTER)

    StartButton = Button(LoginWindow, text="Iniciar", command=partial(LoginValidation,UsernameTextBox,PasswordTextBox))
    StartButton.place(relx=0.5,rely=0.9,anchor=CENTER)

    LoginWindow.mainloop()

def OpenRegisterWindow():
    ClosePreviousWindow()
    global RegisterWindow
    RegisterWindow = Tk() # instanciar
    SetupWindow(RegisterWindow,"400x300","La Guerra De Los Mejores","#C1B9B9","images/VamohIcon.ico")

    Label(RegisterWindow, text="Regístrate",bg="#C1B9B9").place(relx=0.5,rely=0.1,anchor=CENTER)

    Label(RegisterWindow, text="Usuario",bg="#C1B9B9").place(relx=0.5,rely=0.2,anchor=CENTER)

    UsernameTextBox = Entry(RegisterWindow)
    UsernameTextBox.place(relx=0.5,rely=0.3,anchor=CENTER)

    Label(RegisterWindow, text="Contraseña",bg="#C1B9B9").place(relx=0.5,rely=0.4,anchor=CENTER)

    PasswordTextBox = Entry(RegisterWindow,show="*")
    PasswordTextBox.place(relx=0.5,rely=0.5,anchor=CENTER)

    Label(RegisterWindow, text="Confirmar contraseña",bg="#C1B9B9").place(relx=0.5,rely=0.6,anchor=CENTER)

    RePasswordTextBox = Entry(RegisterWindow,show="*")
    RePasswordTextBox.place(relx=0.5,rely=0.7,anchor=CENTER)

    RegisterButton = Button(RegisterWindow, text="Registrar", command=partial(RegisterValidation,UsernameTextBox,PasswordTextBox,RePasswordTextBox))
    RegisterButton.place(relx=0.5,rely=0.9,anchor=CENTER)

    RegisterWindow.mainloop()

def OpenGamemodeWindow():
    ClosePreviousWindow()
    global GamemodeWindow
    GamemodeWindow = Tk() # instanciar
    SetupWindow(GamemodeWindow,"500x300","La Guerra De Los Mejores. Selecciona el modo de juego","#C1B9B9","images/VamohIcon.ico")

    Button(GamemodeWindow, text="Modo entrenamiento", command=partial(OpenCharacterSelectionWindow,False),height=5,width=20).place(relx=0.5,rely=0.3,anchor=CENTER)

    Button(GamemodeWindow, text="Modo historia", command=partial(checkProgress,True),height=5,width=20).place(relx=0.5,rely=0.7,anchor=CENTER)

def OpenCharacterSelectionWindow(isHistoryMode):
    ClosePreviousWindow()
    global CharacterSelectionWindow
    CharacterSelectionWindow = Tk() # instanciar
    CharacterSelectionWindow.geometry("400x400") # alterar el tamanio
    CharacterSelectionWindow.config(bg="#C1B9B9") # editar el background
    CharacterSelectionWindow.iconbitmap("images/VamohIcon.ico") # editar el icono de la aplicacion
    if isHistoryMode:
        CharacterSelectionWindow.title("La Guerra De Los Mejores. Selecciona tu personaje") # editar el titulo
    else:
        CharacterSelectionWindow.title("La Guerra De Los Mejores. Selecciona tu personaje y a tu oponente") # editar el titulo

    global characters
    characters = initCharacters()
    Dir ="images/"
    Im1 = Image.open(Dir + "aquarder.png")
    Im2 = Image.open(Dir + "electder.png")
    Im3 = Image.open(Dir + "firesor.png")
    Im4 = Image.open(Dir + "mousebug.png")
    Im5 = Image.open(Dir + "splant.png")
    Im6 = Image.open(Dir + "rockdog.png")

    newsize = (100,100)
    Im_1 = Im1.resize(newsize)
    Im_2 = Im2.resize(newsize)
    Im_3 = Im3.resize(newsize)
    Im_4 = Im4.resize(newsize)
    Im_5 = Im5.resize(newsize)
    Im_6 = Im6.resize(newsize)

    im1 = ImageTk.PhotoImage(Im_1)
    im2 = ImageTk.PhotoImage(Im_2)
    im3 = ImageTk.PhotoImage(Im_3)
    im4 = ImageTk.PhotoImage(Im_4)
    im5 = ImageTk.PhotoImage(Im_5)
    im6 = ImageTk.PhotoImage(Im_6)
    
    cuantityList = [0,0,0,0,0,0]
    charactersToFight = []

    for i in range(3):
        Label(CharacterSelectionWindow,text=characters[i].name,bg="#C1B9B9").grid(row=0,column=i)

    Character1Button = Button(CharacterSelectionWindow,image=im1,command=partial(SelectCharacter,cuantityList,0,isHistoryMode,charactersToFight))
    Character1Button.grid(row=1,column=0) #ipadx para acomodar tamaños
    Character2Button = Button(CharacterSelectionWindow,image=im2,command=partial(SelectCharacter,cuantityList,1,isHistoryMode,charactersToFight))
    Character2Button.grid(row=1,column=1)
    Character3Button = Button(CharacterSelectionWindow,image=im3,command=partial(SelectCharacter,cuantityList,2,isHistoryMode,charactersToFight))
    Character3Button.grid(row=1,column=2)

    for i in range(3):
        Button(CharacterSelectionWindow,text="Detalle",command=partial(OpenDetailsWindow,characters[i])).grid(row=2,column=i)

    for i in range(3):
        Label(CharacterSelectionWindow,text=characters[i+3].name,bg="#C1B9B9").grid(row=3,column=i)

    Character4Button = Button(CharacterSelectionWindow,image=im4,command=partial(SelectCharacter,cuantityList,3,isHistoryMode,charactersToFight))
    Character4Button.grid(row=4,column=0) #ipadx para acomodar tamaños
    Character5Button = Button(CharacterSelectionWindow,image=im5,command=partial(SelectCharacter,cuantityList,4,isHistoryMode,charactersToFight))
    Character5Button.grid(row=4,column=1)
    Character6Button = Button(CharacterSelectionWindow,image=im6,command=partial(SelectCharacter,cuantityList,5,isHistoryMode,charactersToFight))
    Character6Button.grid(row=4,column=2)

    for i in range(3):
        Button(CharacterSelectionWindow,text="Detalle",command=partial(OpenDetailsWindow,characters[i+3])).grid(row=5,column=i)

    global ClearButton
    ClearButton = Button(CharacterSelectionWindow,text="Limpiar selecciones",command=partial(ClearSelections,cuantityList,charactersToFight),state=tkinter.DISABLED)
    ClearButton.grid(row=7,column=2)

    global startFightButton
    startFightButton = Button(CharacterSelectionWindow,text="Iniciar",command=partial(startBattle,charactersToFight,0,isHistoryMode),state=DISABLED)
    startFightButton.grid(row=6,column=1)

    global characterButtons
    characterButtons = [Character1Button,Character2Button,Character3Button,Character4Button,Character5Button,Character6Button]

    Button(CharacterSelectionWindow,text="Volver a selección\nde modos de juego",command=OpenGamemodeWindow).grid(row=7,column=0)

    CharacterSelectionWindow.mainloop()

def OpenDetailsWindow(character):
    global DetailsWindow
    # DetailsWindow = Tk() # instanciar
    DetailsWindow = Toplevel(CharacterSelectionWindow) # instanciar
    SetupWindow(DetailsWindow,"400x400","La Guerra De Los Mejores. Detalles del personaje","#C1B9B9","images/VamohIcon.ico")

    Im1 = Image.open(character.imagePath)
    newsize = (100,100)
    Im_1 = Im1.resize(newsize)
    im1 = ImageTk.PhotoImage(Im_1)

    attacksNames = list(character.attacks)
    attacks = character.attacks

    advantageText = "Ventaja con: " + ", ".join(character.advantage)
    disadvantageText = "Desventaja con: " + ", ".join(character.disadvantage)
    normalText = "Normal con: " + ", ".join(character.normal)

    Label(DetailsWindow,image=im1,bg="#C1B9B9").grid(row=0,column=0, columnspan = 7)
    Label(DetailsWindow,text=character.name + ": Tipo " + character.type,bg="#C1B9B9").grid(row=1,column=0, columnspan = 7)
    Label(DetailsWindow,text=advantageText,bg="#C1B9B9").grid(row=2,column=0, columnspan = 7)
    Label(DetailsWindow,text=disadvantageText,bg="#C1B9B9").grid(row=3,column=0, columnspan = 7)
    Label(DetailsWindow,text=normalText,bg="#C1B9B9").grid(row=4,column=0, columnspan = 7)

    columnNames = ["Habilidad","norm","At vent","At desv","pot norm","pot vent","pot desv"]
    for i in range(7):
        Label(DetailsWindow,text=columnNames[i],bg="#C1B9B9").grid(row=5,column=i,sticky=W)

    for i in range(3):
        Label(DetailsWindow,text=attacksNames[i],bg="#C1B9B9").grid(row=i+6,column=0,sticky=W)

    Label(DetailsWindow,text=character.powerUpName,bg="#C1B9B9").grid(row=9,column=0,sticky=W)

    #Daños de ataques
    for i in range(6):
        Label(DetailsWindow,text=str(attacks[attacksNames[0]][i]) + "pt",bg="#C1B9B9").grid(row=6,column=i+1)

    Label(DetailsWindow,text=str(attacks[attacksNames[1]]) + "pt",bg="#C1B9B9").grid(row=7,column=1)
    Label(DetailsWindow,text=str(attacks[attacksNames[2]]) + "pt",bg="#C1B9B9").grid(row=8,column=1)

    Label(DetailsWindow,text="Potenciador de campo, 1 vez cada 3 turnos\n tiene una duración de 2 turnos",bg="#C1B9B9").grid(row=9,column=1, columnspan=6)
    
    DetailsWindow.mainloop()

def SelectCharacter(cuantityList, index, isHistoryMode,charactersToFight):
    cuantityList[index] += 1

    buttonsPressedNeeded = 1 if isHistoryMode else 2

    charactersToFight.append(characters[index])

    if sum(cuantityList) >= buttonsPressedNeeded:
        disableButtons(characterButtons)
        ClearButton.config(state=NORMAL)
        startFightButton.config(state=NORMAL)

    if cuantityList[index] != 1 or sum(cuantityList) > 1:
        characterButtons[index].config(bg="#2596be") #azul cpu
    else:
        characterButtons[index].config(bg="#873e23") #rojo player
        if not isHistoryMode:
            ms.showinfo(message="Elige a tu oponente")

def ClearSelections(cuantityList,charactersToFight):
    for button in characterButtons:
        button.config(state=NORMAL,bg="SystemButtonFace")

    startFightButton.config(state=DISABLED)

    for i in range(len(cuantityList)):
        cuantityList[i] = 0

    ClearButton.config(state=DISABLED)
    charactersToFight.clear()

def OpenFightWindow(charactersToFight,level,isHistoryMode):
    ClosePreviousWindow()
    global FightWindow
    global displayText
    global actualLevel
    actualLevel = level
    FightWindow = Tk() # instanciar
    SetupWindow(FightWindow,"400x300","La Guerra De Los Mejores. Demuestra tu destreza","#C1B9B9","images/VamohIcon.ico")

    displayText = tkinter.StringVar()
    displayText.set("")

    global changeTurn
    changeTurn = tkinter.BooleanVar()
    changeTurn.set(False)

    characters = initCharacters()

    player = charactersToFight[0]
    cpu = characters[actualLevel] if isHistoryMode else copy.copy(charactersToFight[1])

    player.isPlayer = True
    cpu.isPlayer = False

    fightCommentary = Label(FightWindow,textvariable=displayText,bg="#C1B9B9",font=("Arial",12))
    fightCommentary.grid(row=8,column=0,columnspan=7,rowspan=4)

    attackNames = list(player.attacks)

    Attack1Button = Button(FightWindow,text=attackNames[0],command=partial(UseAbility,player,cpu,attackNames[0]),width=12)
    Attack1Button.grid(row=0,column=0,ipadx=20)
    Attack2Button = Button(FightWindow,text=attackNames[1],command=partial(UseAbility,player,cpu,attackNames[1]),width=12)
    Attack2Button.grid(row=1,column=0,ipadx=20)
    Attack3Button = Button(FightWindow,text=attackNames[2],command=partial(UseAbility,player,cpu,attackNames[2]),width=12)
    Attack3Button.grid(row=2,column=0,ipadx=20)

    global powerUpButton
    global attackButtons
    global playerHP
    global cpuHP
    playerHP = tkinter.IntVar()
    playerHP.set(25)

    cpuHP = tkinter.IntVar()
    cpuHP.set(25)

    attackButtons = [Attack1Button,Attack2Button,Attack3Button]

    powerUpButton = Button(FightWindow,text=player.powerUpName,command=partial(activatePowerUp,player),width=12)
    powerUpButton.grid(row=3,column=0,ipadx=20)

    Im1 = Image.open(player.imagePath)
    Im2 = Image.open(cpu.imagePath)

    newsize = (100,100)
    Im_1 = Im1.resize(newsize)
    Im_2 = Im2.resize(newsize)

    im1 = ImageTk.PhotoImage(Im_1)
    im2 = ImageTk.PhotoImage(Im_2)
    
    Label(FightWindow,image=im1,bg="#873e23").grid(row=0,column=1, rowspan=4)
    Label(FightWindow,image=im2,bg="#2596be").grid(row=0,column=2, rowspan=4)
    Label(FightWindow,text=player.name,bg="#C1B9B9",font=("Arial",15)).grid(row=5,column=1)
    Label(FightWindow,text=cpu.name,bg="#C1B9B9",font=("Arial",15)).grid(row=5,column=2)
    Label(FightWindow,text="HP",bg="#C1B9B9",font=("Arial",15)).grid(row=6,column=1)
    Label(FightWindow,text="HP",bg="#C1B9B9",font=("Arial",15)).grid(row=6,column=2)
    Label(FightWindow,textvariable=playerHP,bg="#C1B9B9",font=("Arial",15)).grid(row=7,column=1)
    Label(FightWindow,textvariable=cpuHP,bg="#C1B9B9",font=("Arial",15)).grid(row=7,column=2)

    if isHistoryMode:
        FightWindow.protocol("WM_DELETE_WINDOW", lambda:loseInHistoryMode(player,actualLevel,isHistoryMode,True)) 

    else:
        FightWindow.protocol("WM_DELETE_WINDOW", lambda:loseInTrainingMode(True)) #
        
    StartFight(player,cpu,actualLevel,isHistoryMode)

    FightWindow.mainloop()

def StartFight(player,cpu,level,isHistoryMode):

    global actualLevel
    actualLevel = level
    FightWindow.update_idletasks()

    firstTurnNumber=random.randint(1,2)

    if cpu.isPowerUpAvailable:
        randomAttack = random.randint(0,3)
    else:
        randomAttack = random.randint(0,2)

    cpuAttacksNames = list(cpu.attacks)
 
    if (firstTurnNumber==1):
        displayText.set("Primer movimiento es tuyo\n¡¡Piensa bien!!\n")
        FightWindow.wait_variable(changeTurn)
        FightWindow.update()

        disableButtons(attackButtons)
        powerUpButton.config(state=DISABLED)
        updatePowerUp(player)

        time.sleep(1)

    else:
        displayText.set("Primer movimiento es del CPU\n¡¡Cuidado!!\n")

        disableButtons(attackButtons)
        powerUpButton.config(state=DISABLED)

        FightWindow.update()

        time.sleep(1)

        if randomAttack < 3:
            UseAbility(cpu,player,cpuAttacksNames[randomAttack])
        else:
            activatePowerUp(cpu)

        FightWindow.update()

        updatePowerUp(cpu)

        time.sleep(2)

    powerUpButton.config(state=DISABLED)
 
    while (player.HP > 0 and cpu.HP > 0):
        if cpu.isPowerUpAvailable:
            randomAttack = random.randint(0,3)
        else:
            randomAttack = random.randint(0,2)

        if changeTurn.get():
            changeTurn.set(not changeTurn.get()) 

            displayText.set("Turno del CPU...")

            FightWindow.update()
            
            time.sleep(1)

            if randomAttack < 3:
                UseAbility(cpu,player,cpuAttacksNames[randomAttack])
            else:
                activatePowerUp(cpu)

            FightWindow.update()

            updatePowerUp(cpu)

            time.sleep(2)

        #primer movimiento fue del cpu
        else:
            displayText.set("¡¡¡Tu turno!!!")

            enableButtons(attackButtons)
            if (player.isPowerUpAvailable):
                powerUpButton.config(state=NORMAL)

            FightWindow.wait_variable(changeTurn)
            FightWindow.update()

            updatePowerUp(player)

            time.sleep(1)
    
    winner = True if cpu.HP <= 0 else False

    player.HP = 25
    cpu.HP = 25

    if isHistoryMode:
        if winner:
            ms.showinfo(message="¡Muy bien! Ganaste",title="Combate finalizado")
            actualLevel += 1

            if len(loadedData[1]) == 1:
                loadedData[1].append(player.name)
                loadedData[1].append(actualLevel)
                saveData(loadedData,usernamePath)

            goToNextLevel(player,actualLevel,isHistoryMode)
        else:
            loseInHistoryMode(player,actualLevel,isHistoryMode,False)
    else:
        if winner:
            ms.showinfo(message="¡Eres imparable! regresarás a seleccionar personajes",title="Combate finalizado")
            OpenCharacterSelectionWindow(False)
        else:
            loseInTrainingMode(False)

def checkProgress(isHistoryMode):
    if len(loadedData[1]) == 1:
        OpenCharacterSelectionWindow(isHistoryMode)
    else:
        dictionary = {"Aquarder":0,"Electder":1,"Firesor":2,"Mousebug":3,"Splant":4,"Rockdog":5}
        characters = initCharacters()
        player = characters[dictionary[loadedData[1][1]]]

        OpenFightWindow([player,None],int(loadedData[1][2]),isHistoryMode)
        
def startBattle(charactersToFight,actualLevel,isHistoryMode):
    isReady = ms.askyesno(message="¿Estás listo?\nComenzará un combate legendario",title="No hay vuelta atrás")
    if isReady:
        OpenFightWindow(charactersToFight,actualLevel,isHistoryMode)

def activatePowerUp(character):
    character.activatePowerUp()
    displayText.set(character.name + " ha utilizado " + character.powerUpName +"\nQuedan 2 movimientos")
    if character.isPlayer:
        powerUpButton.config(state=DISABLED)
        changeTurn.set(not changeTurn.get())
        disableButtons(attackButtons)
 
def updatePowerUp(character):
    character.updatePowerUp()

def loseInTrainingMode(isForClose):
    if isForClose:
        ms.showinfo(message="Regresarás a seleccionar personajes",title="Combate cancelado")
    else:
        ms.showinfo(message="Has perdido, pero siempre puedes intentarlo de nuevo\nRegresarás a seleccionar personajes",title="Combate finalizado")

    OpenCharacterSelectionWindow(False)

def loseInHistoryMode(player,actualLevel,isHistoryMode,isForClose):
    if isForClose:
        willRetray = ms.askretrycancel(message="¿Deseas reintentar?", title="Diste click en el botón de cerrar pestaña")
    else:
        willRetray = ms.askretrycancel(message="¿Deseas reintentar?", title="Has perdido")

    if willRetray:
        goToNextLevel(player,actualLevel,isHistoryMode)
    else:
        willSaveMatch = ms.askyesno(message="¿Desea guardar la partida?\nDe no ser así, perderás tu proceso", title="Saldrás del combate")

        if willSaveMatch:
            if len(loadedData[1]) == 1: #poner en cuando ganes
                loadedData[1].append(player.name)
                loadedData[1].append(actualLevel)
                saveData(loadedData,usernamePath)
            else:
                loadedData[1][1] = player.name
                loadedData[1][2] = actualLevel
                saveData(loadedData,usernamePath)
        else:
            if len(loadedData[1]) != 1: #si tiene ya progreso actual
                loadedData[1].pop() #quitar level
                loadedData[1].pop() #quitar personaje   
            saveData(loadedData,usernamePath)
        OpenGamemodeWindow()

def UseAbility(attackingCharacter,attackedCharacter,attackName):

    damage = attackingCharacter.attack(attackedCharacter.type,attackName)

    attackedCharacter.receiveDamage(damage)

    if attackingCharacter.isPlayer:
        changeTurn.set(not changeTurn.get())

        disableButtons(attackButtons)
        powerUpButton.config(state=DISABLED)

        if cpuHP.get()-damage < 0:
            cpuHP.set(0)
        else:
            cpuHP.set(cpuHP.get()-damage)
    else:
        if playerHP.get()-damage < 0:
            playerHP.set(0)
        else:
            playerHP.set(playerHP.get()-damage)

    displayText.set(attackingCharacter.name + " ha utilizado " + attackName)

def goToNextLevel(player,actualLevel,isHistoryMode):
    ClosePreviousWindow()
    if actualLevel >= 6: #cantidad de personajes
        ms.showinfo(message="¡¡¡FELICIDADES!!!\nHas superado todos los combates\nPuedes intentar completar otra aventura con otro personaje!!",title="GAME OVER")
        ClosePreviousWindow()

        if len(loadedData[1]) != 1: #si tiene ya progreso actual
            loadedData[1].pop() #quitar level
            loadedData[1].pop() #quitar personaje
        saveData(loadedData,usernamePath)
    else:
        OpenFightWindow([player,None],actualLevel,isHistoryMode)

def disableButtons(buttons):
    for button in buttons:
        button.config(state=DISABLED)

def enableButtons(buttons):
    for button in buttons:
        button.config(state=NORMAL)

def RegisterValidation(UsernameTextBox,PasswordTextBox,RePasswordTextBox):
    username = UsernameTextBox.get()
    password = PasswordTextBox.get()
    rePassword = RePasswordTextBox.get()
    global usernamePath
    usernamePath = "registeredUsers/" + username + ".csv"

    # Si ya existe el usuario
    if exists(usernamePath):
        ms.showinfo(message="Ese nombre de usuario ya está registrado, prueba con otro",title="Usuario ya existente")
        return

    if username == "" or password == "" or rePassword == "":
        ms.showwarning(message="Completa todos los campos",title="Campos requeridos")
        return
     
    if password != rePassword:
        ms.showinfo(message="Las contraseñas no coinciden",title="Contraseña inválida")
        return

    datos=[["Contraseña","Personaje","Nivel"]]
    dbName = "registeredUsers/"+ UsernameTextBox.get() + ".csv"
    datos.append([PasswordTextBox.get()])
    
    archivo=open(dbName,"w")
    with archivo:
        escritor=csv.writer(archivo)
        escritor.writerows(datos)

    global loadedData
    loadedData = datos

    OpenGamemodeWindow()
    
def LoginValidation(username, password):
    global usernamePath
    usernamePath = "registeredUsers/" + username.get() + ".csv"
    Data = [[]]

    if username.get() == "" or password.get() == "":
        ms.showinfo(message="Completa todos los campos",title="Campos requeridos")
        return

    # Si no existe el usuario
    if not exists(usernamePath):
        valor=ms.askokcancel(message="No se encontró el usuario\n¿Deseas registrar un usuario nuevo?",title="Usuario no encontrado")
        if valor:
            OpenRegisterWindow()
        else:
            username.delete(0,END)
            password.delete(0,END)
        return

    # Si existe
    with open(usernamePath) as archivo:
        lector = csv.reader(archivo,delimiter=",",
                            quotechar=",",
                            quoting=csv.QUOTE_MINIMAL)
        for renglon in lector:
            if(len(renglon)!=0):
                Data.append(renglon)
    
    #Comprobar contraseña
    if Data[2][0] == password.get():
        openData(path=usernamePath)
        OpenGamemodeWindow()
    else:
        ms.showerror(message="Contraseña incorrecta",title="No fue posible iniciar sesión")
        password.delete(0,END)

def openData(path):
    global loadedData
    loadedData = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if len(row) > 0:
                loadedData.append(row)
    saveData(loadedData,path)

def saveData(data, path):
    with open(path, "w") as fil:
        writer = csv.writer(fil)
        writer.writerows(data)
    # print("File stored with success")


OpenInitialWindow()