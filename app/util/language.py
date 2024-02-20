from PyMultiDictionary import MultiDictionary

dictionary = MultiDictionary()

def get_similar_words(word: str, language_code: str, max_results: int = 5):
    similar_words = dictionary.synonym(language_code, word)
    meaning = dictionary.meaning(language_code, word)
    if meaning:
        meaning = meaning[0]

    if len(similar_words) > max_results:
        similar_words = similar_words[:max_results]

    return meaning, similar_words 



if __name__ == "__main__":
    print(get_similar_words("bonjour", "fr"))