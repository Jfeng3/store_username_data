#Write a program that reads list of 1,000,000 user names from a file and store them in memory. You should implement the following interface that checks whether a user name exists in memory or not. You may use external libraries.
# 
#// return true if the user is in memory, else return false.
#bool checkUser(char * userID);
# 
# 
#Your data structure should be one that provides a quick response even for huge amount of user names. Please also answer the following questions:
#Describe the data structure you have selected and the Order of search operation for a user name.
#How would you improve your solution to support 1,000,000,000 user names?
import trie_jie
import datrie
import string
import sys

class Finder:
    def __init__(self,filename):
        self.filename = filename
        self.trie = None
        
        
    def _store_in_datrie(self, filename):
        '''add all usernames from a file into trie implementation datrie from https://pypi.python.org/pypi/datrie/0.1.1'''
        
        t = datrie.Trie(string.ascii_lowercase)
        with open(filename,'rb') as f:
            for line in f: 
                t[unicode(line.strip())] = None
        return t

    def _store_in_trie_jie(self, filename):
        '''add all usernames from a file into my tri implementation'''
        
        t = trie_jie.Trie()
        with open(filename,'rb') as f:
            for line in f:
                t.add(line.strip())
        return  t
                   
    def exist_user(self, username):
        '''return true if a username is in the file'''
        if not self.trie:
            self.trie = self._store_in_datrie(self.filename)
        return unicode(username) in self.trie
    
if __name__=='__main__':
    filename = 'store1.txt'
    finder = Finder(filename)
    for username in ['a','bb']:
        if finder.exist_user(username):
            print "Yes! {} exists in the file".format(username)
        else:
            print "No! {} does not exist in the file".format(username)
            
    


