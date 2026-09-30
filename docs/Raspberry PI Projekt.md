---
creationDate: 2026-09-23
tags:
  - schule
lastEditDate:
---
# Aufgabe
![[2026_Raspberry_Temperatur_Monitoring_Auftrag.pdf]]



# Doku

## Festlegung Systemumgebung und Installation

### Systemumgebung

- **OS**: PI OS Light 64 bit
	-> Warum:
		- leichtgewichtig und ressourcenschohnend
		- keine Graphische Oberfläche nötig das Arbeit via ssh
- **Systemsprache**: Deutsch
	-> für Tastatus-Layout und Zeit
- **Accountdaten**
	-> user:admin
	-> pwd:admin
- **Zugriffsmöglichkeiten**
    -> ssh 
    -> Pi Connect (da das Netzwerk IT-Lab_Schueler P2P nicht zulässt)

### Installation

> **Offizielle Doku RasPi**: [https://www.raspberrypi.com/documentation/computers/getting-started.html](https://www.raspberrypi.com/documentation/computers/getting-started.html)
> **Offizielle Doku BPM280** [https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf)

**Vorgehen im PI Imager**:
1. Gerät auswählen
2. OS auswählen
3. SD-Karte zum schreiben auswählen
4. Hostnamen vergeben (raspi-grp3)
5. Zeitzone und Keyboardlayout setzen
6. Nutzer (admin) erstellen mit Passwort und Namen
7. "enable SSH" mit Passwort Authentication
8. Pi Connect aktivieren (da das Netzwerk P2P nicht zulässt)
9. dann Wirte image

**WLAN Verbindung einrichten**:

Da wir eine Netzwerkverbindung via Banutzername und Passwort herstellen wollen, muss dies noch direkt im *Image* konfiguriert werden, da dies nicht über den *PI Imager* eingerichtet werden kann.

1. Terminal öffnen
2. in gemountetes SK-Karten verzeichnis navigieren
3. dort dann `/etc/NetworkManager/systemconnection/`
	- dort können Einträge angelegt werden, welche Anagaben über die verschiedenen Netzwerkverbinungen enthalten
4. 

**in P2P enabled network**

Da die einrichtung direkt am Gerät in der Schule nicht funktioniert hat in anderem Netzwerk eingerichtet
1. login auf Pi
2. sudo nmtui
3. wlan auswählen 
4. new (connection)
5. angaben nach vorgabe der Maske machen 
6. wlan verbindung testen im Zielnetzwerk

**Docker**
[Docker Installationsanleitung für non testing](https://docs.docker.com/engine/install/debian/)

**Grafana**
[Grafana APT-Installation](https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/#install-from-apt-repository)

**plotly**
[plotly for python](https://plotly.com/python/getting-started/#installation)
Installation via apt
sudo apt install python3-plotly

**Crontab**
crontab -e
zeile unten einfügen
\#*/5 * * * * /pfad-zum-data-polling-script

zum späterem aktivieren das \# vor der Zeile entfernen

**NodeRed**
kontrolle nodejs installiert - ja
sudo apt install nodejs npm 

**I2C**
sudo raspi-config
3 Interface Options
I5 I2C aktivieren
sudo reboot
sudo apt isntall i2c-tools

**Verkabelung Sensor**
[https://pinout.xyz/](https://pinout.xyz/)
Vcc zu pin1 
gnd zu pin6
scl zu pin3
sda zu pin5

## Python Polling Script
[lgpio Dokumentation](https://rpi-lgpio.readthedocs.io/en/latest/api.html)
keine API von Bosch gefunden

# Abgesprochener Softwarestack ist installiert

