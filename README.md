<div align="center">

# ⚡ **polsoft.ITS™ NET‑BOOST CONTROL PANEL v1.0**  
### Ultra‑lekki panel optymalizacji sieci dla Windows

**Nowoczesny. Modułowy. Bezpieczny. Szybki.**  
Stworzony przez **polsoft.ITS™ London** — zaprojektowany dla użytkowników, którzy chcą mieć pełną kontrolę nad stosami sieciowymi Windows.

</div>

---

## 🧠 O projekcie

**NET‑BOOST CONTROL PANEL** to minimalistyczna aplikacja GUI w Pythonie, która pozwala jednym kliknięciem zastosować zaawansowane optymalizacje sieciowe.  
Zaprojektowana z myślą o:

- administratorach,
- graczach,
- twórcach,
- użytkownikach wymagających stabilnego i responsywnego połączenia.

Aplikacja korzysta z natywnych narzędzi Windows (`netsh`, `ipconfig`, `sc`) i prezentuje je w przyjaznym, neonowym interfejsie.

---

## 🚀 Funkcje

| Funkcja | Opis |
|--------|------|
| 🔄 **Reset TCP/IP + Winsock** | Przywraca stos sieciowy Windows do ustawień fabrycznych. |
| 🧹 **Flush & Register DNS** | Czyści pamięć DNS i rejestruje konfigurację. |
| ⚙️ **TCP Autotuning (experimental)** | Agresywny tuning przepustowości. |
| 🚀 **CTCP – szybkie pobieranie** | Włącza nowoczesny algorytm kontroli przeciążenia. |
| 🟢 **ECN – mniejsze lagi** | Aktywuje Explicit Congestion Notification. |
| 🧠 **Wyłączenie heurystyk TCP** | Usuwa ograniczenia narzucone przez heurystyki systemowe. |
| 🛑 **Wyłączenie usług (DiagTrack, WSearch)** | Zatrzymuje telemetrię i indeksowanie. |
| 🔁 **Restart DNS Cache** | Restartuje usługę `dnscache`. |

Każda opcja działa niezależnie — wybierasz tylko to, czego potrzebujesz.

---

## 🖥️ Zrzut ekranu (UI)

Interfejs utrzymany jest w stylu **dark‑tech**:

- tło: `#101010`
- neonowe akcenty: `#00FF66` / `#00FFAA`
- czcionka: **Consolas**
- minimalistyczny układ checkboxów

*(Możesz dodać tu screenshot, jeśli chcesz — mogę przygotować mockup.)*

---

## 🧩 Architektura

Aplikacja składa się z trzech głównych modułów:

### 1️⃣ **Warstwa wykonawcza**
- `run_cmd()` — bezpieczne wykonywanie poleceń systemowych  
- obsługa błędów i komunikatów `messagebox`

### 2️⃣ **Warstwa logiki**
- `apply_settings()` — generuje listę akcji na podstawie wyborów użytkownika  
- sekwencyjne wykonywanie poleceń systemowych

### 3️⃣ **Warstwa prezentacji (GUI)**
- Tkinter  
- DPI Awareness (ostre czcionki na monitorach 4K)  
- neonowy motyw polsoft.ITS™

---

## 📦 Instalacja

### ✔️ Wymagania
- Windows 10 / 11  
- Python 3.x  
- Uprawnienia administratora  

### ✔️ Uruchomienie

```bash
python netboost.py