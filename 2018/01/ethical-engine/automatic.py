from audit import audit


def automatic_decision(scenario):
    # *** YOUR CODE GOES HERE ***

    # default to saving the passengers
    return "passengers" 

if __name__ == '__main__':
    audit(automatic_decision, 60, seed=8675309)
