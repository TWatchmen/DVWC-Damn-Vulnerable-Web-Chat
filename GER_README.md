##### Probleme:
- sqlite statt mariadb


# Damn Vulnerable Web Chat (DVWC)
## ⚠️ Disclaimer

Damn Vulnerable Web Chat (DVWC) ist eine absichtlich verwundbare Webanwendung, die ausschließlich zu Schulungs-, Lern- und Testzwecken entwickelt wurde.

Die enthaltenen Schwachstellen sind bewusst implementiert, um das Verständnis für Websicherheit und die Ausnutzung sowie Behebung typischer Sicherheitslücken zu fördern.

Nutze dieses Projekt ausschließlich in einer isolierten lokalen Testumgebung oder in autorisierten Laboren.

## Features
- Benutzerregistrierung und Login
- Forum
Öffentliche Chaträume
Private Nachrichten
Benutzerprofile
Dateiuploads
Admin-Bereich
Mehrere absichtlich verwundbare Module
Verschiedene Sicherheitsstufen (geplant)

## Enthaltene Schwachstellen (geplant)
| Kategorie               |  Status |
|:------------------------|--------:|
| Login Brute Force       |       ⏳ |
| Broken Access Control   |       ⏳ |
| Session Vulnerabilities |       ⏳ |
| Passwörter im Klartext  |       ⏳ |
| Mass Assignment         |       ⏳ |
| Stored XSS              |      	⏳ |
| Reflected XSS           |       ⏳ |
| DOM XSS                 |       ⏳ |
| SQL Injection           |       ⏳ |
| Blind SQL Injection     |       ⏳ |

CSRF	⏳
IDOR	⏳
File Upload	⏳
Local File Inclusion (LFI)	⏳
Command Injection	⏳
Server-Side Request Forgery (SSRF)	⏳
Session Vulnerabilities	⏳

## Projektstruktur
damn-vulnerable-web-chat/
│
├── app/
├── database/
├── vulnerable/
├── php/
├── docs/
└── docker/
## Installation
1. Repository klonen 
   1. git clone https://github.com/TWatchmen/DVWC-Damn-Vulnerable-Web-Chat.git
2. cd damn-vulnerable-web-chat
   Virtuelle Umgebung erstellen
   python -m venv .venv

Linux/macOS

source .venv/bin/activate

Windows

.venv\Scripts\activate
Abhängigkeiten installieren
pip install -r requirements.txt
Anwendung starten
python run.py

Die Datenbank wird beim ersten Start automatisch erstellt.

## Technologien
Python
Flask
HTML5
CSS3
JavaScript
SQLite
PHP (für ausgewählte Übungen)
Docker
## Projektziel
Das Projekt wurde von mir in meiner Freizeit geschrieben um mich selber mit Cyber Security vertraut zu machen.
Dieses Projekt soll eine moderne, bewusst verwundbare Chat-Anwendung bereitstellen, 
mit der typische Web-Schwachstellen praxisnah untersucht und verstanden werden können. Ziel ist es, 
sowohl die Angriffsseite als auch die Umsetzung sicherer Gegenmaßnahmen nachvollziehbar zu machen.

## Hinweise
Nicht produktiv einsetzen.
Nicht auf öffentlich erreichbaren Servern betreiben.
Nur in autorisierten Testumgebungen verwenden.


Lizenz

Dieses Projekt steht unter der in der Datei LICENSE angegebenen Lizenz.