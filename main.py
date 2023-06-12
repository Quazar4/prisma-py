from prisma import Client

prisma = Client()

def create_person(name, age):
    return prisma.person.create(
        data={
            "name": name,
            "age": age
        }
    )

def get_all_persons():
    return prisma.person.find_many()

person = create_person("Percy", 18)
print(person)

persons = get_all_persons()
for person in persons:
    print(person)
