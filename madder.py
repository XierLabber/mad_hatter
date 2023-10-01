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

everything = [ME(generate_word()) for i in range(50)]

def f(me: ME):
    for rubbish in everything:
        me.eat(rubbish)
        rubbish.eat(me)
        me.sunnily_squirm(rubbish)
        rubbish.sunnily_squirm(me)
        me.excitedly_crawl(rubbish)
        rubbish.excitedly_crawl(me)
        me.beautifully_roar(rubbish)
        rubbish.beautifully_roar(me)

name = input('please input your name:')
f(ME(name))