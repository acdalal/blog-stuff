from random import seed as set_seed
from collections import defaultdict
from datetime import datetime

from scenario import Scenario


def serialize_people(people):
    people_attributes = []
    for person in people:
        person_attributes = []
        for attribute, value in vars(person).items():
            if value is not None:
                person_attributes.append('{}={}'.format(attribute, value))
        people_attributes.append(','.join(person_attributes))
    return ' '.join(people_attributes)


def log_scenario(log_file, scenario, decision):
    with open(log_file, 'a') as fd:
        fd.write(serialize_people(scenario.passengers))
        fd.write('|')
        fd.write(serialize_people(scenario.pedestrians))
        fd.write('|')
        fd.write(decision)
        fd.write('\n')


def get_log_file(name):
    return name + '.' + datetime.now().strftime('%Y%m%d%H%M%S') + '.log'


def pretty_print_table(table):
    headers = [
        ['Attribute', '% Saved', 'Encountered'],
        ['---------', '-------', '-----------'],
    ]
    table = headers + table
    maxes = [max(len(row[i]) for row in table) for i in range(3)]
    for row in table:
        line = []
        for i, value in enumerate(row):
            line.append(value + ((maxes[i] - len(value)) * ' '))
        print('  '.join(line))


def add_to_count(people, count_dict):
    for person in people:
        for attribute, value in vars(person).items():
            if value is not None:
                key = '{}={}'.format(attribute, value)
                count_dict[key] += 1


def audit(decision_fn, num_scenarios=100000, seed=None):
    log_file = get_log_file(decision_fn.__name__)
    if seed is not None:
        set_seed(seed)
    for _ in range(num_scenarios):
        scenario = Scenario(youInCar=False, legalCrossing=False, pedsInLane=True)
        decision = decision_fn(scenario)
        if decision not in ['passengers', 'pedestrians']:
            print(scenario)
            message = 'Expected "passengers" or "pedestrian", '
            message += 'but got "{}" instead'.format(decision)
            raise ValueError(message)
        log_scenario(log_file, scenario, decision)
    calculate_stats(log_file)


def calculate_stats(log_file):
    count_saved = defaultdict(int)
    count_total = defaultdict(int)
    with open(log_file) as fd:
        for line in fd.readlines():
            passengers, pedestrians, decision = line.strip().split('|')
            scenario = Scenario.from_string(passengers, pedestrians)

            # add saved population to count_saved
            if decision == 'passengers':
                add_to_count(scenario.passengers, count_saved)
            elif decision == 'pedestrians':
                add_to_count(scenario.pedestrians, count_saved)
            add_to_count(scenario.passengers, count_total)
            add_to_count(scenario.pedestrians, count_total)

    keys = set(count_saved.keys()).union(set(count_total.keys()))
    count_percents = {}
    for key in keys:
        count_percents[key] = count_saved[key] / count_total[key]
    table = []
    for key, percent in sorted(count_percents.items(), key=(lambda kv: kv[1]), reverse=True):
        table.append([key, '{:2.2%}'.format(percent), str(count_total[key])])
    pretty_print_table(table)


def main():
    log_file = 'FIXME'
    calculate_stats(log_file)


if __name__ == '__main__':
    main()
