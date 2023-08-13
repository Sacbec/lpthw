import sys # importar sys

script, input_encoding, error = sys.argv  # atrapar variables con sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline() # ¿por que solo una linea?
    if line: # si la linea tiene contenido
        print_line(line, encoding, errors)
        return main(language_file, encoding,errors)
    
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<->", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
