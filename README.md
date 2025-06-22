# 🔐 Keylogger Pro

**Keylogger Pro** is a GUI-based ethical keylogging tool developed for cybersecurity research and educational purposes. Built with Python using `pynput` and `CustomTkinter`, it allows users to monitor keystrokes in real-time, export logs securely, and understand how keyloggers operate to promote better awareness and protection.

> 📄 Developed as part of **Pinnacle Labs Cybersecurity Internship 2025** (Task 2)

---

## ✨ Features

* 📊 **Real-Time Keystroke Display** in a modern GUI
* ⏱ **Start/Stop Logging** with button control
* 📃 **Export Logs** to timestamped text files
* ⛔ **Offline Tool**: Works entirely without internet
* 📡 **Ethical Use Notice** built into UI

---

## 🔧 Technologies Used

| Technology    | Purpose                       |
| ------------- | ----------------------------- |
| Python 3.8+   | Core Programming Language     |
| pynput        | Keyboard event tracking       |
| CustomTkinter | Modern GUI layout and widgets |
| threading     | Background keystroke listener |
| datetime      | Timestamping exported logs    |

---

## ▶️ How It Works

1. Launch the app
2. Enter the main interface (displays a warning about ethical usage)
3. Click **Start Logging** to begin capturing keystrokes
4. Keys will appear live in the GUI window
5. Click **Stop Logging** to stop the listener
6. Click **Export Logs** to save all captured keystrokes to a `.txt` file with a timestamp

> All logs are saved in the same folder as the script with a timestamped filename.

---

## 🔮 Installation

1. Clone the repository:

```bash

```

2. Install dependencies:

```bash
pip install customtkinter pynput
```

3. Run the script:

```bash
python keylogger_gui.py
```

---

## 🔓 Ethical Use Disclaimer

This tool was created **strictly for cybersecurity awareness and research**. Do **not** deploy or distribute this tool for malicious purposes. Use only in environments where monitoring is permitted.

---

## 🌐 Use Case Scenarios

* Demonstrating how keyloggers work in ethical hacking labs
* Teaching students about system monitoring and defense
* Creating awareness about input security and anti-keylogging techniques

---

## 💼 Project Info

**Project Task:** Internship Task 2 - Keylogger Software

**Internship:** Pinnacle Labs Cybersecurity Internship 2025

**Developer:** Jishnu Dipak Patil



## 📜 License

This project is licensed under the **MIT License**.



**Protect your systems by understanding the threats. Use responsibly.**
