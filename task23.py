sentence ="heute ist es schön"
def check_string(sentence_):
    for s in sentence_:
         if s.isdigit():
          return True
    else :
          return False
print(check_string(sentence))

