class Packages:

    def __init__(self, ID, street, city, state, zip, deadline, weight, notes, status):
        self.ID = ID
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s ,%s, %s, %s, %s" % (self.ID, self.street, self.city, 
                                                   self.state, self.zip, self.deadline, 
                                                   self.weight, self.notes, self.status)

    