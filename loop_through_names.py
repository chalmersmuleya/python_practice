names = [
    "Naruto Uzumaki",
    "Sasuke Uchiha",
    "Sakura Haruno",
    "Goku",
    "Vegeta",
    "Monkey D. Luffy",
    "Zoro Roronoa",
    "Nami",
    "Edward Elric",
    "Alphonse Elric",
    "Light Yagami",
    "L Lawliet",
    "Mikasa Ackerman",
    "Eren Yeager",
    "Levi Ackerman",
    "Tanjiro Kamado",
    "Nezuko Kamado",
    "Ichigo Kurosaki",
    "Rukia Kuchiki",
    "Killua Zoldyck",
    "Gon Freecss",
    "Saitama",
    "Genos",
    "Kaneki Ken",
    "Todoroki Shoto",
    "Midoriya Izuku",
    "All Might",
    "Erza Scarlet",
    "Natsu Dragneel",
    "Jiraiya" 
]

for name in names:
    print ("Hello",name)

for idx, name in enumerate(names,1):    
    print (f"{idx}.{name}")         # Uses an f-string to format the output.
                                    # Prints two spaces (for indentation), then the index number idx, a period ., a space, and then the option text.

#another way to do indexing without enumerate
index = 1  # Start counting at 1
for name in names:
    print(f"  {index}.. {name}")
    index += 1  # Increase index by 1 each time



#count 
count = 0

for name in names:
    if "Naruto" in name:
        count += 1
print(count)

