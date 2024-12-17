class AdresseMail:
    def __init__(self, adresse, nom=None, domaine=None):
        self.adresse = adresse
        self.nom = nom
        self.domaine = domaine

    def __str__(self):
        return self.adresse


class PieceJointe:
    def __init__(self, nom_fichier, taille, type_fichier):
        self.nom_fichier = nom_fichier
        self.taille = taille
        self.type_fichier = type_fichier

    def __str__(self):
        return f"{self.nom_fichier} ({self.type_fichier}, {self.taille} Ko)"


class Titre:
    def __init__(self, contenu):
        self.contenu = contenu

    def __str__(self):
        return self.contenu


class Texte:
    def __init__(self, contenu):
        self.contenu = contenu

    def __str__(self):
        return self.contenu


class Email:
    def __init__(self, adresse_source, adresses_destinataires):
        # Composition : Titre et Texte sont créés à l'intérieur de l'objet Email
        self.titre = None
        self.texte = None

        # Association avec AdresseMail
        self.adresse_source = adresse_source
        self.adresses_destinataires = adresses_destinataires

        # Agrégation avec PieceJointe
        self.pieces_jointes = []

    def definir_titre(self, contenu):
        """Définit le contenu du titre."""
        self.titre = Titre(contenu)

    def definir_texte(self, contenu):
        """Définit le contenu du texte."""
        self.texte = Texte(contenu)

    def ajouter_piece_jointe(self, piece_jointe):
        self.pieces_jointes.append(piece_jointe)

    def __str__(self):
        destinataires = ', '.join([str(adresse) for adresse in self.adresses_destinataires])
        pieces_jointes = '\n'.join([str(pj) for pj in self.pieces_jointes])
        return (f"Email:\n"
                f"Source: {self.adresse_source}\n"
                f"Destinataires: {destinataires}\n"
                f"Titre: {self.titre}\n"
                f"Contenu: {self.texte}\n"
                f"Pièces jointes:\n{pieces_jointes if pieces_jointes else 'Aucune'}")


# Exemple d'utilisation
if __name__ == "__main__":
    # Créer une adresse mail source
    adresse_source = AdresseMail("expediteur@example.com")

    test_destinataires = [AdresseMail("destinataire1@example.com", "michel", "exdomaine"),
                          AdresseMail("destinataire2@example.com")]

    # Créer un email
    email = Email(adresse_source, test_destinataires)

    # Définir un titre et un texte
    email.definir_titre("Projet UML")
    email.definir_texte("Bonjour, voici l'email du projet UML.")

    # Ajouter des pièces jointes
    email.ajouter_piece_jointe(PieceJointe("diagramme.png", 500, "image/png"))
    email.ajouter_piece_jointe(PieceJointe("documentation.pdf", 1200, "application/pdf"))

    # Afficher l'email
    print(email)

