import pyautogui
import time

"""
# Obtiene la posición actual del cursor
print("Coloca el cursor en la posición deseada y presiona Enter.")
input("Presiona Enter para obtener las coordenadas...")

x, y = pyautogui.position()
print(f"La posición actual del cursor es: ({x}, {y})")
"""


#Posicion (332, 230)
#Posicion (926, 236)


num_repeticiones = 46

for _ in range(num_repeticiones):
    # Primer clic
    pyautogui.moveTo(355, 230)
    pyautogui.click()
    time.sleep(0.5)
    
    # Segundo clic
    pyautogui.moveTo(358, 288)
    time.sleep(0.6)
    pyautogui.click()
    time.sleep(5)
    
    # Tercer clic
    pyautogui.moveTo(926, 236)
    pyautogui.click()
    time.sleep(1)
