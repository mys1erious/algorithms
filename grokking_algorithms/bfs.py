# Using python lists (slow)
class ListQueue:
    def __init__(self, item=None):
        self.__data = []

        if item:
            self.enqueue(item)

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        return self.__data.pop(0)

    def __str__(self):
        return f'{self.__data}'


# Using Linked List
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.previous = None

    def __repr__(self):
        return f'{self.item}'


class LLQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)

        if not self.tail:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        self.length += 1

    def enqueue_multiple(self, arr):
        for item in arr:
            self.enqueue(item)

    def dequeue(self):
        item = self.head.item
        self.head = self.head.next

        if self.head:
            self.head.previous = None

        self.length -= 1
        if self.length == 0:
            self.tail = None

        return item


class Person:
    def __init__(self, name, seller=False):
        self.name = name
        self.friends = set()
        self.seller = seller

    def add_friend(self, person):
        self.friends.add(person)

    def add_friends(self, people):
        self.friends.update(people)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'
        # return f'{self.name}: ({self.friends})'


def imitate_social_graph():
    friends_template = {
        'me': ['alice', 'bob', 'claire'],
        'alice': ['peggy'],
        'bob': ['anuj', 'peggy'],
        'claire': ['thom', 'jonny']
    }

    people_names = ['me', 'alice', 'bob', 'claire', 'peggy', 'anuj', 'thom', 'jonny']
    graph = [Person(name) if name != 'thom' else Person(name, seller=True) for name in people_names]

    for person in graph:
        friends_names = friends_template.get(person.name)

        if friends_names:
            friends = [person for person in graph if person.name in friends_names]
        else:
            friends = []

        person.add_friends(friends)
    return graph


# Breadth-first-search
def bfs(initial_person):
    search_q = LLQueue()
    search_q.enqueue(initial_person)
    visited = []

    while search_q:
        person = search_q.dequeue()
        if person not in visited:
            if person.seller:
                print(f'{person} is a seller')
                return True
            print(f'{person} is not a seller')
            search_q.enqueue_multiple(person.friends)
            visited.append(person)

    return False


if __name__ == '__main__':
    graph = imitate_social_graph()

    me = None
    for person in graph:
        if person.name == 'me':
            me = person
            break

    if me:
        bfs(me)
