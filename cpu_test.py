import time
import pickle
a = []
for i in range( 50000 ):
    q = time.time_ns()
    a.append( q )

print( a[0], a[1] )
with open( './timestamp.txt', 'w' ) as f:
    idx = 0
    for time in a:
        f.write( str( idx ) + ', ' + str( ( time - a[0] ) * 1e-9 ) )
        f.write( '\n' )
        idx += 1
