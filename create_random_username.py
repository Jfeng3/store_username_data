from random import randint
def get_random_word(count):
    ''' create random string for testing purpose'''
    for i in xrange(count):
        len = randint(1,20)
        s = ''.join(chr(97 + randint(0, 25)) for i in range(len))
        yield s
        
if __name__=='__main__':
    count = 100000
    with open('store2.txt','wb') as f:
        for word in get_random_word(count):
            f.write(word+'\n')