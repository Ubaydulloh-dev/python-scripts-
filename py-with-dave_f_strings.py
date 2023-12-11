person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins)
print(message)

message2 = "\n{} has {} coins left.".format(person, coins)
print(message2)

message3 = "\n{1} has {0} coins left.".format(coins, person)

print(message3)

message4 = "\n{person} has {coins} coins left.".format(
    coins=coins, person=person)
print(message4)

player = {'person': "Dave", 'coins': 3}

message4 = "\n{person} has {coins} coins left.".format(**player)
print(message4)


# F-strings! This is the way.

message5 = f"\n{person} has {coins} coins left."

name = "Bro"
message6 = f"\n{person} has {coins} coins left."
print(message6)

message6 = f"\n{person.lower()} has {2 * 5} coins left."
print(message6)


message6 = f"\n{player['person'].upper()} has {2 * 5} coins left."
print(message6)


#####
# You can pass fomatting options.

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")


for num in range(1, 11):
    print(f"{num} devided by 4.52 is {num / 4.52:.2%}")


# lesson n13
