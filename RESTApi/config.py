# REST API Configuration for Docker Deployment (avec support des secrets Docker)

import os


def read_secret(path: str, default: str = "") -> str:
    """
    Lit un secret Docker depuis un fichier monté dans /run/secrets.
    Renvoie 'default' si le fichier n'existe pas.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return default


# Base server configuration
SERVER_HOST = "0.0.0.0"  # Docker doit écouter sur toutes les interfaces
SERVER_PORT = 5001
DEBUG = False

# CORS : nécessaire si le front nginx sert sur un autre hôte
ENABLE_CORS = True

# SQL Production Database Configuration
SQLDB_SETTINGS = {
    "db": "myrames-prod-db",
    "user": "mariaUsr",
    # Si le secret n'est pas présent (ex: en local simple), fallback sur l'ancien mot de passe
    "password": read_secret("/run/secrets/mariadb_user_password", "mariaPwd"),
    "host": "sqldatabase",  # service docker
    "port": 3306,
}

# MongoDB History Database Configuration
MONGODB_SETTINGS = {
    "db": "history-db",
    "host": "nosqldatabase",  # service docker
    "port": 27017,
    "username": "mongoUsr",
    "password": read_secret("/run/secrets/mongo_root_password", "mongoPass"),
    "authentication_source": "admin",
}
