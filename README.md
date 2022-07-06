# pdf_password_remove_windows_contextmenu
Supprimer rapidement les mots de passe protégeants des PDF via le menu contextuel Windows (vous devez connaitre le mot de passe !)
![alt text](https://github.com/thomasdelorge/pdf_password_remove_windows_contextmenu/blob/main/jpg/context-menu.jpg?raw=true "screenshot")

## Pré-requis
- Avoir installé Python (https://www.python.org/downloads/)
- Avoir installé PikePDF ('pip install pikepdf' depuis cmd.exe) (https://pypi.org/project/pikepdf/)
- Avoir les droits administrateur sur la machine (ajout au menu contextuel via regedit, uniquement au premier lancement du script)

## Fonctionnement
1) Télécharger le fichier "pdf_password_remover_contextmenu.py" ci-dessus
2) Executer le fichier : 
- Au premier lancement: powershell vous demande des droits administrateur pour ajouter le script au menu contextuel des fichiers PDF
- Si executé simplement : vous demande de saisir le chemin du fichier PDF a deverrouiller.
![alt text](https://github.com/thomasdelorge/pdf_password_remove_windows_contextmenu/blob/main/jpg/mot%20de%20passe.jpg?raw=true "screenshot")
- Si executé depuis le menu contextuel ou via un drag&drop d'un fichier pdf sur le .py : vous demande de saisir le mot de passe du fichier pdf
![alt text](https://github.com/thomasdelorge/pdf_password_remove_windows_contextmenu/blob/main/jpg/chemin.jpg?raw=true "screenshot")

3) Le fichier pdf deverrouillé est disponible au même emplacement que le fichier pdf verrouillé, préfixé de "_unprotected"

Vous pouvez par la suite supprimer le fichier .py téléchargé : celui-ci se copie dans votre répertoire utilisateur (%userprofile%) pour l'utilisation via le menu contextuel de Windows
