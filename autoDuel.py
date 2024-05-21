import pyautogui as gui
import time

# Inizializza la dimensione dello schermo
ampiezza, larghezza = gui.size()

# Variabili per lo spostamento tra i 4 menu in basso
volte = 0
cicliCompleti = 0
xAttuale = 680
xDaSpostarsi = 200
yMenu = 1040

# Variabili Booleane per i try - except
vaiAlPrimoDuellante = True
vaiAlSecondoDuellante = True
vaiAlTerzoDuellante = True
vaiAlQuartoDuellante = True
vaiAlQuintoDuellante = True
vaiAlSestoDuellante = True
vaiAlSettimoDuellante = True
vaiAllOttavoDuellante = True
vaiAlNonoDuellante = True

# Quando un duellante viene trovato
def duellanteTrovato(x, y):
    gui.click(x, y)
    gui.click(x, y)
    time.sleep(1)
    gui.click(1000, 500)
    time.sleep(1)
    gui.click(1000, 500)
    time.sleep(2)
    gui.click(1160, 930)
    time.wait(20)
    gui.click(967, 1032)
    for i in range(1, 20):
        gui.click(967, 1032)
        time.sleep(0.25)
    time.sleep(10)

# Ciclo per trovare i duellanti in Duel World
while True:
    if volte == 3:
        xDaSpostarsi *= -1
        volte = 0
        cicliCompleti += 1
    
    if cicliCompleti == 10:
        break
    
    if not (vaiAlPrimoDuellante) and not (vaiAlSecondoDuellante) and not (vaiAlTerzoDuellante) and not (
            vaiAlQuartoDuellante) and not (vaiAlQuintoDuellante) and not (vaiAlSestoDuellante) and not (
            vaiAlSettimoDuellante) and not (vaiAllOttavoDuellante):
        vaiAlPrimoDuellante = True
        vaiAlSecondoDuellante = True
        vaiAlTerzoDuellante = True
        vaiAlQuartoDuellante = True
        vaiAlQuintoDuellante = True
        vaiAlSestoDuellante = True
        vaiAlSettimoDuellante = True
        vaiAllOttavoDuellante = True
        vaiAlNonoDuellante = True

        xAttuale += xDaSpostarsi
        volte += 1
        time.sleep(1)
        gui.click(xAttuale, yMenu)

    if vaiAlPrimoDuellante:
        try:
            x, y = gui.locateCenterOnScreen("Duelists/duelist1.png", confidence=0.7)
            duellanteTrovato(x, y)
            vaiAlPrimoDuellante = False
        except:
            vaiAlPrimoDuellante = False
            continue

    if vaiAlSecondoDuellante:
        try:
            x, y = gui.locateCenterOnScreen("Duelists/duelist2.png", confidence=0.7)
            duellanteTrovato(x, y)
            vaiAlSecondoDuellante = False
        except:
            vaiAlSecondoDuellante = False
            continue

    if vaiAlTerzoDuellante:
        try:
            x, y = gui.locateCenterOnScreen("Duelists/duelist3.png", confidence=0.7)
            duellanteTrovato(x, y)
            vaiAlTerzoDuellante = False
        except:
            vaiAlTerzoDuellante = False
            continue

    if vaiAlQuartoDuellante:
        try:
            x, y = gui.locateCenterOnScreen("Duelists/duelist4.png", confidence=0.7)
            duellanteTrovato(x, y)
            vaiAlQuartoDuellante = False
        except:
            vaiAlQuartoDuellante = False
            continue

    if vaiAlQuintoDuellante:
        try:
            x, y = gui.locateCenterOnScreen("Duelists/duelist5.png", confidence=0.7)
            duellanteTrovato(x, y)
            vaiAlQuintoDuellante = False
        except:
            vaiAlQuintoDuellante = False
            continue

    if vaiAlSestoDuellante:
        try:
            x, y = gui.locateCenterOnScreen("Duelists/duelist6.png", confidence=0.7)
            duellanteTrovato(x, y)
            vaiAlSestoDuellante = False
        except:
            vaiAlSestoDuellante = False
            continue

    if vaiAlSettimoDuellante:
        try:
            x, y = gui.locateCenterOnScreen("Duelists/duelist7.png", confidence=0.7)
            duellanteTrovato(x, y)
            vaiAlSettimoDuellante = False
        except:
            vaiAlSettimoDuellante = False
            continue

    if vaiAllOttavoDuellante:
        try:
            x, y = gui.locateCenterOnScreen("Duelists/duelist8.png", confidence=0.7)
            duellanteTrovato(x, y)
            vaiAllOttavoDuellante = False
        except:
            vaiAllOttavoDuellante = False
            continue

    if vaiAlNonoDuellante:
        try:
            x, y = gui.locateCenterOnScreen("Duelists/duelist9.png", confidence=0.7)
            duellanteTrovato(x, y)
            vaiAlNonoDuellante = False
        except:
            vaiAlNonoDuellante = False
            continue
