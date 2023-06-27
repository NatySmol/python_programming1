zaznamy = ["Miroslav Janča","Pavel Malý","Irena Novotná","Roman Ročák",
           "Jitka Murinová", "Matěj Krejčí","Jiří Neveselý","Tomáš Havelka"]
print(sorted(zaznamy, key = lambda x: (x.split()[1], x.split()[0])))
