# Définition des classes
class Habitat:
    def __init__(self, type_habitat, climat, taille_area):
        self.type_habitat = type_habitat  # Type de l'habitat (ex: Forêt, Désert, etc.)
        self.climat = climat  # Climat de l'habitat (ex: Tempéré, Tropical)
        self.taille_area = taille_area  # Taille de la zone (ex: Grande, Moyenne, Petite)


class Corps:
    def __init__(self, type_corps, couleur, taille):
        self.type_corps = type_corps  # Type du corps (ex: Musclé, Léger)
        self.couleur = couleur  # Couleur du corps (ex: Marron, Gris)
        self.taille = taille  # Taille du corps (ex: Grand, Petit)


class Pattes:
    def __init__(self, longueur, force, type_patte):
        self.longueur = longueur  # Longueur des pattes (ex: Longue, Courte)
        self.force = force  # Force des pattes (ex: Forte, Moyenne)
        self.type_patte = type_patte  # Type des pattes (ex: Griffues, Palmées)


class Tete:
    def __init__(self, forme, taille, type_de_tete):
        self.forme = forme  # Forme de la tête (ex: Ronde, Pointue)
        self.taille = taille  # Taille de la tête (ex: Grande, Petite)
        self.type_de_tete = type_de_tete  # Type de la tête (ex: Lisse, Poilue)


class Animal:
    def __init__(self, nom, reproduction, alimentation, type_animal):
        self.nom = nom  # Nom de l'animal (ex: Loup, Cerf)
        self.reproduction = reproduction  # Nombre de petits qu'il peut avoir
        self.alimentation = alimentation  # Type d'alimentation (ex: Carnivore, Herbivore)
        self.type_animal = type_animal  # Type d'animal (ex: Mammifère, Oiseau)
        self.habitat = None  # Référence à l'habitat (Agrégation)
        self.pattes = []  # Liste de pattes (0 à 1000 pattes)
        self.tete = None  # Une seule tête pour chaque animal
        self.corps = None  # Le corps sera assigné via une méthode

    def occuper_habitat(self, habitat):
        self.habitat = habitat  # L'animal occupe un habitat spécifique

    def ajouter_patte(self, patte):
        if len(self.pattes) < 1000:
            self.pattes.append(patte)  # Ajouter une patte
        else:
            print("Le nombre maximal de pattes est atteint.")

    def assigner_tete(self, tete):
        if self.tete is None:
            self.tete = tete  # Assigner une seule tête à l'animal
        else:
            print("Cet animal a déjà une tête.")

    def assigner_corps(self, corps):
        if self.corps is None:
            self.corps = corps  # Assigner un corps à l'animal
        else:
            print("Cet animal a déjà un corps.")


class Carnivore(Animal):
    def __init__(self, nom, reproduction, alimentation, type_animal, methode_chasse):
        super().__init__(nom, reproduction, alimentation, type_animal)
        self.methode_chasse = methode_chasse  # Méthode de chasse (ex: en meute, solitaire)


class Herbivore(Animal):
    def __init__(self, nom, reproduction, alimentation, type_animal, type_végétation):
        super().__init__(nom, reproduction, alimentation, type_animal)
        self.type_végétation = type_végétation  # Type de végétation mangée (ex: Herbe, Feuilles)


# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'un habitat
    habitat = Habitat(type_habitat="Forêt", climat="Tempéré", taille_area="Grande")

    # Création d'un animal herbivore
    herbivore = Herbivore(nom="Cerf", reproduction=2, alimentation="Herbivore", type_animal="Mammifère",
                          type_végétation="Herbe")
    herbivore.occuper_habitat(habitat)

    # Ajout de pattes à l'animal
    patte1 = Pattes(longueur="Longue", force="Forte", type_patte="Griffues")
    patte2 = Pattes(longueur="Courte", force="Moyenne", type_patte="Palmées")
    herbivore.ajouter_patte(patte1)
    herbivore.ajouter_patte(patte2)

    # Création d'un corps pour l'herbivore
    corps_herbivore = Corps(type_corps="Musclé", couleur="Marron", taille="Grand")
    herbivore.assigner_corps(corps_herbivore)

    # Création d'un animal carnivore
    carnivore = Carnivore(nom="Loup", reproduction=4, alimentation="Carnivore", type_animal="Mammifère",
                          methode_chasse="En meute")
    carnivore.occuper_habitat(habitat)

    # Création de têtes
    tete1 = Tete(forme="Ronde", taille="Grande", type_de_tete="Poilue")
    tete2 = Tete(forme="Pointue", taille="Petite", type_de_tete="Lisse")
    herbivore.assigner_tete(tete1)
    carnivore.assigner_tete(tete2)

    # Création d'un corps pour le carnivore
    corps_carnivore = Corps(type_corps="Léger", couleur="Blanc", taille="Moyenne")
    carnivore.assigner_corps(corps_carnivore)

    # Affichage des informations
    print(f"Herbivore : {herbivore.nom}, Habitat : {herbivore.habitat.type_habitat}")
    print(f"Carnivore : {carnivore.nom}, Méthode de chasse : {carnivore.methode_chasse}")

    print(f"Nombre de pattes du herbivore : {len(herbivore.pattes)}")
    for i, patte in enumerate(herbivore.pattes, start=1):
        print(f"Patte {i} : Longueur = {patte.longueur}, Force = {patte.force}, Type = {patte.type_patte}")

    print(
        f"Tête du herbivore : Forme = {herbivore.tete.forme}, Taille = {herbivore.tete.taille}, Type de corps = {herbivore.tete.type_de_tete}")
    print(
        f"Corps du herbivore : Type = {herbivore.corps.type_corps}, Couleur = {herbivore.corps.couleur}, Taille = {herbivore.corps.taille}")

    print(
        f"Tête du carnivore : Forme = {carnivore.tete.forme}, Taille = {carnivore.tete.taille}, Type de corps = {carnivore.tete.type_de_tete}")
    print(
        f"Corps du carnivore : Type = {carnivore.corps.type_corps}, Couleur = {carnivore.corps.couleur}, Taille = {carnivore.corps.taille}")
