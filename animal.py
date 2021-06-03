class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        
    def add_lion(self, name, age, health, happy):
        self.animals.append(lion(name, age, health, happy) )
        
    def add_tiger(self, name, age, health, happy):
        self.animals.append(tiger(name, age, health, happy) )
        
    def add_wolf(self, name, age, health, happy):
        self.animals.append(wolf(name, age, health, happy) )
        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


class Animal:
    def __init__(self, name, age, health, happy):
        self.nombre = name
        self.age = age
        self.health = health
        self.happy = happy

    def feeding (self):
        self.health += 10
        self.happy += 10
        return self
    
    def display_info(self):
        print(f"animal : {self.name}({self.__class__.__name__}) salud :{self.health} felicidad :{self.happy}")
        return self
    
class lion(Animal):
    def __init__(self, name, age, health, happy):
        super().__init__(name, age, health, happy)
        
class tiger(Animal):
    def __init__(self, name, age, health, happy):
        super().__init__(name, age, health, happy)
        
class wolf(Animal):
    def __init__(self, name, age, health, happy):
        super().__init__(name, age, health, happy)
        
            
zoo1 = Zoo("Italo Zoo")
zoo1.add_lion("Nala",10,20,30)
zoo1.add_lion("Simba", 5,10,20)
zoo1.add_tiger("Rajah",15,30,40)
zoo1.add_tiger("Shere Khan",12,10,30)
zoo1.add_wolf("Khan",6,30,50)
zoo1.add_wolf("Shere",8,20,40)
    

print(zoo1.print_all_info)
