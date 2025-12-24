# Authentification

Bien que votre portfolio est heberge par vous meme et que vous pouvez le manipuler comme bon vous semble, `Mrcfolio` offre un server d'authentification embarque, ce qui permettra de securiser des ednpoints qui peuvent changer le comportement des entites comme : **Projects, Technologies, Collaborateurs**. <br>
Le serveur d'auth est visible uniquemet via l'application principale et l'application offira un endpoint `/users/login` qui permettra de recuperer un token depuis le service d'auth.

## Cas d'utilisation
```bash
GET /users/login
```
Ce point de terminaison attend un formulaire avec le couple `username` `password`. A noter que le username correspondra au courriel que vous avez fourni a votre compte administrateur dans votre `.env` et un token vous sera delivre.

### Exemple
```bash
curl -X 'POST' \
  'http://localhost:8079/api/v1/users/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=admin@example.com&password=Admin@12345'
```
### Reponse : 
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbkBleGFtcGxlLmNvbSIsImV4cCI6MTc2NjU1NjI1MiwiYWRtaW4iOnRydWV9.mreBpyZQLK23wBLCnrhKphP-b88SoiwmF3DC6qUpRzU",
  "token_type": "bearer"
}
```
Votre token, vous pouvez l'utiliser pour les points terminaison qui sont proteges. vous en savoir plus. Veuillez regarder les autres sections sur les points de terminaison dans la documentation.


**N.B.** Si vous avez fourni vos identifiants de connexions correctement et que vous avez un code de reponse HTTP `401`. Veuillez verifier si vous avez bel et bien initialiser votre instance avec votre administratif. lors du lancement de votre instance pour la premiere fois, vous devez appeler le endpoint: `/init` et lui fourni le `key` une cle secrete que vous devez vous meme declarer dans votre `.env`. Si vous ne l'avez pas appele, il suffit juste de le faire et de reessayer d'obtenir votre token. Sinon, ouvrez un issue sur le depot github pour un suivi plus fine.

#### Exemple d'initialisation
```bash
curl -X 'POST' \
  'http://localhost:8079/init?key=494c157c-0880-461f-826a-3a867cfa128a' \
  -H 'accept: */*' 
```
`key` : est la cle secrete dans votre `.env`
#### Response
Aucune reponse avec donees ne sera renvoyee, vous recevrez un code HTTP `204` pour savoir si votre compte administratif a bel et ete cree, vous pouvez essayer d'otenir un token d'acces.