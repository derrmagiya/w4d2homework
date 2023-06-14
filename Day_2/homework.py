# Question 1:

# Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.
words = ['this' , 'is', 'a', 'sentence', '.']

def reverse_string(s):
    return s[::-1]

left = 0
right = len(words) - 1

while left < right:
    words[left], words[right] = words[right], words[left]
    words[left] = reverse_string(words[left])
    words[right] = reverse_string(words[right])
    left += 1
    right -= 1

print(words)

# Question 2:

# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def count_words(text):
    word_count = {}
    words = text.split()

    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

result = count_words(a_text)
print(result)

# Qusetion 3

# Use binary search to return the index of the target num

cool_list = [2, 5, 6, 12, 45, 47, 98, 123, 1000]
target = 123

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1

cool_list = [2, 5, 6, 12, 45, 47, 98, 123, 1000]
target = 123

index = binary_search(cool_list, target)
print(index)
