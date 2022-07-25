# response = []

# while True:
#     user_input = input("Say something: ")
#     response.append(user_input)
#     if user_input == "\end":
#         for i in range(0,len(response)-1):
#             print(response[i])
#         break
#     else:
#         continue

def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)    #return f"{capitalized}?"
    else:
        return "{}.".format(capitalized)

#print(sentence_maker("how are you"))

results = []

while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))