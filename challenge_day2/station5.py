#station 5 from Nicolas

# Klaudia 1
# Dan 1

#Amir 3
#David G: 1

#Thessa 4
#Sophie M: 5

#Anna 1
#Younes 2

#Olesya 6
#Younes 2

#Kaisa 1
#David 1

#Maria Paz 2
#Balti 3

def solution_station_5(name: str) -> int:
    lt1 = {"Daeho", "David", "Kaisa", "Oliver", "Sara", "Dan", "Ivar", "Lotte", "Riya", "Vassil", "Twan", "Ester", "Karolina", "Lena", "Margarita", "Anna", "Kien", "Klaudia", "Maliah", "Todd"}
    lt2 = {"Oumaima", "Mathilde", "Marie", "Anita", "Ziyan", "Bernardo", "Eleanor", "Lorijn", "Maria", "Younes", "Yvan", "Henning", "Liangyu", "Maciej", "Toprak", "Chris", "GengXin", "Mingze", "Phoebe"}
    lt3 = {"Betija", "Haider", "Kacper", "Sophie", "Amir", "Baltasar", "Isar", "Jelle", "Nicolas", "David", "Ipek", "Juan", "Marfa", "Maria", "Alissa", "Leopoldo", "Mies", "Jiaying", "Kaixin", "Mai", "Sem", "Tibbe"}
    lt4 = {"Justus", "Julia", "Philip", "Uli", "Vanessa", "Anna", "Ekaterina", "Thessa", "Tongfei", "Yang", "Benedikt", "Jan", "Nadee", "Osjah", "Tim", "Eliana", "Joana", "Peilin", "Pija", "Wenhao"}
    lt5 = {"Afua", "Cristina", "Greta", "Jace", "Laura", "Anna", "Bassant", "Ivan", "Juriaan", "Kiavash"}
    lt6 = {"Keitaro", "Nohemi", "Norina", "Yifan", "Yinan", "Luo", "Nikola", "Olesya", "Sophie", "Tom"}

    if name in lt1:
        return 1
    elif name in lt2:
        return 2 
    elif name in lt3:
        return 3
    elif name in lt4:
        return 4
    elif name in lt5:
        return 5
    elif name in lt6:
        return 6
    else:
        raise ValueError(f"Name {name} not found in any group")
