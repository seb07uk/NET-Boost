<img width="748" height="884" alt="image" src="https://github.com/user-attachments/assets/d505f122-9e4d-4773-bdcf-78c923d0eefd" />


# ⚡ **polsoft.ITS™ NET‑BOOST CONTROL PANEL v1.0** 
# Ultra‑lightweight Network Optimization Panel for Windows

**Modern. Modular. Secure. Fast.** Developed by **polsoft.ITS™ London** — designed for users who demand full control over Windows network stacks.

</div>

---

## 🧠 About the Project

**NET‑BOOST CONTROL PANEL** is a minimalist Python-based GUI application that applies advanced network optimizations with a single click.  
Designed for:
- System Administrators
- Gamers and Creators
- Users requiring a stable, responsive connection

The application utilizes native Windows tools (`netsh`, `ipconfig`, `sc`) presented through a user-friendly, neon interface.

---

## 🚀 Features

| Feature | Description |
|:--- |:--- |
| 🔄 **Reset TCP/IP + Winsock** | Restores the Windows network stack to factory defaults. |
| 🧹 **Flush & Register DNS** | Clears DNS cache and re-registers configuration. |
| ⚙️ **TCP Autotuning** | Aggressive bandwidth tuning (experimental). |
| 🚀 **CTCP Support** | Enables modern congestion control for faster downloads. |
| 🟢 **ECN Activation** | Reduces latency via Explicit Congestion Notification. |
| 🧠 **Disable TCP Heuristics** | Removes limitations imposed by system heuristics. |
| 🛑 **Service Management** | Stops telemetry (DiagTrack) and indexing (WSearch). |
| 🔁 **Restart DNS Cache** | Quickly restarts the `dnscache` service. |

---

## 🧩 Architecture

The application is built on three core modules:
1. **Execution Layer:** Securely runs system commands and handles error messaging via `messagebox`.
2. **Logic Layer:** Generates and executes a sequence of system actions based on user selection.
3. **Presentation Layer (GUI):** Built with Tkinter, featuring DPI Awareness for 4K clarity and a signature **polsoft.ITS™** neon dark-tech theme.

---

## 📦 Installation & Usage

### ✔️ Requirements
- Windows 10 / 11
- Python 3.x
- Administrator Privileges

### ✔️ Launching
```bash
python netboost.py
