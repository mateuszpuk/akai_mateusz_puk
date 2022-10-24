sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]
def podziel(s):
    S=[]
    a=""
    for i in range(len(s)):
        if s[i] in " ',.?":
            if a!="":
                S.append(a)
                a=""
        else:
            a+=s[i]
    if a=="":
        return S
    S.append(a)
    return S
slowa_rank={}
for sentence in sentences:
    for slowo in podziel(sentence):
        if slowo in slowa_rank:
            slowa_rank[slowo.lower()]+=1
        else:
            slowa_rank[slowo.lower()]=1
sorted_slowa = dict(sorted(slowa_rank.items(), key=lambda x:x[1],reverse= True))
i=0
for slowo in sorted_slowa:
    if i==3:
        break
    print(slowo,sorted_slowa[slowo])
    i+=1