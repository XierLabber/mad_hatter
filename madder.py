import random

def generate_word():
    len = random.randint(5, 10)
    word = ['='] * len
    for i in range(len):
        word[i] = chr(random.randint(0, 25) + ord('a'))
    return ''.join(word)

class ME(object):
    def __init__(self, name):
        self.name = name
    
    def do_str(self, person, s):
        if random.randint(0, 110) % 2 == 0:
            print(self.name, s, person.name)
        elif random.randint(0, 110) % 3 == 0:
            print(self.name, "is tired and does not want to " + s, person.name)
        else:
            print(self.name, 'fail to', s, person.name, 'and eats a hamburger with Mr.Eight')

    def eat(self, person):
        self.do_str(person, 'eats')
    
    def sunnily_squirm(self, person):
        self.do_str(person, 'squirms sunnily with')
    
    def excitedly_crawl(self, person):
        self.do_str(person, 'crawls excitedly with')

    def beautifully_roar(self, person):
        self.do_str(person, "roars beautifully with")

def fuck_world(me: ME, len = 5):
    everything = [ME(generate_word()) for i in range(len)]
    for rubbish in everything:
        if random.randint(0, 1) == 0:
            random_do = random.randint(0, 3)
            if random_do == 0:
                me.eat(rubbish)
            elif random_do == 1:
                me.sunnily_squirm(rubbish)
            elif random_do == 2:
                me.excitedly_crawl(rubbish)
            elif random_do == 3:
                me.beautifully_roar(rubbish)
        else:
            random_do = random.randint(0, 3)
            if random_do == 0:
                rubbish.eat(me)
            elif random_do == 1:
                rubbish.excitedly_crawl(me)
            elif random_do == 2:
                rubbish.sunnily_squirm(me)
            elif random_do == 3:
                rubbish.beautifully_roar(me)

name = input('please input your name: ')
n_items = input('how many times would you like to like this world: ')
fuck_world(ME(name), int(n_items))