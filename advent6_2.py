foo = sum([len(set.intersection(*map(set,g.split('\n')))) for g in open('6.txt','r').read().split('\n\n')])
