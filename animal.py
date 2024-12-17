# Définition des classes
class Habitat:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

class Corps:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

class Pattes:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

class Animal:
    def __init__(self, field, se_reproduit, mange, type_animal):
        self.field = field
        self.se_reproduit = se_reproduit  # Nombre d'enfants
        self.mange = mange                # Type de nourriture
        self.type = type_animal           # Type d'animal
        self.habitat = None               # Agrégation : référence à Habitat
        self.corps = Corps("valeur1", "valeur2", "valeur3")  # Composition obligatoire
        self.pattes = []                  # Liste de pattes (0 à 1000 instances de Pattes)

    def occuper_habitat(self, habitat):
        self.habitat = habitat

    def ajouter_patte(self, patte):
        if len(self.pattes) < 1000:
            self.pattes.append(patte)
        else:
            print("Nombre maximal de pattes atteint")

class Carnivore(Animal):
    def __init__(self, field, se_reproduit, mange, type_animal, chasse):
        super().__init__(field, se_reproduit, mange, type_animal)
        self.chasse = chasse  # Méthode de chasse

class Herbivore(Animal):
    def __init__(self, field, se_reproduit, mange, type_animal, broute):
        super().__init__(field, se_reproduit, mange, type_animal)
        self.broute = broute  # Type de végétation mangée

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'un habitat
    habitat = Habitat("Forêt", "Zone humide", "Tempéré")

    # Création d'un animal herbivore
    herbivore = Herbivore(field="Cerf", se_reproduit=2, mange="Herbe", type_animal="Herbivore", broute="Feuilles")
    herbivore.occuper_habitat(habitat)

    # Ajout de pattes à l'animal
    patte1 = Pattes("Grande", "Puissante", "Marron")
    patte2 = Pattes("Petite", "Fine", "Noire")
    herbivore.ajouter_patte(patte1)
    herbivore.ajouter_patte(patte2)

    # Création d'un animal carnivore
    carnivore = Carnivore(field="Loup", se_reproduit=4, mange="Viande", type_animal="Carnivore", chasse="En meute")
    carnivore.occuper_habitat(habitat)

    # Affichage des informations
    print(f"Herbivore : {herbivore.field}, Habitat : {herbivore.habitat.field1}")
    print(f"Carnivore : {carnivore.field}, Chasse : {carnivore.chasse}")
    print(f"Nombre de pattes de l'herbivore : {len(herbivore.pattes)}")
    for i, patte in enumerate(herbivore.pattes, start=1):
        print(f"Patte {i} : {patte.field1}, {patte.field2}, {patte.field3}")
