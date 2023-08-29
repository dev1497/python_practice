def group_by_anagrams(word_list):
    """
    finds the words that are anagrams and groups them together
    :param word_list: a list of string words
    :return anagramsList: list where anagram words are grouped together and others as such
    O(n*k) time, O(n*k) space
    """
    word_dict = {}
    for word in word_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]

    return list(word_dict.values())


print("List with grouped anagrams is:", group_by_anagrams(["listen", "silent", "hello", "world", "act", "cat"]))
