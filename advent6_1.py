foo = sum([len(set(g.replace('\n',''))) for g in open('6-1.txt','r').read().split('\n\n')])