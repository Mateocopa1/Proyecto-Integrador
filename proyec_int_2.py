import readchar

while True:
    key = readchar.readkey()
    if key == readchar.key.UP:
        print("Se presionó la tecla UP. Terminando el programa...")
        break
    else:
        print(f"Se presionó la tecla: {key}")