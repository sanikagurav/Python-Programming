def count_case(sentence):
    # Initialize counters
    upper_count = 0
    lower_count = 0

    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is an uppercase letter
        if char.isupper():
            upper_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lower_count += 1

    # Print the results
    print("Number of uppercase letters:", upper_count)
    print("Number of lowercase letters:", lower_count)

# Get input from the user
user_sentence = input("Enter a sentence: ")

# Call the function with the user input
count_case(user_sentence)
