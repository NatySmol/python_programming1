def palindrom(vstup):
    return [slovo for slovo in vstup.split() if slovo == slovo[::-1]]
