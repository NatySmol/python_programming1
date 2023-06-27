def ruzne_prvky(seznam):
    seznam = defaultdict(int)
    return len(seznam) == len(set(seznam))
