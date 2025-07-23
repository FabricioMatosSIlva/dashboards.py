import pyautogui
import time

# Mostra a resolução da tela
largura, altura = pyautogui.size()
print(f"Resolução da tela: {largura}x{altura}")

# Move o mouse em forma de quadrado
print("Movendo o mouse em forma de quadrado...")
pyautogui.moveTo(100, 100, duration=0.5)
pyautogui.moveTo(500, 100, duration=0.5)
pyautogui.moveTo(500, 500, duration=0.5)
pyautogui.moveTo(100, 500, duration=0.5)
pyautogui.moveTo(100, 100, duration=0.5)

# Clique com o botão esquerdo na posição atual
pyautogui.click()
print("Clique executado.")

# Scroll (rolagem do mouse)
pyautogui.scroll(-500)  # scroll para baixo
time.sleep(1)
pyautogui.scroll(500)   # scroll para cima

# Mover o mouse em círculos (opcional, visual e divertido 😄)
print("Movendo o mouse em círculo...")
import math
raio = 100
centro_x, centro_y = 600, 400
for grau in range(0, 360, 10):
    x = centro_x + raio * math.cos(math.radians(grau))
    y = centro_y + raio * math.sin(math.radians(grau))
    pyautogui.moveTo(x, y, duration=0.05)

print("Movimento finalizado.")
