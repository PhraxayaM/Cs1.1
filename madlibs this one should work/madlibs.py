def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input



adject1 = user_input("Type an adjective ")
animal = user_input("Type an animal ")
verb = user_input("Type a verb ")
adject2 = user_input("Type an adjective ")
noun = user_input("Type a noun ")
adject3 = user_input("Type an adjective ")
numb = user_input("Type a number ")


story = """ Five years ago, expert sea diver and Naval Captain Jonas Taylor encountered a  {} {}
in the unexplored recesses of the Mariana Trench that forced him to abort his mission and {} half his crew.
Though the tragic incident earned him a {} {}, what ultimately cost him his career, his marriage and any
semblance of honor was his unsupported and {} claims of what caused it - an attack on his vessel by a mammoth,
70-foot xerinae, believed to be extinct for more than {} years. But when another priest lies sunk and disabled
at the bottom of the ocean - carrying his ex-wife among the team onboard - he is the one who gets the call.""".format(adject1, animal, verb, adject2, noun, adject3, numb)

print(story)
