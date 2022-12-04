# added word "saat" to exceptions


from colorama import Fore
import colorama
colorama.init()
print(f"{Fore.WHITE}", end="")
vowels = "aeiıoöuü"
hard_consonants = "pçtk"
soft_consonants = "bcdğ"
behaviours = {
    "ignoreAllErrors": False,
    "raiseAllErrors": False,
    "errors": {
        "emptyStringInput": {
            "error": IndexError("Enter a word :)"),
            "output": f"{Fore.RED}ERROR: Word can't be empty {Fore.WHITE}",
            "ignored": True
        },
        "noVowelInput": {
            "error": IndexError("A word has to contain at least one valid vowel"),
            "output": f"{Fore.RED}ERROR: A word has to contain at least one valid vowel{Fore.WHITE}",
            "ignored": True
        },
    },
}

def error(name, props = behaviours):
    if (behaviours["ignoreAllErrors"] and not behaviours["raiseAllErrors"]) or behaviours["errors"][name]:
        return behaviours["errors"][name]["output"]
    raise behaviours["errors"][name]["error"]

def equalizeCases(a,b):
    return b.upper() if a.isupper() else b.lower()

def getvowels(word):
    return [i for i in word.lower() if i in vowels]
def lastvowel(word):
    getvowels(word)[-1]
def softenConsonant(word):
    return
def doubleConsonant():
def hardenConsonant():

def addsuffix(word, suffix):
    if suffix.lower() == "n" or suffix.lower() == "m":
        suffix = suffix.upper() if word.isupper() else suffix
        try:
            if word[-1].lower() in vowels:
                if word.lower() in ("o", "bu", "şu"):
                    return word + equalizeCases(word, "nu") + suffix
                elif word.lower() == equalizeCases(word, "su"):
                    return word + equalizeCases(word, "yu") + suffix
                elif word.lower() in ("ora", "bura", "şura"):
                    return word + equalizeCases(word, "nı") + suffix
                else:
                    if len(word) == 1 or (word[0].isupper() and word[1:].islower()):
                        word = word + "'"
                    return word + suffix
        except IndexError:
            error("emptyStringInput")
        else:
            if word.lower() in ("ben", "biz"):
                return word + "im"
            if word[-1].lower() in hard_consonants and word.lower() not in ("top", "sap", "merak", "saat"):
                word = word[:-1] + soft_consonants[hard_consonants.index(word[-1])]
            try:
                if getvowels(word)[-1] in ("o", "u"):
                    return word + "u" + suffix
            except IndexError:
                return
            if getvowels(word)[-1] in ("a", "ı"):
                if word not in ("kalb","saat"):
                    return word + "ı" + suffix
                else:
                    return word + "i" + suffix
            elif getvowels(word)[-1] in ("ö", "ü"):
                return word + "ü" + suffix
            elif getvowels(word)[-1] in ("e", "i"):
                return word + "i" + suffix
while True:
    x = input("Kelime girin: ")
    if x== "!exit": print(f"{Fore.LIGHTBLUE_EX} Thanks for using {Fore.YELLOW}LercDsgn SuffixAdder{Fore.LIGHTGREEN_EX}! Program terminated successfully. {Fore.WHITE}"); break
    print(addsuffix(x, "m"))
