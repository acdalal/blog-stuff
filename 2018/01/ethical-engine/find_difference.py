from scenario import Scenario
from automatic import automatic_decision


def find_difference(manual_file):
    with open(manual_file) as manual_fd:
        for manual_line in manual_fd.readlines():
            passengers, pedestrians, manual_decision = manual_line.strip().split('|')
            scenario = Scenario.from_string(passengers, pedestrians)
            auto_decision = automatic_decision(scenario)
            if manual_decision != auto_decision:
                print(scenario)
                print()
                print('manual decision: ' + manual_decision)
                print('auto decision: ' + auto_decision)
                print(40 * '-')


def main():
    # *** NOTE: Replace this with the name of your manual decision log file ***
    manual_file = 'manual_decision.20181031130021.log'
    find_difference(manual_file)


if __name__ == '__main__':
    main()
