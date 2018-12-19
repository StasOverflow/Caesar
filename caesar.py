to_encode = 'Hello, My dearest friend, im here for an absolutely necessary purpose, encode me, pls'\
            'Тут еще присутствует 1235569990немножечко русского рукописного текста, вместе с буквами и ё Я я'


def do_caesar_stuff(string_to_encode, magic_number, decode=True):
    string_encoded = ''
    for ch in string_to_encode:
        ch = ord(ch)
        if ch >= ord('0'):
            if ord('A') <= ch <= ord('Z'):
                top_boundary = ord('Z')
                btm_boundary = ord('A')
            elif ord('a') <= ch <= ord('z'):
                top_boundary = ord('z')
                btm_boundary = ord('a')
            elif ord('0') <= ch <= ord('9'):
                top_boundary = ord('9')
                btm_boundary = ord('0')
            elif ord('А') <= ch <= ord('Я'):
                top_boundary = ord('Я')
                btm_boundary = ord('А')
            elif ord('а') <= ch <= ord('я'):
                top_boundary = ord('я')
                btm_boundary = ord('а')

            magic_number = magic_number % (top_boundary - btm_boundary)
            if decode:
                if ch - magic_number <= btm_boundary:
                    ch = ch + (top_boundary - btm_boundary) - magic_number
                else:
                    ch = ch - magic_number
            else:
                if ch + magic_number >= top_boundary:
                    ch = ch - (top_boundary - btm_boundary) + magic_number
                else:
                    ch = ch + magic_number

        ch = chr(ch)
        string_encoded += ch

    return string_encoded


def caesar_encode(string_to_encode, num):
    return do_caesar_stuff(string_to_encode, num, False)


def caesar_decode(string_to_decode, num):
    return do_caesar_stuff(string_to_decode, num, True)


string = caesar_encode(to_encode, -10)

print(string)

string = caesar_decode(string, -10)

print(string)


