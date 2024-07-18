sentence = "  heute ,  ist    es  schön  "
def remove_whitespace(sentence_):
    return f"{"sentence_ : "}{sentence_} \n {"strip() : "}{sentence_.strip()} \n {"split() :"}{ "".join(sentence_.split(","))} \n {"replace() :"} {sentence_.replace(" ","")}"
print(remove_whitespace(sentence))
