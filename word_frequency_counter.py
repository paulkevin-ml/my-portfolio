import string
def word_frequency(text):
     text = text.translate(str.maketrans("","",string.punctuation))
     words = text.split()
     counts = {}
     for word in words:
         if word in counts:
             counts[word] = counts[word] + 1
         else:
            counts[word] = 1
     return counts
passage = input("Enter a text to find the number of times each word occurs: \n")
print(word_frequency(passage))
        