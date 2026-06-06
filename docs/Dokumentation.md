# Projektdokumentation – Employee Service mit Flask, PostgreSQL, Docker und AWS

## 1. Projektübersicht

### Projektname

Employee Service – REST-API mit Flask, PostgreSQL, Docker und AWS

### Projektziel

Ziel des Projekts war die Entwicklung einer containerisierten REST-API zur Verwaltung von Mitarbeiterdaten. Die Anwendung sollte lokal entwickelt, mit Docker containerisiert, über GitHub versioniert und anschließend auf einer AWS EC2-Instanz bereitgestellt werden.

---

# 2. Verwendete Technologien

* Python 3.13
* Flask
* PostgreSQL 17
* Docker
* Docker Compose
* Git
* GitHub
* AWS EC2
* Ubuntu Linux
* SSH

---

# 3. Entwicklung der Flask-Anwendung

## Ziel

Erstellung einer REST-API mit Python Flask.

## Durchführung

Eine Flask-Anwendung wurde erstellt und der Endpunkt `/employees` implementiert.

Die Anwendung wurde lokal gestartet und getestet.

## Ergebnis

Die Flask-Anwendung lief erfolgreich auf Port 3000.

### Screenshot

Phase3_Flask-Application-Running.png

---

# 4. Installation der Python-Abhängigkeiten

## Ziel

Installation der benötigten Bibliotheken.

## Durchführung

Installation von:

* Flask
* psycopg2-binary

Überprüfung der installierten Pakete mit `pip list`.

## Ergebnis

Alle benötigten Pakete wurden erfolgreich installiert.

### Screenshot

Phase3_Python-Packages-Installation.png

---

# 5. PostgreSQL-Datenbank erstellen

## Ziel

Einrichtung einer PostgreSQL-Datenbank für die Speicherung von Mitarbeiterdaten.

## Durchführung

Datenbank erstellt:

```sql
CREATE DATABASE employee_db;
```

Benutzer erstellt:

```sql
CREATE USER employee_user WITH PASSWORD 'StrongPassword123';
```

Rechte vergeben:

```sql
GRANT ALL PRIVILEGES ON DATABASE employee_db TO employee_user;
```

### Screenshots

* Phase2_PostgreSQL_Database-Overview.png
* Phase2_PostgreSQL_Table-Creation.png

---

# 6. Tabelle employees erstellen

## Durchführung

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(100)
);
```

### Screenshot

Phase2_PostgreSQL_Table-Creation.png

---

# 7. Testdaten einfügen

## Durchführung

```sql
INSERT INTO employees (name, role)
VALUES
('Max', 'Admin'),
('Anna', 'HR');
```

### Screenshots

* Phase2_PostgreSQL_Testdata-Insert.png
* Phase2_PostgreSQL_Data-Verification.png

---

# 8. Datenbankberechtigungen

## Problem

Der Benutzer employee_user verfügte zunächst nicht über ausreichende Rechte.

Fehlermeldung:

```text
permission denied for table employees
```

## Lösung

Die erforderlichen Berechtigungen wurden auf die Tabelle vergeben.

## Ergebnis

Der Datenbankbenutzer konnte erfolgreich auf die Tabelle zugreifen.

### Screenshot

Phase3_PostgreSQL_Table-Permissions.png

---

# 9. Dockerisierung der Anwendung

## Ziel

Containerisierung der Flask-Anwendung.

## Durchführung

Ein Dockerfile wurde erstellt.

Funktionen:

* Python Base Image
* Installation der Abhängigkeiten
* Start der Flask-Anwendung

### Screenshots

* Phase4_Dockerfile-Creation.png
* Phase4_Dockerfile-and-Requirements-Configuration.png

---

# 10. Docker Image erstellen

## Durchführung

```bash
docker build -t employee-service .
```

### Screenshots

* Phase4_Docker-Image-Build.png
* Phase4_Docker-Image-Overview.png

---

# 11. Docker Berechtigungsproblem

## Problem

Beim Ausführen von Docker-Befehlen trat ein Fehler auf.

Fehlermeldung:

```text
permission denied while trying to connect to the Docker daemon socket
```

## Ursache

Der Benutzer war nicht Mitglied der Docker-Gruppe.

## Lösung

```bash
sudo usermod -aG docker $USER
```

Anschließend erfolgte eine Neuanmeldung.

### Screenshots

* Phase4_Docker-Permission-Error.png
* Phase4_Docker-Group-Permissions.png
* Phase4_Docker-Access-Test.png

---

# 12. Docker Compose konfigurieren

## Ziel

Betrieb von Flask und PostgreSQL in separaten Containern.

## Durchführung

Erstellung einer docker-compose.yml mit zwei Services:

* app
* db

### Screenshots

* Phase5_DockerCompose-Configuration.png
* Phase11_DockerCompose-Konfiguration-Prüfung.png

---

# 13. Fehleranalyse – Datenbankverbindung

## Problem

Die API konnte keine Verbindung zur Datenbank herstellen.

Fehlermeldung:

```text
connection refused
```

## Analyse

Die Docker Logs wurden ausgewertet.

### Screenshot

Phase5_Docker-Logs-Database-Connection-Error.png

---

# 14. Fehleranalyse – Tabelle nicht vorhanden

## Problem

Beim Aufruf der API trat folgender Fehler auf:

```text
relation "employees" does not exist
```

## Ursache

Die Tabelle war im Container noch nicht vorhanden.

### Screenshots

* Phase5_API-Internal-Server-Error.png
* Phase11_PostgreSQL-Table-Not-Found-Error.png

---

# 15. Fehlerbehebung

## Durchführung

Tabelle erneut erstellt:

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(100)
);
```

Daten eingefügt:

```sql
INSERT INTO employees (name, role)
VALUES
('Max', 'Admin'),
('Anna', 'HR');
```

## Ergebnis

Die API konnte die Daten erfolgreich abrufen.

### Screenshot

Phase11_PostgreSQL-Daten-Eingefügt.png

---

# 16. Docker Compose erfolgreich gestartet

## Durchführung

```bash
docker compose up -d --build
```

Containerstatus geprüft:

```bash
docker compose ps
```

## Ergebnis

Beide Container liefen erfolgreich.

### Screenshots

* Phase5_DockerCompose-Services-Running.png
* Phase11_Container-Start-AWS.png

---

# 17. API-Test

## Durchführung

```bash
curl http://localhost:3000/employees
```

## Ergebnis

```json
[
  {"name":"Max","role":"Admin"},
  {"name":"Anna","role":"HR"}
]
```

### Screenshots

* Phase3_API-Database-Test.png
* Phase11_API-Erfolgreicher-Test.png

---

# 18. Git Repository erstellen

## Durchführung

```bash
git init
git add .
git commit -m "Initial commit"
```

### Screenshots

* Phase6_Git-Repository-Erstellt.png
* Phase6_Erster-Git-Commit.png
* Phase6_Gitignore-Erstellt.png

---

# 19. GitHub Repository

## Durchführung

Repository auf GitHub erstellt und verbunden.

```bash
git remote add origin https://github.com/sangeeta-das-is/employee-service.git
git push -u origin main
```

### Screenshots

* Phase6_GitHub-Repository-Erstellt.png
* Phase6_GitHub-Push.png

---

# 20. AWS EC2 Instanz erstellen

## Konfiguration

* Ubuntu 24.04 LTS
* t3.micro
* Public IP aktiviert
* SSH Key Pair
* Security Group

### Screenshots

* Phase7_EC2-Instanz-Erstellt.png
* Phase7_EC2-KeyPair-Erstellt.png
* Phase7_EC2-SecurityGroup-Konfiguration.png
* Phase7_EC2-Instanz-Läuft.png
* Phase7_EC2-Public-IP.png

---

# 21. SSH Verbindung zur EC2 Instanz

## Durchführung

```bash
ssh -i employee-service-key.pem ubuntu@<PUBLIC-IP>
```

### Screenshots

* Phase7_EC2-SSH-Verbindung.png
* Phase7_EC2-SSH-Verbindung1.png

---

# 22. Docker auf AWS installieren

## Durchführung

```bash
sudo apt update
sudo apt install docker.io -y
```

Docker gestartet:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Screenshots

* Phase8_Docker-Installation-AWS.png
* Phase8_Docker-Gruppe-Konfiguration.png

---

# 23. Projekt auf AWS bereitstellen

## Durchführung

Repository geklont:

```bash
git clone https://github.com/sangeeta-das-is/employee-service.git
```

Docker Compose gestartet:

```bash
docker compose up -d --build
```

### Screenshots

* Phase9_GitHub-Repository-Geklont.png
* Phase10_DockerCompose-Installation.png
* Phase11_Container-Start-AWS.png

---

# 24. Öffentliche Bereitstellung

## Durchführung

Port 3000 in der AWS Security Group freigegeben.

### Screenshot

Phase12_AWS-Port3000-Freigabe.png

---

# 25. Öffentlicher Funktionstest

## Test

Aufruf über Browser:

```text
http://13.60.194.19:3000/employees
```

## Ergebnis

Die Mitarbeiterdaten wurden erfolgreich als JSON ausgegeben.

### Screenshots

* Phase12_AWS-API-Öffentlich-Erreichbar.png
* Phase12_EC2-Running.png

---

# 26. Fazit

Im Rahmen dieses Projekts wurde eine vollständige REST-API entwickelt, containerisiert und erfolgreich in der AWS Cloud bereitgestellt.

Besonders wertvoll waren die Erfahrungen in den Bereichen:

* Linux Administration
* PostgreSQL Datenbanken
* Docker und Docker Compose
* Git und GitHub
* AWS EC2 Deployment
* Fehleranalyse und Troubleshooting

Das Projekt bildet einen vollständigen End-to-End-Prozess von der Entwicklung bis zum Cloud Deployment ab.
