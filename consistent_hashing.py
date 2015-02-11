from hash_ring import HashRing

memcache_servers = ['192.168.0.246:11212',
                    '192.168.0.247:11212',
                    '192.168.0.249:11212']
def consistent_hash(filename,memcache_servers):
'''store each key in the file to memcache servers'''
    ring = HashRing(memcache_servers)
    with open(filename,'rb') as f:
            for line in f:
                server = range.get_node(line.strip())
                # then hash or use trie on this server to store the key
    
