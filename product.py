
class Product:
    def __init__(self, name, bought_with = None):
        if len(name) < 2:
            raise ValueError('invalid name')
        self.name = name
        if bought_with == None:
            self.bought_with = {}
        else:
            self.bought_with = bought_with

    def __repr__(self):
        return self.name

    
    def update(self, product_names):
        for p in product_names:
            self.bought_with[p] = self.bought_with.get(p, 0)+1

    def get_recommendations(self, k):
        return sorted(self.bought_with, key = self.bought_with.get, reverse=True)[:k]

################################

class GoldProduct:#(Product)
    def __init__(self, name, amount, bought_with = None):
        Product.__init__(self, name, bought_with)
        self.amount = amount
        
    def __repr__(self):
        return Product.__repr__(self) +': '+str(self.amount)+' units left!'

    
    def update(self, product_names):
        #print(self.bought_with)
        Product.update(self, product_names)
        self.amount -= 1
        #print(self.bought_with, self.amount)

    def get_recommendations(self, k):
        results = Product.get_recommendations(self, k)
        for i in range(len(results)):
            if self.bought_with[results[i]] < 10:
                return results[:i]
        return results

###################################  

class RecommendationsSystem:
    def __init__(self, product_tuples):
        self.products = {}
        for name, amaunt in product_tuples:
            if amaunt == -1:
                self.products[name] = Product(name)
            else:
                self.products[name] = GoldProduct(name, amaunt)
    
    
    def update(self, purchased_product_names):
        for i in range(len(purchased_product_names)):
            prod = purchased_product_names[i]
            before = purchased_product_names[:i]
            affter = purchased_product_names[i+1:]
            self.products[prod].update(before+affter)

    def get_recommendations(self, product_name, k):
        return self.products[product_name].get_recommendations(k)
    
##########################################


a = RecommendationsSystem([('aa',8),('ab',-1),('ac',-1),('ad',7),('ae',-1)])
a.update(['aa','ab','ac'])
a.update(['aa','ab','ae'])
print(a.get_recommendations('aa',1))
print(a.get_recommendations('ab',1))

######################################################


class Clip:
    def __init__(self, name, year):
        self.name = name
        self. year = year
        self.is_played = False

    def __rper__(self):
        return self.name+': '+str(self.year)


    def play(self):
        self.is_played = True
    def stop(self):
        self.is_played = False

###############################

class ArtClip(Clip):
    def __init__(self, name, year, time):
        Clip.__init__(self,name, year)
        self.time = time

    def __repr__(self):
        return Clip.__repr__(self)+' ('+str(self.time)+')'


    def is_valid_for_euro(self):
        return self.time <= 3

################################

class Player:
    def __init__(self, clips):
        self.clips = clips
        for clip in self.clips:
            Clip.stop()
        self.current = -1

#    def __next__(self):



#c1 = ArtClip('asd',123,3)
#print(c1)
#print(c1.is_valid_for_euro())
#c1.play()
#print(c1.is_played)

