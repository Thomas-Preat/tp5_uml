class Adresse:
    """Classe représentant une adresse."""
    def __init__(self, rue, numero, code_postal, ville):
        self.rue = rue
        self.numero = numero
        self.code_postal = code_postal
        self.ville = ville

    def __str__(self):
        return f"{self.numero} {self.rue}, {self.code_postal} {self.ville}"


class Personne:
    """Classe mère représentant une personne."""
    def __init__(self, nom, prenom, etat_civil, adresse: Adresse):
        self.nom = nom
        self.prenom = prenom
        self.etat_civil = etat_civil
        self.adresse = adresse

    def afficher_infos(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}, État Civil: {self.etat_civil}, Adresse: {self.adresse}"


class Eleve(Personne):
    """Classe Élève qui hérite de Personne."""
    def __init__(self, nom, prenom, etat_civil, adresse, niveau):
        super().__init__(nom, prenom, etat_civil, adresse)
        self.niveau = niveau

    def afficher_infos(self):
        return f"{super().afficher_infos()}, Niveau: {self.niveau}"


class Prof(Personne):
    """Classe Professeur qui hérite de Personne."""
    def __init__(self, nom, prenom, etat_civil, adresse, matiere):
        super().__init__(nom, prenom, etat_civil, adresse)
        self.matiere = matiere

    def afficher_infos(self):
        return f"{super().afficher_infos()}, Matière: {self.matiere}"


class Groupe:
    """Classe représentant un groupe composé d'élèves et d'un professeur."""
    def __init__(self, nom_groupe, prof: Prof, eleves=None):
        self.nom_groupe = nom_groupe
        self.prof = prof
        self.eleves = eleves if eleves is not None else []

    def ajouter_eleve(self, eleve: Eleve):
        if len(self.eleves) < 30:  # Limite à 30 élèves par groupe
            self.eleves.append(eleve)
        else:
            print("Impossible d'ajouter plus d'élèves, le groupe est complet.")

    def afficher_groupe(self):
        print(f"Groupe: {self.nom_groupe}")
        print(f"Professeur: {self.prof.afficher_infos()}")
        print("Liste des élèves:")
        for eleve in self.eleves:
            print(f" - {eleve.afficher_infos()}")


# --- Exemple d'utilisation ---
if __name__ == "__main__":
    # Créer une adresse
    adresse_prof = Adresse("Rue des Écoles", 12, "75001", "Paris")
    adresse_eleve = Adresse("Avenue de la République", 45, "75002", "Paris")

    # Créer des instances de Prof et Élèves
    prof1 = Prof("Dupont", "Jean", "Marié", adresse_prof, "Mathématiques")
    eleve1 = Eleve("Martin", "Claire", "Célibataire", adresse_eleve, "Terminale")
    eleve2 = Eleve("Durand", "Paul", "Célibataire", adresse_eleve, "Terminale")

    # Créer un groupe et ajouter des élèves
    groupe1 = Groupe("Groupe 1", prof1)
    groupe1.ajouter_eleve(eleve1)
    groupe1.ajouter_eleve(eleve2)

    # Afficher les informations du groupe
    groupe1.afficher_groupe()
