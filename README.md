# Immobilier_Arcane

Ce projet a été développé en tant qu'étude de cas durant la phase de recrutement d'Arcane. 

# Problématique : 
Dans le cadre d’un projet de création d’une application web de gestion immobilière, on nous demande de créer un ensemble de microservices. Ces microservices doivent permettre à un utilisateur de renseigner un bien immobilier avec les caractéristiques suivantes : nom, description, type de bien, ville, pièces, caractéristiques des pièces, propriétaire) et de consulter les autres biens disponibles sur la plateforme. 


## Table des matières
1. [Débutons](#débutons)  
    1.1 [Prérequis](#prérequis)  
    1.2 [Installation et démarrage](#installation-et-démarrage)  
2. [Technologies utilisées](#technologies-utilisées)    
    2.1 [Liste des Technologies](#liste-des-technologies)   
    2.2 [Architecture base de données MongoDB](#architecture-base-de-données-mongodb)   
3. [Guide utilisateur](#guide-utilisateur)  
    3.1 [Fonctionnalités](#fonctionnalités)     
    3.2 [Page de connexion/inscription](#page-de-connexioninscription)  
    3.3 [Page d'accueil](#page-daccueil)    
    3.4 [Page d'ajout d'un bien immobilier](#page-dajout-dun-bien-immobilier)   
    3.5 [Page de modification d'un bien immobilier](#page-de-modification-dun-bien-immobilier)  
    3.6 [Page de modification du profil](#page-de-modification-du-profil)   

## Débutons 

Suivez ces instructions afin de copier une version fonctionnelle du projet sur votre machine.

### Prérequis

Tout d'abord, avant de vous lancer, vous aurez besoin d'installer mongo sur votre machine. Suivez donc le lien [suivant](https://www.mongodb.com/download-center/community) afin de procéder à l'installation.
Vous aurez également besoin de télécharger sur votre machine les modules pymongo et wtforms de python avec les lignes de commande suivantes : 
```bash
$ pip install pymongo
$ pip install wtforms
```


### Installation et démarrage 

1) Placez-vous dans le repérertoire où vous souhaitez travailler sur le projet.
2) Clonez le projet avec la commande suivante : 

```bash
$ git clone https://github.com/Git-StevenP/Immobilier_Arcane.git
```

Allez dans le repository :
```bash
$ cd API_Flask/
```

Enfin, il  vous suffit  d'exécuter la commande suivante : 
```bash
$ python run.py
```

Une fois que l'application a fini de se lancer vous pourrez l'utiliser dans votre moteur de recherche.
Lorsque l'exécution est terminée, cliquez sur le lien suivant : [http://127.0.0.1:2745/](http://127.0.0.1:2745/)

## Technologies utilisées

### Liste des technologies

* [Python](https://www.python.org/) - Langage utilisé
* [Flask](http://flask.pocoo.org/) - Framework python utilisé pour développer des application web
* [MongoDB](https://www.mongodb.com/) - Une base de données NoSql utilisée pour stocker les données

### Architecture base de données MongoDB

La base de données est composée de trois collections : users, biens_immobiliers et enfin room_number

La première collection sert à stocker les différents utilisateurs de l'application à l'aide de leur nom de compte et de leur mot de passe. A noter que la fonctionnalité [Modification du profil](#page-de-modification-du-profil) permet d'ajouter des informations à cet utilisateur telles que son nom, son prénom, ou encore sa date de naissance.

La deuxième collection sert à stocker les différents biens immobiliers présents dans l'application. Celle-ci est composée ainsi : 
- name : le nom du bien immobilier
- description : la description du bien immobilier
- type : le type de bien immobilier (maison, appartement, villa)
- city : la ville dans laquelle se situe le bien immobilier
- rooms : les pièces et leurs différentes caractéristiques (détaillées plus bas)
- owner : le propriétaire du bien immobilier
- property : l'utilisateur ayant ajouté le bien immobilier sur la plateforme

![](API_Flask/doc/real_estate.JPG)

La partie comportant les pièces d'un bien est composée ainsi où où chaque pièce est composée de 3 variables :
- room_type : le type de pièce (WC, bedroom, bathroom, garden...)
- room_area : la surface de la pièce (en mètres carrés)
- room_furniture : la pièce est meublée (oui ou non)

![](API_Flask/doc/rooms.JPG)

## Guide utilisateur

### Fonctionnalités

1) Un utilisateur peut modifier les caractéristiques d’un bien (changer le nom, ajouter une pièce, etc… )
2) Les utilisateurs peuvent renseigner/ modifier leurs informations personnelles sur la plateforme (nom, prénom, date de naissance)
3) Les utilisateurs peuvent consulter uniquement les biens d’une ville particulière
4) Fonctionnalité bonus : Un propriétaire ne peut modifier que les caractéristiques de son bien sans avoir accès à l’édition des autres biens.


### Page de connexion/inscription
La page de connexion permet de se connecter ou de s'inscrire dans l'application. Celle-ci permettra donc la création d'un compte et la mémorisation de celui-ci avec votre mot de passe et vos biens immobiliers précédemment créés.


### Page d'accueil
Une fois connecté, la page d'accueil affiche le titre de la page, une barre de navigation comportant les différentes fonctionnalités ainsi qu'une barre de recherche et les biens déjà ajoutés dans la base de données.
Lorsque vous avez déjà ajouté un bien avec cet utilisateur, vous pouvez observer votre bien en surbrillance et, ce faisant, cliquer dessus vous permettra d'accéder à la page de modification.
Vous pouvez aussi utiliser la barre de recherche en tapant une ville afin d'uniquement afficher les biens se situant dans cette ville.


### Page d'ajout d'un bien immobilier
La page d'ajout présente différents champs correspondant aux nom, description, type de bien, ville, pièces, caractéristiques des pièces, propriétaire du bien immobilier. Une fois ces champs remplis et après avoir ajouté ou retiré des pièces, vous pouvez cliquer sur le bouton 'modifier' afin d'ajouter votre bien immobilier dans l'application.


### Page de modification d'un bien immobilier
Lorsque vous êtes l'utilisateur ayant ajouté le bien en question, vous pouvez cliquer sur ce bien dans la page d'accueil et arriver sur la page de modification. Au même titre que la page d'ajout, la page de modification comporte les différents champs précédement cités et permet de modifier le bien sélectionné.


### Page de modification du profil
La page de modification du profil comporte 3 champs correspondant au nom, prénom et date de naissance de l'utilisateur. Une fois ces champs remplis, vous pouvez valider afin d'ajouter/modifier ces différentes informations.
