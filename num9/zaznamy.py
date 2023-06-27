zaznamy = ["Miroslav Janča","Pavel Malý","Irena Novotná","Roman Ročák",
           "Jitka Murinová", "Matěj Krejčí","Jiří Neveselý","Tomáš Havelka"]

print(max(zaznamy, key = lambda x: len(x.split()[1])))
