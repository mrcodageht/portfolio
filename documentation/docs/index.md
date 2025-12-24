# Introduction
Mrcfolio est une application open-source, simple, flexible et auto-hébergeable pour créer des portfolios dynamiques.

## Objectif du projet

Ce projet a pour but de fournir une `base technique moderne et évolutive` pour créer des portfolios dynamiques sans partir de zero.
Chaque utilisateur peut installer sa propre instance du back-end, ajouter ses projets, ses technologies metrisees, des collaborateurs, les modifier, les organiser, et connecter n’importe quel front-end.

Le projet est pensé pour être :

* `Facile à déployer`
* `Facile à comprendre`
* `Facile à personnaliser`
* `Facile à contribuer`

## Pourquoi ce projet existe ?

* Un `back-end dynamique` géré via une API propre ;
* Un `CMS` intégré permettant d’ajouter, modifier ou supprimer les differentes entites sans toucher au code sans faire des requetes http en durs;
* Une architecture `open-source` où tout le monde peut proposer des améliorations ;
* Une instance `indépendante` pour chaque utilisateur.

**Il ne s’agit pas d’un service centralisé**.
Tu clones le dépôt → tu l’installes → tu utilises ton API sur ton propre environnement.

Le dépôt principal est collaboratif :

* Issues ouvertes ;
* Suggestions d’évolution ;
* Amélioration des modèles, endpoints, documentation…
* Pull requests bienvenues !

Le but est de construire ensemble un outil utile à tous.

## Sécurité simplifiée

Chaque instance possède :<br>
Lors du premier lancement de votre instance, vous devez configurer votre fichier d'environemnt `.env` en fournissant une cle secrete qui permttrait d'initialiser le compte administratif du systeme que vous precisera les informations pertinentes dans le fichier environnement aussi.
* Un compte administrateur local 
* Recuperation des tokens de connexions pour manipuler les endpoints proteges. 

## Technologies utilisées

* `FastAPI` - pour sa simplicité, sa rapidité et sa documentation automatique
* `Python` - langage accessible pour les contributeurs
* `Base de données` - MySQL 
* `Docker` - pour faciliter le déploiement

## Comment contribuer ?

1. Forker le projets
2. Créer une branche dédiée
3. Travailler votre amélioration
4. Écrire ou mettre à jour la documentation
5. Soumettre une Pull Request

Toutes les idées, améliorations, corrections de bug ou nouvelles fonctionnalités sont les bienvenues.

## Licence

Projet distribué sous licence `MIT`, permettant une utilisation libre, personnelle ou commerciale.

## Remerciements

Merci à toutes les personnes qui testeront, utiliseront ou contribueront à ce projet.
L’objectif est d’offrir un outil simple, puissant et évolutif pour tous ceux qui veulent montrer leurs projets de manière dynamique.

