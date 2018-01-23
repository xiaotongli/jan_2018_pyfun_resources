def insert_name(name):
    return "You just inserted <{}> into this sentence.".format(text)

print(__name__)

if __name__ == "__main__":

    text = raw_input("What name do you want to put in a sentence?")
    print(insert_name(text))