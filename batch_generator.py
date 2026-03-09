import sys
from main import *

count=int(sys.argv[1])

for i in range(count):
    print("Generating reel",i+1)
    main()