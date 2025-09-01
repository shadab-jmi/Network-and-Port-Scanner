# 🔍 TCP Port Scanner

A simple Python-based **TCP Port Scanner** developed during my internship.  
It allows you to scan specific ports on a given **hostname/IP address** and provides detailed information such as service state, name, version, and extra info.

---

## 🚀 Features
- Accepts hostname/IP as input.
- Scans multiple ports (comma-separated).
- Uses **nmap** for accurate scanning.
- Retrieves and displays the IP address of the target host.
- Handles unreachable machines gracefully.

---

## 📂 Project Structure

scanner.py # Main script for scanning

---

## 🛠️ Tech Stack

- Python
- nmap (Port scanning)
- requests (Host reachability check)
- socket (Hostname/IP resolution)

---

## ⚡ Requirements
- Python 3.x
- Install dependencies using:
```bash
pip install python-nmap requests
```

---

## ▶️ Usage

Run the script with required arguments:
```bash
python scanner.py -o <HOST> -p <PORTS>
```

### Example:

```bash
python3 scanner.py -o scanme. nmap. org -p 22, 80, 444
```

---

## 📌 Sample Output

```bash
The IP Address of the Website scanme.nmap.org is: 45.33.32.156
Successfully connected to 45.33.32.156.
[*] 45.33.32.156 tcp/22 open tcpwrapped
[*] 45.33.32.156 tcp/80 open http 2.4.7 (Ubuntu)
[*] 45.33.32.156 tcp/444 closed snpp
```
