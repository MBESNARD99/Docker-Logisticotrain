# Étape 1 : Image Python légère
FROM python:3.11-slim

LABEL maintainer="LogisticoTrain Deployment Team"
LABEL description="LogisticoTrain REST API (Flask)"

# Installer les dépendances système nécessaires à mysqlclient
RUN apt-get update && \
    apt-get install -y gcc g++ make pkg-config \
    default-libmysqlclient-dev libmariadb-dev-compat libmariadb-dev && \
    rm -rf /var/lib/apt/lists/*

# Dossier de travail
WORKDIR /app

# Installer les dépendances système
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev wget && \
    rm -rf /var/lib/apt/lists/*

# Copier les dépendances et installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    python -m compileall .

# Copier tout le code source dans l'image
COPY . .

# Rendre le script start-server.sh exécutable
RUN chmod +x start-server.sh

# Exposer le port Flask
EXPOSE 5001

# Variables d'environnement
ENV PYTHONUNBUFFERED=1 \
    FLASK_ENV=production

# Commande de lancement
ENTRYPOINT ["./start-server.sh"]
