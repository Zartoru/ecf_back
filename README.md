# ECF BACK-END

## Base de données Django avec PhpMyAdmin

### Avant de commencer

#### Prérequis :

Python3 lts, pip3, phpmyadmin

NB: les commandes pour la console sont placées dans des crochets pour permettre de les repérer plus facilement


#### Installer pip3

[sudo apt-get -y install python3-pip]

#### Installer Django

[sudo pip3 install Django]

[python3 -c "import django; print(django.get_version())"] pour verifier l'installation

### Créer la base de données

copier le contenu de create_db.sql dans la fenetre de requete de php my admin
ensuite dans un terminal ouvert dans le dossier du projet faire

[python3 manage.py migrate]

cela appliquera les tables créées 

### Créer l'utilisateur de base de données

copier le contenu de create_dbuser.sql dans la fenetre de requetes de pma
remplacer "username" et "password" par les nom d'utilisateur et mot de passe choisis dans la requete sql ainsi que dans le fichier mysql.cnf

### Inserer les données indispensables

Copier le contenu de data_indisp.sql dans la fenetre de requete de ecf_bdd sur pma

### Inserer les données

copier le contenu de data.sql dans la fenetre de requete sql de la base de données sur pma

## Pour lancer le serveur de dev et se connecter a l'interface d'admin:

[python3 manage.py createsuperuser]

[pyhton3 manage.py runserver]

ceci permettra de se connecter a l'interface d'admin de django en rajoutant "/admin" a la fin de l'url

les adresses pour acceder aux données sont:
(ip)/schoolyears
(ip)/projects
(ip)/users
