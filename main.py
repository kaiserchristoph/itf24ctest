class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        
    def altern(self, jahre):
        self.alter = max(1, self.alter + jahre)
      