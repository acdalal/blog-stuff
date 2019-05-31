from audit import audit

LOG_FILE = 'decisions.log'


def manual_decision(scenario):
    print()
    print(40 * '-')
    print()
    print(scenario)
    print()
    response = ' '
    while response.lower() not in ['a', 'b']:
        response = input("Enter 'a' to save the passengers, or 'b' to save the pedestrians: ")
    if response.lower() == 'a':
        return 'passengers'
    else:
        return 'pedestrians'


if __name__ == '__main__':
    audit(manual_decision, 60, seed=8675309)
