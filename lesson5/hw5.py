import re

def main():
    def normalize():
        text = input("Please enter the text you want to trasnlate: ")
        alphabet   = {ord('А'): 'A',
                    ord('Б'): 'B',
                    ord('В'): 'V',
                    ord('Г'): 'G',
                    ord('Д'): 'D',
                    ord('Е'): 'E',
                    ord('Ё'): 'Je',
                    ord('Ж'): 'Zh',
                    ord('З'): 'Z',
                    ord('И'): 'I',
                    ord('Й'): 'Y',
                    ord('К'): 'K',
                    ord('Л'): 'L',
                    ord('М'): 'M',
                    ord('Н'): 'N',
                    ord('П'): 'P',
                    ord('Р'): 'R',
                    ord('С'): 'S',
                    ord('Т'): 'T',
                    ord('У'): 'U',
                    ord('Ф'): 'F',
                    ord('Х'): 'Kh',
                    ord('Ц'): 'C',
                    ord('Ч'): 'Ch',
                    ord('Ш'): 'Sh',
                    ord('Щ'): 'Jsh',
                    ord('Ъ'): 'Z',
                    ord('Ы'): 'Ih',
                    ord('Ь'): 'Jh',
                    ord('Э'): 'Eh',
                    ord('Ю'): 'Ju',
                    ord('Я'): 'Ja',
                    ord('а'): 'a',
                    ord('б'): 'b',
                    ord('в'): 'v',
                    ord('г'): 'g',
                    ord('д'): 'd',
                    ord('е'): 'e',
                    ord('ё'): 'je',
                    ord('ж'): 'zh',
                    ord('з'): 'z',
                    ord('и'): 'i',
                    ord('й'): 'y',
                    ord('к'): 'k',
                    ord('л'): 'l',
                    ord('м'): 'm',
                    ord('н'): 'n',
                    ord('п'): 'p',
                    ord('р'): 'r',
                    ord('с'): 's',
                    ord('т'): 't',
                    ord('у'): 'u',
                    ord('ф'): 'f',
                    ord('х'): 'kh',
                    ord('ц'): 'c',
                    ord('ч'): 'ch',
                    ord('ш'): 'sh',
                    ord('щ'): 'jsh',
                    ord('ъ'): 'z',
                    ord('ы'): 'ih',
                    ord('ь'): 'jh',
                    ord('э'): 'eh',
                    ord('ю'): 'ju',
                    ord('я'): 'ja'}

        translate_text = text.translate(alphabet) 
        translated = re.sub(r"\W", "_", translate_text)
        
        return translated

    print(normalize())

if __name__=="__main__":
    main()


