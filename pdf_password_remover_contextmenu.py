from dataclasses import replace
import pikepdf
import os
import sys
import shutil
import ctypes

# Variables initialisation script
scriptFullPath = os.path.realpath(__file__)
username = os.getlogin()
python = sys.executable
scriptNeededPath = "C:\\Users\\" + username + "\\pdf_password_remover.py"

if scriptFullPath != scriptNeededPath:
    # Copie le script dans "C:\Users\USERNAME\pdf_password_remover.py" si executé depuis un autre emplacement
    shutil.copyfile(scriptFullPath, scriptNeededPath)

    # Ajoute la clé de registre pour lancer le script depuis le menu contextuel Windows des fichier PDF
    cmdRegAdd = r"REG ADD HKEY_CLASSES_ROOT\SystemFileAssociations\.pdf\shell\Deverrouiller-PDF\command /f /d '\\\"C:\Users\Thomas\AppData\Local\Programs\Python\Python310\python.exe\\\"  \\\"C:\Users\Thomas\pdf_password_remover.py\\\" \\\"%1\\\"'"
    ctypes.windll.shell32.ShellExecuteW(None, "runas", 'powershell.exe', cmdRegAdd)
    print("Le menu contextuel a été ajouté pour déverouiller les .pdf (clic droit) !")

# Récupère le chemin du fichier via argument1 ou via copier coller du chemin
try:
    file = sys.argv[1]
except:
    file = input("Saisir le chemin du fichier pdf à déchiffrer : ")

    # Supprimer les guillemets si présentes
    file = file.replace('"',"")

    # Vérifier que le fichier existe
    if not os.path.isfile(file):
        print ("[ERREUR] Le fichier '" + file + "' n'existe pas !")
        os.system("pause")
        quit()
    
    # Vérifier que le fichier est au format .pdf
    extension = file.split('.')[-1]
    if extension != "pdf":
        print ("[ERREUR] Le fichier '" + file + "' n'est pas au format PDF !")
        os.system("pause")
        quit()


# Générer le nouveau nom de fichier (ajout '_unprotected' avant extension pdf)
x = file.split("\\")
oldName = x[-1]
y = x[-1].replace(".pdf", "_unprotected.pdf")
del x[-1]
x.append(y)
newfile = ('\\').join(x)

# Récupère le mot de passe du fichier PDF
pdf_password = input("Saisir le mot de passe du fichier " + oldName + " : ")

# Deverrouille le PDF
try:
    pdf = pikepdf.open(file, password=pdf_password)
    pdf.save(newfile)
    print("[SUCCES] '" + file + "' a été déchiffré vers " + y)
except pikepdf._qpdf.PasswordError:
    print("[ERREUR] '" + file + "' : mot de passe incorrect")

# Pause fin
os.system("pause")