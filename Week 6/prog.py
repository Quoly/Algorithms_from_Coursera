class HashTable( object ):
    """A data structure that contains a collection of values
       where each value is located by a hashable key.
       No two values may have the same key, but more than one
       key may have the same value.
    """
    __slots__ = ( "table", "size" )
    def __init__( self, capacity=1000000 ):
        """Create a hash table.
           The capacity parameter determines its initial size.
        """
        self.table = [ None ] * capacity
        self.size = 0
    def __str__( self ):
        """Return the entire contents of this hash table,
           one chain of entries per line.
        """
        result = ""
        for i in range( len( self.table ) ):
            result += str( i ) + ": "
            result += str( self.table[i] ) + "\n"
        return result
class _Entry( object ):
    """A private class used to hold key/value pairs"""
    __slots__ = ( "key", "value" )
    def __init__( self, entryKey, entryValue ):
        self.key = entryKey
        self.value = entryValue
    def __str__( self ):
        return "(" + str( self.key ) + ", " + str( self.value ) + ")"
def hash_function( val, n ):
    """Compute a hash of the val string that is in range(0,n)."""
    # return 0
    # return len(val) % n
    return hash( val ) % n
def keys( hTable ):
    """Return a list of keys in the given hashTable.
       (It would be better to return a sequence, but that
         is too advanced.)
    """
    result = []
    for entry in hTable.table:
        if entry != None:
            result.append( entry.key )
    return result
def _locate( hTable, key ):
    """Find the entry in the hash table for the given key.
       If the key is not found, find the first unused location in the table.
       (This is called 'open addressing'.)
       If the entry for the key is found, that entry is returned.
       Otherwise the int index where the key would go in the table is returned.
       Finally if the key is not found and no unusued locations are left,
            the int -1 is returned.
       This function is meant to only be called from within hashtable.
       Callers of this function must be prepared to
       deal with results of two different types, unless they
       are absolutely sure whether the key is in the table
       or not.
    """
    index = hash_function( key, len( hTable.table ) )
    startIndex = index # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = ( index + 1 ) % len( hTable.table )
        if index == startIndex:
            return -1
    if hTable.table[ index ] == None:
        return index
    else:
        return hTable.table[ index ]
def contains( hTable, key ):
    """Return True iff hTable has an entry with the given key."""
    entry = _locate( hTable, key )
    return isinstance( entry, _Entry )
def put( hTable, key, value ):
    """Using the given hash table, set the given key to the
       given value. If the key already exists, the given value
       will replace the previous one already in the table.
       If the table is full, an Exception is raised.
    """
    entry = _locate( hTable, key )
    if isinstance( entry, int ): # It's the index of an unused position.
        if entry == -1:
            raise Exception( "Hash table is full." )
        hTable.table[ entry ] = _Entry( key, value )
        hTable.size += 1
    else: # pre-existing entry
        entry.value = value
    return True
def get( hTable, key ):
    """Return the value associated with the given key in
       the given hash table.
       Precondition: contains(hTable, key)
    """
    entry = _locate( hTable, key )
    return entry.value


def TwoSum_HashTable(lst, target):
    '''
    2-SUM algorithm via hash table.
    
    O(n) time.
    '''
    
    hashTable = HashTable()
    
    for x in lst:
        hashTable[x] = True
        
    for x in lst:
        y = target-x
        if y in hashTable and x != y:
            return (x, y)
        
    return None


file_name = 'Numbers.txt' 
f = open(file_name)
file_list = f.readlines()
data = [int(file_list[i]) for i in range(len(file_list))]
count = 0
for t in range(-10000, 10001):
    if(TwoSum_HashTable(data, t)):
        count += 1
print('Via hash table: ' + str(count))