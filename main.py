import pandas
student_data_frame = pandas.DataFrame(student_dict)


alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict={row.letter:row.code for(index,row) in alphabets.iterrows()}


def list_maker():
    message = input("What is your word? ").upper()
    result=[]
    for x in message:
        for y in alphabet_dict:
            if x == y :
                result+=[alphabet_dict[y]]
    return result





