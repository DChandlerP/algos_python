def isValidSubsequence(array, seqeunce):
    index = 0
    for number in array:
        if number == seqeunce[index]:
            index += 1
            if index == len(seqeunce):
                return True
    return False
