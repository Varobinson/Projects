class Person:

    def __init__(self, name, email, phone):
        
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print('{}\'s email is: {} \n{}\'s phone number is: {}'.format(
            self.name, self.email, self.name, self.phone))

    def add_friend(self,new_friend):
        return self.friends.append(new_friend)

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# sonny.greet(jordan)
# jordan.greet(sonny)

# print(f'{sonny.name}\'s contact info \nemail: {sonny.email}\nphone: {sonny.phone}')
# print(f'{jordan.name}\'s contact info \nemail: {jordan.email}\nphone: {jordan.phone}')

#sonny.print_contact_info()
jordan.add_friend(sonny)
sonny.add_friend(jordan)
print(len(jordan.friends))
