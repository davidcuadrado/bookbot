def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    character_recount = {}
    for character in text.lower():
        character_recount[character] = character_recount.get(character, 0) + 1
    return character_recount

def sort_character_counts(char_counts):
    # Create a list of dictionaries from the char_counts dict
    sorted_list = [
        {'character': char, 'count': count}
        for char, count in char_counts.items()
    ]

    # Sort by count, from greatest to least
    sorted_list.sort(key=lambda x: x['count'], reverse=True)

    return sorted_list

def print_report(text, text_path):
    num_words = get_num_words(text)
    sorted_list = sort_character_counts(character_count(text))
    print(f'============ BOOKBOT ============'
          f'\nAnalyzing book found at {text_path}'
          f'\n----------- Word Count ----------'
          f'\n Found {num_words} total words'
          f'\n--------- Character Count -------')
    for char_dict in sorted_list:
        if char_dict["character"].isalpha():
            print(f'{char_dict["character"]}: {char_dict["count"]}')
    print('============= END ===============')