class Country():
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population
        
    def get_info(self):
        return {
            "Name": self.name,
            "Capital": self.capital,
            "Population": self.population
        }
        
class DevelopedCountry(Country):
    def __init__(self, name, capital, population, gdp):
        super().__init__(name, capital, population)
        self.gdp = gdp
        
    def get_info(self):
        info = super().get_info()
        info["GDP"] = self.gdp
        return info
    
class DevelopingCountry(Country):
    def __init__(self, name, capital, population, hdi):
        super().__init__(name, capital, population)
        self.hdi = hdi
        
    def get_info(self):
        info =  super().get_info()
        info["HDI"] = self.hdi
        return info
    
class World():
    def __init__(self):
        self.countries = []
        
    def add_country(self, country):
        self.countries.append(country)
        
    def get_country_info(self, name):
        for country in self.countries:
            if country.name == name:
                return country.get_info()
        return None
    

world = World()

usa = DevelopedCountry("United States", "Washington DC", 33100000, 22512000)
india = DevelopingCountry("India", "New Delhi", 13800004385, 0.645)
china = DevelopingCountry("China", "Beijing", 1444216107, 0.785)

world.add_country(usa)
world.add_country(india)
world.add_country(china)

country_info = world.get_country_info("India")

if country_info:
    print("Country info: ")
    for key, value in country_info.items():
        print(f"{key}: {value}")
else:
        print("Country not found!")
