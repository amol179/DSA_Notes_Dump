def record_lecture():
    # Read number of words in the lecture and number of words in each language
    n, m = map(int, input().split())

    # Create a dictionary to map first language words to second language words
    word_map = {}
    for _ in range(m):
        a, b = input().split()
        word_map[a] = b

    # Read the lecture text
    lecture_text = input().split()

    # Record the lecture according to the given rules
    recorded_lecture = []
    for word in lecture_text:
        word_in_first_language = word
        word_in_second_language = word_map[word]

        # Choose the shorter word, or the first language's word if they are of equal length
        if len(word_in_first_language) <= len(word_in_second_language):
            recorded_lecture.append(word_in_first_language)
        else:
            recorded_lecture.append(word_in_second_language)

    # Output the recorded lecture
    print(" ".join(recorded_lecture))


# Call the function
record_lecture()
