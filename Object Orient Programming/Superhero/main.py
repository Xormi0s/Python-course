class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def user_power(self):
        print(f"{self.name} is using {self.power} power!")
        
    def intro_hero(self):
        print(f"I am {self.name} and I have the power {self.power}")
        
    def save_day(self):
        print(f"{self.name} has saved the day!")
        
    def power_level(self):
        lenght = len(self.power)
        level = lenght*10
        return level
    
class Flying(Superhero):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.speed = speed
    
    def use_power(self):
        print(f"{self.name} is flying at the speed of {self.speed} km/hour")
    
    def calc_distance(self, time):
        distance = self.speed * time
        return distance
    
    
batman = Superhero("Batman", "Strenght")
batman.intro_hero()
print(batman.power_level())

superman = Flying("Clark Kent", "Fly", 130)
superman.intro_hero()
superman.use_power()
distance = superman.calc_distance(30)
print(f"{superman.name} can fly a distance of {distance} km in 30 hours")