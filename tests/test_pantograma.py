import unicodedata


LIST_LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def normalize_sentence(sentence):
    letter_normalize = (unicodedata.normalize('NFD', sentence).encode('ascii', 'ignore')).decode()
    return letter_normalize.lower()


def pantograma(sentence):
    sentence = normalize_sentence(sentence)
    for letter in LIST_LETTERS:
        if letter not in sentence:
            return False
    return True


def test_len_pantograma():
    sentenca = normalize_sentence(' Quem traz CD, LP, fax, engov e whisky JB? (29 letras).\
        Desafio: Dada uma string, detecte se ela é ou não um Pantograma retornand')

    assert len(sentenca) >= 26


def test_is_not_in_letters():
    assert pantograma('a') is False


def test_is_not_string():
    assert str(1).isalpha() is False


def test_len_pantograma_lower_letters():
    sentenca = normalize_sentence('Quem traz CD, LP, fax, engov e whisky JB? (29 letras).')
    assert pantograma(sentenca) is True
