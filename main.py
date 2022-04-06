names = open("./Input/Names/invited_names.txt")
letter = open("./Input/Letters/starting_letter.txt")

starting_letter = letter.read()
name_list = names.read().splitlines()

for name in name_list:
    new_letter = starting_letter.replace("[name]", name)
    print(new_letter)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
