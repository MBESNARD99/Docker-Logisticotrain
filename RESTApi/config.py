# REST API Configuration for Docker Deployment

# Base server configuration
SERVER_HOST = '0.0.0.0'  # Docker doit écouter sur toutes les interfaces
SERVER_PORT = 5001
DEBUG = False

# CORS : nécessaire si le front nginx sert sur un autre hôte
ENABLE_CORS = True

# SQL Production Database Configuration
SQLDB_SETTINGS = {
    "db": "myrames-prod-db",
    "user": "mariaUsr",
    "password": "mariaPwd",
    "host": "sqldatabase",  # service docker
    "port": 3306
}

# MongoDB History Database Configuration
MONGODB_SETTINGS = {
    "db": "history-db",
    "host": "nosqldatabase",  # service docker
    "port": 27017,
    "username": "mongoUsr",
    "password": "mongoPass",
    "authentication_source": "admin"
}
