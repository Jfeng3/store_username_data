

class Trie:

    def __init__(self):
        # only have key , no values for this specific problem, 
        # can easily extend to store key value pair
        self.path = {}
        self.end = False # indicate end of a key
        

    def add(self, key):
        '''add a key to the trie'''
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            node = Trie()
            self.path[head] = node

        if len(key) > 1:
            remains = key[1:]
            node.add(remains)
        else:
            node.end = True # indicating end of the key

    def __contains__(self, key):
        '''check if the trie contains a key'''
        try:
            head = key[0]
            if head in self.path:
                node = self.path[head]
            else:
                raise KeyError(key)
            if len(key) > 1:
                remains = key[1:]
                try:
                    return node.__contains__(remains)
                except KeyError:
                    raise KeyError(key)
            elif node.end:
                return True
            else:
                raise KeyError(key)
        
        except KeyError:
            return False
        return True

    def __len__(self):
        n = 1 if self.end else 0
        for k in self.path.keys():
            n = n + len(self.path[k])
        return n

    