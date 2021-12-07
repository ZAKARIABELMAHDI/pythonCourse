people = [
    {"name":"Harry","house":"setif"},
    {"name":"Cho","house":"bejaia"},
    {"name":"Draco","house":"djelf"}
]



people.sort( key=lambda person: person["name"])


print(people)