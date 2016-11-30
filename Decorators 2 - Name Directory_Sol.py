import operator

people = [input().split() for i in range(int(input()))]

def person_lister(f):
    def inner(people):
        return [f(person) for person in sorted(people, key=lambda s: s[2])]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[-1] == "M" else "Ms. ") + " ".join(person[:-2])

print(*name_format(people), sep='\n')