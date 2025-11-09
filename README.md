1. Présentation

Ce projet déploie l’ensemble du système LogisticoTrain à l’aide de Docker Compose.
Il comprend :

Un frontend React servi via Nginx

Une API REST Flask (Python) pour la gestion des rames et des voies

Une API Realtime Spring Boot (Java) pour la communication en temps réel

Deux bases de données : MariaDB (SQL) et MongoDB (NoSQL)

Un broker RabbitMQ pour la communication inter-services

Des outils d’administration : phpMyAdmin et Mongo Express

Le but est de disposer d’un environnement complet, reproductible et isolé pour l’application.

2. Déploiement
Étape 1 : Cloner le projet
git clone https://github.com/MBESNARD99/Docker-Logisticotrain.git
cd logisticotrain-deploy

Étape 2 : Construire le frontend
docker compose --profile build-webapp up --build webapp


Cette commande compile le frontend React et dépose le résultat dans le volume webapp-build.

Étape 3 : Lancer le système complet
docker compose up -d

Étape 4 : Vérifier le statut des conteneurs
docker compose ps


Tous les services doivent apparaître comme healthy.

3. Accès aux services
Frontend	            http://localhost            Interface principale React
REST API (Flask)	    http://localhost/api/v1/    API de gestion (rames, voies, actions)
Realtime API (Spring)	http://localhost/wsapi      Communication temps réel
phpMyAdmin	            http://localhost:8081       Interface d’administration MariaDB
Mongo Express	        http://localhost:8082       Interface d’administration MongoDB
RabbitMQ Admin	        http://localhost:15672      Interface d’administration du broker

4. Commandes utiles

Vérifier les conteneurs :
docker compose ps


Afficher les logs :
docker logs restapi --tail 50


Redémarrer un service :
docker compose restart restapi


Accéder à MariaDB :
docker exec -it sqldatabase mariadb -u root -p

5. Gestion administrative
Bases de données

L’administrateur peut accéder à :

phpMyAdmin via http://localhost:8081
Mongo Express via http://localhost:8082

Supervision

L’état des conteneurs se vérifie avec docker compose ps
Les logs peuvent être consultés avec docker logs <service>
Le broker RabbitMQ est accessible sur http://localhost:15672

Maintenance

Mettre à jour les images et redéployer :

docker compose pull
docker compose up -d --build

Supprimer tout (conteneurs, volumes, images) :

docker compose down -v
docker system prune -a --volumes

6. Fin du déploiement

Une fois tous les conteneurs marqués healthy, l’application est accessible à l’adresse suivante : http://localhost