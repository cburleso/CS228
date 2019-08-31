from pygameWindow import PYGAME_WINDOW

pygameWindow = PYGAME_WINDOW()
print(pygameWindow)
while True:
    pygameWindow.Prepare()
    pygameWindow.Draw_Black_Circle(400, 400)
    pygameWindow.Reveal()
