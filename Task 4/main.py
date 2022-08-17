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


movie1 = Movie("Velnio nuotaka", "Zebriunas", 80000)
movie2= Movie("Tadas Blinda.Pradžia", "Ulvydas", 90000 )

movie = []    
movie.append(movie1)
movie.append(movie2)


for mov in movie:
    print(mov.budget)
def wasExpensive(self, budget): 
    for mov in movie:
        if mov.budget > 100000:
            print("True")
        else:            
             print("False")

    
    movie.wasExpensive()
   