import json
from Earley import Earley
from Rule import Rule

def main() -> None:
    file = open('grammar.json', 'r')

    data = json.load(file)

    rules = []
    for raw_rule in data['rules']:
        exploded_rule = raw_rule.split(' ')
        rules.append(Rule(exploded_rule[0], exploded_rule[2]))

    earley = Earley(word=data['check'], rules=rules)

    print('Правила:')
    print('\n'.join(map(str, earley.rules)))

    answer = 'принадлежит' if earley.get_answer() else 'НЕ принадлежит';
    print(f'\nСлово {earley.word} {answer} языку.')

    file.close()

if __name__ == "__main__":
    main()