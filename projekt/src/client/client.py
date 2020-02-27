#!/usr/bin/env python3
"""Tkinter GUI client"""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

try:
    from tkinter import *
except:
    from Tkinter import *


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFFER_SIZE).decode("utf8")
            messages.insert(END, msg)
        except OSError:
            break


def send(event=None):
    msg = message_tk.get()
    message_tk.set("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{exit}":
        client_socket.close()
        root.quit()


def on_closing():
    message_tk.set("{exit}")
    send()


def window_quit():
    root.destroy()


if __name__ == "__main__":

    root = Tk()
    root.title("Ustaw IP oraz PORT")
    server_details_frame = Frame(root)
    ip = StringVar()
    ip.set("localhost")
    port = StringVar()
    port.set("33000")
    ip_entry = Entry(root, textvariable=ip)
    port_entry = Entry(root, textvariable=port)
    ip_entry.pack()
    port_entry.pack()
    set_button = Button(root, text="Ustaw", command=window_quit)
    set_button.pack()
    root.wait_window()
    PORT = int(port.get())
    HOST = ip.get()
    if not HOST:
        HOST = 'localhost'
    if not PORT:
        PORT = 33000

    root = Tk()
    root.title("Messenger")
    messenger_frame = Frame(root)
    message_tk = StringVar()
    message_tk.set("")
    scrollbar = Scrollbar(messenger_frame)
    messages = Listbox(messenger_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    messages.pack(side=LEFT, fill=BOTH)
    messages.pack()
    messenger_frame.pack()

    entry_field = Entry(root, textvariable=message_tk)
    entry_field.bind("<Return>", send)
    entry_field.pack()
    send_button = Button(root, text="Wyślij", command=send)
    send_button.pack()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    BUFFER_SIZE = 1024
    ADDR = (HOST, PORT)

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(ADDR)

    receive_thread = Thread(target=receive)
    receive_thread.start()
    mainloop()
