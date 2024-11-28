
# py -3 dumb_gen.py > README.md

import glob

flist = glob.glob('*.png')
flist.sort()

print('''# Screenshots

''')
for fname in flist:
    print('''`%s`

![image](%s)
''' % (fname, fname, ))
