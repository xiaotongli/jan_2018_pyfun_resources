# import the text
# parse the file into sections
    # create some association with the
    # section_numbers and their text
# display PROLOGUE text to user
# ask the user for input?
# return back (print) whatever is assoc with that input

with open("narnia.txt", "r") as narnia:
    key = ""
    while key != "PROLOGUE:":
        key = narnia.readline().strip()

    # keys = section_number
    # vals = sections_text
    sections = {}

    # continue processing the file until we get to the next section
    text = ""
    for line in narnia:

        if line.strip().isdigit():
            # store our dictionary stuff and move on
            sections[key] = text
            # print(key)
            # print(text)
            key = line.strip()
            text = ""
            # print(len(sections))
            # print(sections)
            # break
        else:
            # print("yay i read the else part")
            # print(line)
            text+=line
            # print(text)
    sections[key]=text
    # print(len(sections))
    # for key in range(100,341):
    #     if str(key) not in sections:
    #         print("{} key not found".format(key))
    # print(sections)

    print(sections["PROLOGUE:"])
    pg = ""
    while pg != "q":
        pg = input("Enter a page number: ")
        if pg in sections:
            print(sections[pg])
    print("Game Over")
