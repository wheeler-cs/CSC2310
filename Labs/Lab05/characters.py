# Imports Section
import csv
import sys
from typing import List
import getopt
from character_class import WizardingCharacter


# Code!
def get_hp_characters() -> List[WizardingCharacter]:
    """
    Comment block
    :return: list of dictionaries
    """
    hp_chars: List[WizardingCharacter] = []
    with open('data/Characters.csv') as csvfile:
        character_reader = csv.reader(csvfile, delimiter=',')
        for row in character_reader:
            try:
                if isinstance(int(row[0]), int):
                    c = WizardingCharacter(row)
                    hp_chars.append(c)
            except ValueError:
                pass
    return hp_chars


# For calling the method
if __name__ == '__main__':
    people: List[WizardingCharacter] = get_hp_characters()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:", ["house="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--house"):
            for p in people:
                if p.house.lower() == a.lower():
                    print(p)
