#Inverse string func:
def invertStr(sent):
    sent2 = ""
    for i in range(len(sent)):
        sent2 += sent[len(sent) - (i+1)]
    sent = sent2
    return sent

sen = "Hello, world!"
print("Original sentence: ", sen)
print("After invert: ", invertStr(sen))
input()
