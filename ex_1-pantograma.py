"""
O Pantograma é uma sentença que contem todas as letras do alfabeto, ao menos um vez. Por exemplo, a sentença: Quem traz CD, LP, fax, engov e whisky JB? (29 letras).
Desafio: Dada uma string, detecte se ela é ou não um Pantograma retornando True ou False. Ignore números, pontuações e acentos.

Pantogramas para testes:
Jane quer LP, fax, CD, giz, TV e bom whisky.[2] (30 letras)
TV faz quengo explodir com whisky JB. (30 letras)
Vejo xá gritando que fez show sem playback. (35 letras)
Todo pajé vulgar faz boquinha sexy com kiwi. (36 letras)
Vi que ex-janota gordo fez show com playback. (36 letras)
Já fiz vinho com toque de kiwi para belga sexy. (37 letras)
Bancos fúteis pagavam-lhe queijo, whisky e xadrez. (41 letras)
"""

lista_caracteres_especiais = '!#$%&()*+,-./'
lista_acentuacao = 'à,á,â,è,é,ê,ì,í,î,ò,ó,ô,õ,ù,ú,û'
alfabeto = 'abcdefghijklmnopqrstuvwxyz'


def is_pantograma(frase: str):
    frase = frase.lower()
    for c in lista_caracteres_especiais:
        frase = frase.replace(str(c), '')
    for c in lista_acentuacao:
        frase = frase.replace(str(c), 'a')
    frase = frase.replace(' ', '')

    a_alfabeto = ''.join(set(alfabeto))
    a_alfabeto = sorted(a_alfabeto)
    a_frase = ''.join(set(frase))
    a_frase = sorted(a_frase)

    if a_frase == a_alfabeto:
        return True
    else:
        return False


def test_pantograma():
    assert is_pantograma('Jane quer LP, fax, CD, giz, TV e bom whisky') is True
    assert is_pantograma('TV faz quengo explodir com whisky JB') is True
    assert is_pantograma('Vejo xá gritando que fez show sem playback') is True
    assert is_pantograma('Todo pajé vulgar faz boquinha sexy com kiwi') is True
    assert is_pantograma('Vi que ex-janota gordo fez show com playback') is True
    assert is_pantograma('Já fiz vinho com toque de kiwi para belga sexy') is True
    assert is_pantograma('Bancos fúteis pagavam-lhe queijo, whisky e xadrez') is True
