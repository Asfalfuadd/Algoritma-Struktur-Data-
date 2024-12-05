
undo_stack = []
redo_stack = []
stack = []

def push(item):
    stack.append(item)
    undo_stack.append(("pop", item))
    redo_stack.clear()
    print("Push", item, "to stack")

def undo():
    if undo_stack:
        aksi, item = undo_stack.pop()
        if aksi == "pop":
            redo_stack.append(("pop", item))
            stack.pop()
            print("Undo", aksi, item)
    else:
        print("Tidak ada item yang di undo")

def redo():
    if redo_stack:
        aksi, item = redo_stack.pop()
        if aksi == "pop":
            undo_stack.append(("pop", item))
            stack.append(item)
            print("Redo", aksi, item)
    else:
        print("Tidak ada item yang di redo")

while True:
    print("\nTest Program Undo Redo")
    print("Stack saat ini: ", stack)
    print("Pilih aksi")
    print("1. Push")
    print("2. Undo")
    print("3. Redo")
    print("4. Exit")

    perintah = input("Masukkan perintah:")

    if perintah == "1":
        item = input("Masukkan item yang ingin dimasukkan ke stack: ")
        push(item)
    elif perintah == "2":
        undo()
    elif perintah == "3":
        redo()
    elif perintah == "4":
        print("keluar dari program")
        break
    else:
        print("Perintah tidak di kenal")
