# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def wasExpensive(self): 
    
        if self.budget > 100000000:
            return True
        else:            
            return False

movie1 = Movie("Velnio nuotaka", "Zebriunas", 8000000)
movie2 = Movie("Tadas Blinda.Pradžia", "Ulvydas", 9000000000 )   
print(f"Velnio nuotaka budget:", movie1.wasExpensive())
print(f"Tadas Blinda budget:",movie2.wasExpensive())
   