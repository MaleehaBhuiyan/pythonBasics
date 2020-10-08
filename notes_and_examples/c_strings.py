#Working with strings

print("Giraffe Academy")

print("Giraffe\nAcademy")

print("Giraffe\"Academy")

print("Giraffe\Academy")

phrase = "Giraffe Academy"
print(phrase + " is cool")

phrase = "Giraffe Academy"
print(phrase.lower())

phrase = "Giraffe Academy"
print(phrase.upper())

phrase = "Giraffe Academy"
print(phrase.isupper())

phrase = "Giraffe Academy"
print(phrase.upper().isupper())

phrase = "Giraffe Academy"
print(len(phrase))

phrase = "Giraffe Academy"
print(phrase[0])

phrase = "Giraffe Academy"
print(phrase.index("G"))

phrase = "Giraffe Academy"
print(phrase.index("a"))

phrase = "Giraffe Academy"
print(phrase.index("Acad"))

#will give an error
phrase = "Giraffe Academy"
print(phrase.index("z"))

phrase = "Giraffe Academy"
print(phrase.replace("Giraffe", "Panda"))