usage : python search_username.py filename username
example: 
python search_username.py store1.txt tkgjzxk
No! tkgjzxk does not exist in the file

python search_username.py store1.txt ekgjzxk
Yes! ekgjzxk exists in the file

Here I assume each line of input file is a username
store.txt has 1000000 random strings ( average length 10)
store1.txt has 100 random strings ( average length 10)

I use trie to store the usernames and search. The order of seach operation is less than max size of the string, so still constant time. 

There are several trie implementation I tried. 
I implemented my own trie in trie_jie.py file, only have add and __contain__ 2 operations. Only store keys, no values. 

I tested on 1000000 random strings, Obviously the real username might have more prefix and might use less memory. 

memory usage trie_jie.py, obviously pretty bad. 
        Line #    Mem usage    Increment   Line Contents
        ================================================
            13    9.633 MiB    0.000 MiB   @profile
            14                             def store_in_trie(filename):
            15    9.633 MiB    0.000 MiB       '''add all usernames from a file into a tri'''
            16    9.633 MiB    0.000 MiB       t = Trie()
            17 4545.402 MiB 4535.770 MiB       with open(filename,'rb') as f:
            18 4545.402 MiB    0.000 MiB           for line in f:
            19                                         t.add(line.strip())
            20                                 return t
        But the memory usage is pretty bad.
    
memory usage of python standard set

        Line #    Mem usage    Increment   Line Contents
        ================================================
            13   45.344 MiB    0.000 MiB   @profile
            14                             def store_in_trie(filename):
            15                                 '''add all usernames from a file into a tri'''
            16   45.344 MiB    0.000 MiB       t = set()
            17   45.344 MiB    0.000 MiB       with open(filename,'rb') as f:
            18  116.125 MiB   70.781 MiB           for line in f:
            19  116.125 MiB    0.000 MiB               t.add(line.strip())
            20  116.125 MiB    0.000 MiB       return t

memory usage of some other trie implementation datrie from https://pypi.python.org/pypi/datrie/0.1.1

        Line #    Mem usage    Increment   Line Contents
        ================================================
            15   58.961 MiB    0.000 MiB   @profile
            16                             def store_in_trie(filename):
            17                                 '''add all usernames from a file into a tri'''
            18   58.961 MiB    0.000 MiB       t = datrie.Trie(string.ascii_lowercase)
            19   58.961 MiB    0.000 MiB       with open(filename,'rb') as f:
            20   88.934 MiB   29.973 MiB           for line in f:
            21   88.934 MiB    0.000 MiB               t[unicode(line.strip())] = None
            22   88.934 MiB    0.000 MiB       return t


We can see that the memory usage of trie ( standard implementation) is more efficient than hashset
For running time. in the non-scientific experiment i did, trie takes more time than set

    
To support 1000,000,000 users we can use consistent hashing. 
I have not implemented it yet. My idea is for each stirng, use hash(str) get a number then mode to get the position on a circle, then assign the server base on the position. 
A python implementaion would be https://pypi.python.org/pypi/hash_ring/1.3.1. examples are in consistent_hashing.py
