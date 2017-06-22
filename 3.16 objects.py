#method are objects within functions

#class = template or pattern
#method / message = defined capability of class
#field / attribute = data in class
#onject / instance = particular instance in class

class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 1
        print "So Far", self.x

an = PartyAnimal()

an.party()
an.party()
an.party()
