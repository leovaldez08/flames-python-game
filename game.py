def get_flames_result(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()

    name_count = {}
    for char in name1:
        if char in name_count:
            name_count[char] += 1
        else:
            name_count[char] = 1

    for char in name2:
        if char in name_count:
            name_count[char] += 1
        else:
            name_count[char] = 1

    common_count = 0
    for count in name_count.values():
        if count > 1:
            common_count += 1

    flames = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(flames) > 1:
        count = common_count % len(flames)
        flames = flames[count + 1 :] + flames[:count]

    return flames[0]


name1 = input("Enter the your name: ")
name2 = input("Enter your crush' name: ")

result = get_flames_result(name1, name2)
print("The FLAMES result for", name1, "and", name2, "is:", result)
