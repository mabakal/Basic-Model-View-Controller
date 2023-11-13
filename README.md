### Modèle-Vue-Contrôleur (MVC)

Le modèle MVC, ou Modèle-Vue-Contrôleur, est un modèle d'architecture logicielle couramment utilisé dans le développement d'applications. Il divise une application en trois composants principaux, chacun ayant un rôle spécifique dans le traitement des données et la présentation de l'interface utilisateur.

#### Modèle (Model)

- Le Modèle représente les données de l'application et les règles métier associées.
- Il est responsable de la gestion et de la manipulation des données, ainsi que de l'accès à la base de données si nécessaire.
- Le Modèle ne se préoccupe pas de la manière dont les données sont affichées ou manipulées à l'écran.

#### Vue (View)

- La Vue est responsable de l'interface utilisateur et de l'affichage des données.
- Elle présente les informations au format approprié pour l'utilisateur final.
- La Vue ne manipule pas les données, elle se contente de les afficher de manière compréhensible.

#### Contrôleur (Controller)

- Le Contrôleur agit comme un intermédiaire entre le Modèle et la Vue.
- Il reçoit les entrées de l'utilisateur, traite ces entrées (effectue des validations, des mises à jour du modèle, etc.) et met à jour la Vue en conséquence.
- Le Contrôleur gère les événements et les actions utilisateur.

##### Fonctionnement du MVC

1. L'utilisateur interagit avec l'interface utilisateur (Vue).
2. La Vue transmet les événements utilisateur au Contrôleur.
3. Le Contrôleur traite les événements, met à jour le Modèle en conséquence.
4. Le Modèle, une fois mis à jour, informe la Vue du changement.
5. La Vue récupère les données mises à jour du Modèle et les affiche à l'utilisateur.

Ce repositorie contient un projet qui simule le Modèle MVC dans le développement d'une application.
Le modèle représente la structure de données qu'on souhaite récupérer(Nous simulons une base de données comme un fichié csv, mais généralement
données sont stockés dans la base de données).
Le vue dans notre cas est le fichier principale main.py, il représente l'interface utilisateur
Le controleur sert d'intermédière le modèle et la vue.
