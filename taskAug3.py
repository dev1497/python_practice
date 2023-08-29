from collections import Counter

global_sum = 1


def sequence_sum(number):
    """
    calculates sequence of sums by multiplying 3 and adding 2
    :param number:int value upto which sum is calculated
    :return: global_sum having sequence of sums
    O(k) time ,O(k) space complexity
    """
    global global_sum
    sum = 1
    while sum <= number:
        sum = (sum * 3)
        sum += 2
        global_sum = global_sum + sum
    return global_sum


print("Sequence sum is:", sequence_sum(10))


def count_frequency(sentence):
    """
    counts frequency of each word in a sentence
    :param sentence: string of words
    :return:a dictionary having frequency of each word
    O(n+m) time ,O(n+m) space complexity
    """
    sentence = sentence.lower()
    sentence = sentence.replace(".", "")
    sentence = sentence.split()
    return Counter(sentence)


text = input("Enter string:")
print(text)
print(count_frequency(text))


def get_sorted_even(numbers):
    """
    finds even numbers from list and sorts them
    :param numbers: a list of unsorted numbers
    :return: list of even numbers in ascending number
    O(n) time ,O(n) space
    """
    numbers = [x for x in numbers if x % 2 == 0]
    numbers.sort()
    return numbers


print("Even numbers in ascending order are:", get_sorted_even([8, 7, 2, 11, 4, 9, 6, 3, 8]))
