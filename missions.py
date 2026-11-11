import json
import os
from pathlib import Path

class Mission:
    def __init__(self, id, titre, enonce, reponse, xp):
        self.id = id
        self.titre = titre
        self.enonce = enonce
        self.reponse = reponse
        self.xp = xp
    
    def verifier_reponse(self, reponse_joueur):
        if reponse_joueur.strip().lower()==self.reponse.strip().lower():
           return True
        else:
           return False
    def afficher(self):
        print(self.enonce)
        
script_dir = Path(__file__).parent
file_path = script_dir/"missions.json"
with open(file_path) as f:
    raw_data = json.load(f)

missions_list = []
for data in raw_data:
    m = Mission(data["ID"], data["Titre"], data["Enonce"], data["Reponse"], data["XP"])
    missions_list.append(m)

class Joueur:
    def __init__(self, pseudo, points=0, niveau=1, inventaire=None, competences=None):
        self.pseudo = pseudo
        self.points = points
        self.niveau = niveau
        self.inventaire = inventaire if inventaire is not None else []
        self.competences = competences if competences is not None else []
    def gagner_points(self, montant):
        self.points += montant 

    def afficher_profil(self):
        print("Pseudo:", self.pseudo)
        print("Points:", self.points)
        print("Niveau:", self.niveau)
        print("Inventaire:", self.inventaire)
        print("Competences:", self.competences)

class CyberArena:
    def __init__(self, joueur, missions):
        self.joueur = joueur
        self.missions = missions


    def afficher_menu(self):
        print("====================")
        print("    CYBER ARENA")
        print("====================")
        while True:
            print("1) Voir mon profil")
            print("2) Voir les missions")
            print("3) Lancer une mission")
            print("4) Voir mon inventaire")
            print("5) Sauvegarder")
            print("6) Quitter")
            choix = input("Choix: ")
            if choix == "1":
               self.joueur.afficher_profil()
            elif choix == "2":
                for mission in self.missions:
                    print(mission.titre)
            elif choix == "3":
                for i, mission in enumerate(self.missions):
                    print(i+1, "-", mission.titre)
                choix_mission = input("Choisis une mission(numero): ")
                if choix_mission.isdigit():
                    index = int(choix_mission)-1
                    if 0<=index<len(self.missions):
                        mission_choisie = self.missions[index]
                        mission_choisie.afficher()
                        reponse = input("Ta reponse: ")
                        if mission_choisie.verifier_reponse(reponse):
                            self.joueur.gagner_points(mission_choisie.xp)
                            print("Correct! Tu gagnes", mission_choisie.xp, "XP")
                        else:
                            print("Faux! La reponse etait:", mission_choisie.reponse)
                    else:
                        print("Numero invalide.")
                else:
                    print("Ce n'est pas un nombre.")
            elif choix == "4":
               print(self.joueur.inventaire)
            elif choix == "5":
                self.sauvegarder()
            elif choix == "6":
                print("Au revoir!")
                break
            else:
                print("Choix invalide, reessaie.")

    def sauvegarder(self):
        data = {
            "pseudo": self.joueur.pseudo,
            "points": self.joueur.points,
            "niveau": self.joueur.niveau,
            "inventaire": self.joueur.inventaire,
            "competences": self.joueur.competences
        }
        script_dir = Path(__file__).parent
        save_path = script_dir/"save.json"
        print("Saving to:", save_path)
        with open(save_path, "w") as f:
            json.dump(data, f)
        print("Progression sauvegardee!")

script_dir = Path(__file__).parent
save_path = script_dir/"save.json"
if os.path.exists(save_path):
    with open(save_path, "r") as f:
        save_data = json.load(f)
    j = Joueur(
        save_data["pseudo"],
        save_data["points"],
        save_data["niveau"],
        save_data["inventaire"],
        save_data["competences"],
    )    
    print("Progression chargee!")
else:
    j = Joueur("Paul")
    print("Nouvelle partie!")        
arena = CyberArena(j, missions_list)
arena.afficher_menu()

      


