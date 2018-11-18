text = """Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole,
dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi,
Prosto, długo, daleko, jako morza brzegi."""
vowels = "ieyuo"
for i in vowels:
    print(i + ": ", text.count(i))
