"""
Emmy Veselinov
Project: Mad Libs Generator
"""
import random

story1 = """<NAME> <VERB_PASTtense> the <THINGS> after finding out the
<PEOPLE> brought their own to the party. The event was located in a <ADJECTIVE> <PLACE> where <NAME> became very <FEELING>."""

story2 = """A group of <PEOPLE> ran to pick up the <THINGS> from the <PLACE> before 3:00pm. They went back
to the <PLACE> to drop it off where they came across <NAME> who was <ADVERB> <VERB_PRESENTtense> <THINGS>."""

NAMES = ['Bethany', 'Nick', 'Sam', 'Chris', 'Sarah', 'Andrew', 'Emily', 'Maria', 'Kevin', 'Joe', 'Ashley', 'Liz']
VERBS_PASTtense = ['carried', 'threw', 'removed', 'moved', 'dropped', 'cleaned', 'wrapped', 'stashed', 'stole', 'broke']
VERBS_PRESENTtense = ['replacing', 'polishing', 'decorating', 'hiding', 'comparing', 'packing', 'making', 'cutting', 'biting']
THINGS = ['cakes', 'cups', 'plates', 'tables', 'lamps', 'pillows', 'shirts', 'bags','dresses', 'drinks', 'blankets', 'cameras', 'knives']
PEOPLE = ['doctors', 'girls', 'boys', 'lifeguards', 'bakers', 'teenagers', 'chefs', 'photographers', 'friends', 'women', 'men', 'teachers', 'children']
ADVERBS = ['quickly', 'slowly', 'unexpectedly', 'delibrately', 'calmly', 'weirdly', 'aggressively', 'accidentally', 'repeatedly']
PLACES = ['library', 'cafeteria', 'movie theater', 'auditorium', 'classroom', 'train station', 'aquarium', 'airport', 'supermarket', 'bank']
ADJECTIVES = ['small', 'large', 'freezing' 'quiet', 'noisy', 'abandoned', 'haunted', 'crowded', 'hot', 'clean', 'dirty', 'creepy', 'magical']
FEELINGS = ['sad', 'scared', 'worried', 'happy', 'excited', 'terrified', 'bored', 'obnoxious', 'impatient', 'sleepy', 'angry']

# Generate a random word
def random_word(alist):
    random_choice = random.choice(alist)
    return random_choice
    
# Replace each parts of speech in the story
"""Loop through each word in the sentence and if the word is that specific type of speech,
add onto the new sentence by replacing it with a random word of that type"""

def replace_partsofspeech(sentence):
    new_sentence = ""
    for word in sentence.split():
        result = new_sentence + " "
        if word == "<NAME>":
            new_sentence = result + random_word(NAMES)
        elif word == "<VERB_PASTtense>":
            new_sentence = result + random_word(VERBS_PASTtense)
        elif word == "<VERB_PRESENTtense>":
            new_sentence = result + random_word(VERBS_PRESENTtense)
        elif word == "<THINGS>":
            new_sentence = result + random_word(THINGS)
        elif word == "<THINGS>.": # With a period after <THINGS>
            new_sentence = result + random_word(THINGS) + "." # Add a period
        elif word == "<PEOPLE>":
            new_sentence = result + random_word(PEOPLE)
        elif word == "<ADVERB>":
            new_sentence = result + random_word(ADVERBS)
        elif word == "<PLACE>":
            new_sentence = result + random_word(PLACES)
        elif word == "<ADJECTIVE>":
            new_sentence = result + random_word(ADJECTIVES)
        elif word == "<FEELING>":
            new_sentence = result + random_word(FEELINGS)
        elif word == "<FEELING>.":
            new_sentence = result + random_word(FEELINGS) + "." 
        else:
            new_sentence = result + word
    return new_sentence
    

def tests():
    # Orignial sentences
    print("Original Mad libs template: ")
    print("---------------------------------------------------------")
    print(story1)
    print(story2)
    print() #blank line to keep it organized
    # Mad lib outputs
    print("Mad libs output: ")
    print("---------------------------------------------------------")
    print(replace_partsofspeech(story1))
    print(replace_partsofspeech(story2))


if __name__ == "__main__":
    tests()
    