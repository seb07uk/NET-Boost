import tkinter as tk
from tkinter import messagebox
import subprocess
import ctypes

# ============================================
# polsoft.ITS™ NET-BOOST CONTROL PANEL v1.0
# ============================================

# Włączenie wygładzania czcionek (High DPI awareness)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    ctypes.windll.user32.SetProcessDPIAware()

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się wykonać polecenia:\n{cmd}\n\n{e}")

def apply_settings():
    actions = []

    if var_reset_tcp.get():
        actions.append("netsh int ip reset")
        actions.append("netsh winsock reset")

    if var_dns.get():
        actions.append("ipconfig /flushdns")
        actions.append("ipconfig /registerdns")

    if var_autotune.get():
        actions.append("netsh int tcp set global autotuninglevel=experimental")

    if var_ctcp.get():
        actions.append("netsh int tcp set global congestionprovider=ctcp")

    if var_ecn.get():
        actions.append("netsh int tcp set global ecncapability=enabled")

    if var_heuristics.get():
        actions.append("netsh int tcp set heuristics disabled")

    if var_services.get():
        actions.append("sc stop DiagTrack")
        actions.append("sc config DiagTrack start=disabled")
        actions.append("sc stop WSearch")
        actions.append("sc config WSearch start=disabled")

    if var_restart_dns.get():
        actions.append("net stop dnscache")
        actions.append("net start dnscache")

    if not actions:
        messagebox.showinfo("polsoft.ITS™", "Nie wybrano żadnych funkcji.")
        return

    for cmd in actions:
        run_cmd(cmd)

    messagebox.showinfo("polsoft.ITS™", "Optymalizacja zakończona!")

# ============================================
# GUI
# ============================================

root = tk.Tk()
root.title("polsoft.ITS™ NET-BOOST CONTROL PANEL")
root.resizable(False, False)
root.configure(bg="#101010")

title = tk.Label(root, text="polsoft.ITS™ NET‑BOOST", fg="#00FF66", bg="#101010", font=("Consolas", 18, "bold"))
title.pack(pady=(20, 10), padx=20)

# Opcje
var_reset_tcp = tk.BooleanVar()
var_dns = tk.BooleanVar()
var_autotune = tk.BooleanVar()
var_ctcp = tk.BooleanVar()
var_ecn = tk.BooleanVar()
var_heuristics = tk.BooleanVar()
var_services = tk.BooleanVar()
var_restart_dns = tk.BooleanVar()

options = [
    ("Reset TCP/IP + Winsock", var_reset_tcp),
    ("Czyszczenie i rejestracja DNS", var_dns),
    ("Autotuning TCP (experimental)", var_autotune),
    ("CTCP – szybkie pobieranie", var_ctcp),
    ("ECN – mniejsze lagi", var_ecn),
    ("Wyłączenie heurystyk TCP", var_heuristics),
    ("Wyłączenie usług (DiagTrack, WSearch)", var_services),
    ("Restart DNS Cache", var_restart_dns),
]

options_frame = tk.Frame(root, bg="#101010")
options_frame.pack(pady=5, padx=20)

for text, var in options:
    tk.Checkbutton(
        options_frame,
        text=text,
        variable=var,
        fg="#00FFAA",
        bg="#101010",
        selectcolor="#202020",
        font=("Consolas", 12)
    ).pack(anchor="w", pady=2)

# Przycisk
btn = tk.Button(root, text="ZASTOSUJ", command=apply_settings, bg="#00FF66", fg="black", font=("Consolas", 14, "bold"))
btn.pack(pady=20, padx=20)

footer = tk.Label(root, text="NET-BOOST CONTROL PANEL\nv1.0", fg="#00FF66", bg="#101010", font=("Consolas", 10, "bold"))
footer.pack(pady=5, padx=20)

copyright_label = tk.Label(root, text="2026©  polsoft.ITS™ London  by \nSebastian Januchowski. All rights reserved.", fg="#00FF66", bg="#101010", font=("Consolas", 8))
copyright_label.pack(pady=(5, 20), padx=20)

root.mainloop()