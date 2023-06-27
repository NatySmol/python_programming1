zaznamy = ["Miroslav Janča","Pavel Malý","Irena Novotná","Roman Ročák",
           "Jitka Murinová", "Matěj Krejčí","Jiří Neveselý","Tomáš Havelka"]

seznam = list(map(lambda x: " ".join(x.split()[::-1]), zaznamy))
print(seznam)
