def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))
print(is_prime(1))
print(is_prime(2))

def long_words(words):
    result = []
    for w in words:
        if len(w)>4:
            result.append(w)
    return result

test_words = ["cat", "elephant", "dog", "python", "sun", "banana"]
print(long_words(test_words))
