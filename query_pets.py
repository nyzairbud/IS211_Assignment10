import sqlite3 as lite
import sys


con = None

try:
    con = lite.connect('pets.db')
    c = con.cursor()
    person_id = 0
    while person_id != -1:
        try:
            person_id = int(raw_input("\nPlease enter an ID number: "))
            c.execute('''SELECT first_name, last_name, age FROM person WHERE
                 id = %i''' % person_id)
            person_data = c.fetchone()
            person_name = "%s %s" % (person_data[0], person_data[1])
            person_age = person_data[2]
            print " %s, %i years old" % (person_name, person_age)
            c.execute('''SELECT person.first_name, person.last_name, pet.name,
                              pet.breed, pet.age, pet.dead
                             FROM pet
                             LEFT JOIN person_pet
                             ON pet.id = person_pet.pet_id
                             LEFT JOIN person
                             ON person_pet.person_id = person.id
                             WHERE person.id = %i
                          ''' % person_id)
            pet_list = c.fetchall()
            for pet in pet_list:
                pet_name = pet[2]
                pet_breed = pet[3]
                pet_age = pet[4]
                pet_dead = pet[5]
                if pet_dead == 0:
                    print " %s owns %s, a %s, that is %s" % \
                          (person_name, pet_name, pet_breed, pet_age)
                elif pet_dead == 1:
                    print " %s owned %s, a %s, that was %s" % \
                          (person_name, pet_name, pet_breed, pet_age)
        except ValueError:
            print " Enter only integers."
        except TypeError:
            if person_id == -1:
                con.close()
                print " Now exiting program."
                exit(-1)
            print " There is no data associated with that ID number."

except lite.Error, e:

    if con:
        con.rollback()

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()