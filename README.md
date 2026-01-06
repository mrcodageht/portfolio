# Mrcfolio

Mrcfolio est un projet de back-office destiné à gérer un portfolio
personnel de manière moderne, flexible et entièrement auto‑hébergeable.

## Objectif du projet

Ce back-end a pour vocation de fournir une base robuste et évolutive
permettant à chaque utilisateur de :

-   Déployer facilement sa propre instance du service
-   Ajouter, modifier, organiser et publier ses projets
-   Connecter n'importe quel front-end pour afficher son portfolio
-   Personnaliser son environnement selon ses besoins
-   Contribuer librement au code (licence MIT)

Le projet vise à être :

-   **Simple à déployer** grâce à un `docker-compose`
-   **Simple à comprendre** avec une documentation générée via
    **MkDocs**
-   **Simple à maintenir et étendre**
-   **Ouvert à la contribution** (open‑source, licence MIT)


## Stacks & Architecture

Le fichier `docker-compose.yaml` met en place plusieurs services
complémentaires :

### 🔹 Backend (API)

Une API construite avec **FastAPI**, permettant de gérer : <br> 
- Les projets 
- Les technologies maîtrisées 
- Les collaborateurs (pour
attribuer des crédits ou contributions)

```bash
# url
http://localhost:8079
```

### 🔹 Front-end (CMS)

Un petit CMS en **HTML5 / CSS3 / JS / Bootstrap**, permettant
d'interagir avec l'API sans développer un client personnalisé pour gérer
les entités du portfolio.
```bash
# url
http://localhost:8073
```

### 🔹 Documentation

Documentation générée automatiquement grâce à **MkDocs**.
```bash
# url
http://localhost:8075
```

### 🔹 Authentification

Un conteneur dédié à la gestion de l'auth, assurant une sécurité
minimale même en self‑hosting pour empêcher toute modification non
autorisée.
```bash
# url 
http://localhost:8070
```


## Configuration

L'arborescence du projet contient un dossier `config/` regroupant
l'ensemble des fichiers nécessaires pour :

-   Configurer l'environnement
-   Démarrer l'application via Docker
-   Adapter les variables selon votre installation<br>
**N.B:** L'utilisateur admin du systeme n'est pas initialise automatique pour creer le default Admin vous devez fournir les informations dans le fichier .env.backend et aussi une cle screte. Vous devez faire un appel au endpoint /init en fournissant la cle secrete pour initialiser votre compte administrative sans cette modif vous ne pourrez recuperer des jetons et le cms ne sera pas fonctionnel.



## Licence

Ce projet est distribué sous licence **MIT**.


## Collaborateurs

-   **Philogene Wesner**
    -   LinkedIn : [profil linkedin](https://www.linkedin.com/in/wesner-philogene-0b8367374/)
    -   GitHub : [@mrcodageht](https://github.com/mrcodageht)

### Question et support

Email : [ contact courriel ](mrcodage@mrccommunity.com)
