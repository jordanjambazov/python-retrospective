class Person:
    MIN_AGE_TO_HAVE_CHILDREN = 18

    def __init__(self, name, birth_year, gender, father=None, mother=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.father = father
        self.mother = mother

        for parent in ('father', 'mother'):
            if getattr(self, parent, False):
                getattr(self, parent).add_child(self)

        self._children = []

    def get_siblings(self, gender):
        siblings = {parent_child for parent in ('father', 'mother')
                    if getattr(self, parent, False) for parent_child in
                    getattr(self, parent).children(gender) if parent_child is
                    not self}
        return list(siblings)

    def get_brothers(self):
        return self.get_siblings('M')

    def get_sisters(self):
        return self.get_siblings('F')

    def add_parent(self, parent):
        if self not in parent.children():
            return parent.add_child(self)

    def add_child(self, child):
        if isinstance(child, Person) and child not in self.children():
            parent_age = child.birth_year - self.birth_year
            if parent_age < self.MIN_AGE_TO_HAVE_CHILDREN:
                return
            self._children.append(child)
            setattr(child, 'father' if self.gender == 'M' else 'mother', self)

    def children(self, gender=None):
        return list(filter(lambda child: child.gender == gender or
                           gender is None, self._children))

    def is_direct_successor(self, person):
        return person in self.children() or self in person.children()
