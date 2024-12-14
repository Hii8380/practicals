def longest_word(sentence):
    """Function to find the longest word in the string."""
    words = sentence.split()
    longest = max(words, key=len)
    return longest

def char_frequency(sentence, char):
    """Function to determine the frequency of a particular character in the string."""
    return sentence.count(char)

def is_palindrome(sentence):
    """Function to check whether the string is a palindrome."""
    sentence = sentence.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return sentence == sentence[::-1]

def first_substring_index(sentence, substring):
    """Function to find the index of the first appearance of a substring."""
    return sentence.find(substring)

def word_occurrence(sentence):
    """Function to count the occurrence of each word in the string."""
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    # Take input from the user
    sentence = input("Enter a string: ")

    # a) Longest word
    longest = longest_word(sentence)
    print(f"The longest word is: '{longest}'")

    # b) Frequency of occurrence of a particular character
    char = input("Enter a character to check its frequency: ")
    frequency = char_frequency(sentence, char)
    print(f"The frequency of '{char}' is: {frequency}")

    # c) Palindrome check
    if is_palindrome(sentence):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

    # d) First occurrence index of a substring
    substring = input("Enter a substring to find its first occurrence: ")
    index = first_substring_index(sentence, substring)
    if index != -1:
        print(f"The first occurrence of '{substring}' is at index {index}.")
    else:
        print(f"The substring '{substring}' was not found.")

    # e) Word occurrence count
    word_count = word_occurrence(sentence)
    print("Word occurrences:")
    for word, count in word_count.items():
        print(f"'{word}': {count}")

if __name__ == "__main__":
    main()
