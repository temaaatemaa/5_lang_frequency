
def counting(file,amount_of_words,array_of_numiration,array_of_words):
    for x in file:
        x=x.lower()
        word_was_find=0
        for num,i in enumerate(array_of_words):
            if x==i:
                array_of_numiration[num]=array_of_numiration[num]+1
                word_was_find=1
        if (word_was_find==0) or (amount_of_words==0):
            array_of_words.append(x)
            array_of_numiration.append(1)
            amount_of_words=amount_of_words+1
    return amount_of_words




def maxing(file,amount_of_words,array_of_numiration,array_of_words):
    j=1
    while j<=10:
        max=0
        i=1
        while i <= amount_of_words:
            if max<array_of_numiration[i]:
                max=array_of_numiration[i]
                num_for_max=i
            i=i+1
        if max!=0:
            print(array_of_words[num_for_max],array_of_numiration[num_for_max])
            array_of_numiration[num_for_max]=-1
        j=j+1
    return 1


if __name__ == '__main__':
    pass

f = open('txt.txt', 'r+')
file= f.read()
file=file.replace(".","")
file=file.replace(",","")
file=file.split(" ")
amount_of_words=0
array_of_numiration=[0]
array_of_words=[""]

amount_of_words = counting(file,amount_of_words,array_of_numiration,array_of_words)
maxing(file,amount_of_words,array_of_numiration,array_of_words)
