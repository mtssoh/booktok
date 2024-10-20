import string
def sort_on(diccionario):
    return diccionario["cantidad"]

def report(cont, words):
    print("REPORTE DE PALABRAS")
    print(f"{words} palabras encontradas")
    print("\n")
    for i in range(0, len(cont)):
        print(f"La letra {cont[i]["letra"]} ha sido encontrada {cont[i]["cantidad"]} veces.")

def count_char(contents):
    low_char = contents.lower()
    cont = []
    letras = string.ascii_lowercase

    for letra in letras:
        diccionario = {"letra": letra, "cantidad" : 0}
        cont.append(diccionario)

    for letra in low_char:
        if letra in letras:
            for i in range (0, len(cont)):
                if cont[i]["letra"] == letra:
                    cont[i]["cantidad"] += 1

    cont.sort(reverse=True, key=sort_on)
    return cont

    
        

def count_words(contents):
    words = contents.split()
    return len(words)


def main ():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

    cont = count_char(file_contents)
    words = count_words(file_contents)
    report(cont, words)

    
    


main()