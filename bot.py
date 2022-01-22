import pyautogui 
from time import *
import os

path = {
    "connectWallet":"images/connectWallet.png",
    "assign":"images/assign.png",
    "heroes":"images/heroes.png",
    "char":"images/char.png",
    "imageX":"images/imageX.png",
    "hunt":"images/hunt.png",
    "back":"images/back.png",
    "valid":"images/valid.png",
    "newmap":"images/newmap.png",
    "ok":"images/ok.png",
    "work":"images/work.png"
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def timerHunt(timer):
    time_hunt = int(timer)*60
    for i in range(time_hunt):
        if i%60 == 0:
            if exist(path['valid']) == -1:
                raise Exception
        clear()
        print(f'Faltam {time_hunt-i} Segundos')
        sleep(1)
    checkClick('heroes','back')

def checkClick(path1,path2):
    while not pyautogui.locateOnScreen(path[path1]):
        point = exist(path[path2])
        if point:
            pyautogui.click(point)
        sleep(4)

def exist(path_image):
    global path
    clear()

    print(f"Procurando... {path_image.replace('.png','').replace('images/','').title()} [A qualquer momento pressione CTRL + C para sair.]")
    image = pyautogui.locateOnScreen(path_image,confidence=0.65)
    newmap = pyautogui.locateOnScreen(path['newmap'],confidence=0.8)
    okpng = pyautogui.locateOnScreen(path['ok'],confidence=0.8)
    if okpng:
        pyautogui.click(okpng)
        print('Erro! Reiniciando bot.')
        sleep(5)
        return -1
    elif newmap:
        pyautogui.click(newmap)
    return image

def workHeroes():
    global path
    pyautogui.moveTo(900,700)
    pyautogui.dragTo(900, 0, 3, button='left')
    sleep(1)    
    while pyautogui.locateOnScreen(path['work'],confidence =0.985):
        if pyautogui.locateOnScreen(path['work'],confidence =0.985,region=(500,720,590,80)):
            pyautogui.click(pyautogui.locateOnScreen(path['work'],region=(500,720,590,80)))

def run(timer):
    list_images = ['assign','connectWallet','heroes','assign','char','heroes','hunt','imageX','valid','hunt']
    clear()
    while True:
        try:    
            for num in range(0,4,2):
                checkClick(list_images[num],list_images[num+1])
            while True:
                for num in range(4,len(list_images)-1,2):
                    if num == 6:
                        workHeroes()
                    checkClick(list_images[num],list_images[num+1])
                timerHunt(timer)
        except KeyboardInterrupt:
            break
        except Exception as ex:
            pass