# Read and store the content of invited_names.txt as a list
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Read and store the content of the starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

    # Write a letter for each invited person
    for name in names:
        stripped_name = name.strip()
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(letter_content.replace("[name]", stripped_name))