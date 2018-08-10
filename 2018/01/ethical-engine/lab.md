## The Ethical Engine

Content warning: you will be making imaginary life-or-death choices in this lab.

One of the most disruptive technologies currently under development is the self-driving car. [Tesla just announced their electric trucks](https://www.theverge.com/2017/11/16/16667366/tesla-semi-truck-announced-price-release-date-electric-self-driving) - likely to have similar self-driving capabilities as their other vehicles - which raises the question of [what will happen to the 3.5 million truckers in the US](https://www.theguardian.com/technology/2016/jun/17/self-driving-trucks-impact-on-drivers-jobs-us). Google's sister company Waymo is [set to launch a commercial driverless taxi service in Phoenix](https://arstechnica.com/cars/2017/10/report-waymo-aiming-to-launch-commercial-driverless-service-this-year/), and Uber has made it their explicit goal to [convert their entire fleet to driverless cars](https://www.washingtonpost.com/business/economy/uber-signs-deal-to-buy-24000-autonomous-vehicles-from-volvo/2017/11/20/d6038f28-ce2a-11e7-81bc-c55a220c8cbe_story.html); as you might imagine, [taxi companies are not happy about this development](http://money.cnn.com/2017/01/10/technology/new-york-self-driving-cars-ridesharing/index.html). Most major car manufacturers including Ford and Mercedes-Benz are also working on self-driving cars, with many already including lane guidance and automatic parking in their commercial models.

*TODO: update article links*

Much more immediate than the societal impact, however, are ethical problems about how a self-driving car should behave. This is reminiscent of the "trolley problem" in philosophy, which [Wikipedia](https://en.wikipedia.org/wiki/Trolley_problem) describes thus:

> There is a runaway trolley barreling down the railway tracks. Ahead, on the tracks, there are five people tied up and unable to move. The trolley is headed straight for them. You are standing some distance off in the train yard, next to a lever. If you pull this lever, the trolley will switch to a different set of tracks. However, you notice that there is one person tied up on the side track. You have two options:
> 
> * Do nothing, and the trolley kills the five people on the main track.
> * Pull the lever, diverting the trolley onto the side track where it will kill one person.
> 
> Which is the most ethical choice?

Imagine that you and some passengers are in a self-driving car, when several people suddenly run onto the road in front of the car. Should the self-driving car:

* swerve, potentially hitting storefronts and killing you and your passengers? Or,
* keep going, potentially hitting and killing the pedestrians?

This lab asks you to explore this ethical dilemma. Credit goes to Evan Peck of Bucknell University and  Justin Li of Occidental College for developing/refining this assignment.

### Part 1

*TODO: move this to the daily assignment, have students complete before coming to class.*

From the starter files, run `manual.py`. This file will present you with 60 scenarios, with different passengers and pedestrians, in which you must decide which group to save. As a group, work through all 60 scenarios and decide who you would save in each. Take as long as necessary for each one, and aim to answer as truthfully as possible. Your responses will be saved into a timestamped log file.

Once you have gone through 60 scenarios, you will be given a summary of who you have saved. Upload this summary to Moodle (*upload the manual log file*). Bring a copy of this summary to class as well.

*This next part is done in class, at the start. Might want to put this on a slide as the starting "thought question" of the day.*

Start by comparing your manual statistics summary with your partner's. What similarities are there? What are the key differences? Talk briefly about the decision criteria you used, and again, note similarities and differences.

<div style="page-break-after:always"></div>

### Part 2

For this part of the lab, imagine you and your partner are the programmers writing the decision process for a self-driving car. In `automatic.py`, there is a function called `automatic_decision`. Your job is to come to a consensus with your partner on a decision process you are both comfortable with, and then replicate this decision process as much as possible in this function.

The `automatic_decision` function takes a `Scenario` instance, and must return which group to save - either `"passengers"`, or `"pedestrians"`. `Scenario` objects have the following member variables:

* `passengers`, a list of Person objects that describe the passengers in the car
* `pedestrians`, a list of Person objects that describe the pedestrians

`Person` objects have the following member variables:

* `charType`, which describes whether the `Person` is `"human"`, `"cat"`, or `"dog"`
* `age`, which describes whether the human is `"baby"`, `"child"`, `"adult"`, or `"elderly"`
* `gender`, which describes whether the human is `"male"`, `"female"`, or `"nonbinary"`
* `bodyType`, which describes whether the human adult is `"overweight"`, `"athletic"`, or `"average"`
* `profession`, which describes whether the human adult is `"doctor"`, `"CEO"`, `"unemployed"`, or `"unknown"`
* `pregnant`, which is `True` if the human adult female is pregnant, and is `False` otherwise
* `criminal`, which is `True` if the human adult has a criminal (felony charge) history, and is `False` otherwise
* `homeless`, which is `True` if the human is currently homeless and is `False` otherwise

All values will be set to `None` if they do not apply (ie. `pregnant` will be `None` for anyone who is not a human adult female).

**Before you begin coding**, sketch out the algorithm for your decision process **on paper**. What criteria are you using? How much weight are you giving to each criteria? In the case of "ties", what is the tiebreaker? (Note: While you are sketching this out, you will not have access to the lab computer for coding.)

Once you've finished designing your decision algorithm, go ahead and implement it in Python (in the `automatic_decision` function). Run and test your implementation.

**Do not** refer back to the statistics from your manual decisions as you write this function. Note that your function *must* return either `"passengers"` or `"pedestrians"` for any given scenario. Failure to do so will result in an error. Running `automatic.py` will apply your function to 60 random scenarios.


### Part 3

With your partner, answer the following questions:

1. Consider your manual decision making process.
    * Are there attributes of the passengers and pedestrians that had a higher (or lower) survival rate, but that was not a conscious factor in your decision process?
    * What attributes went into your decisions? Does that attribute positively or negatively affect that person’s survival? Why did you consider those attributes?
    * Is the use of those attributes to make those decision "fair" or "ethical" or "moral"? Why/Why not?

2. Run `find_difference.py`, which will run your function on the same 60 scenarios you manually worked through, and show you the scenarios where your automatic and manual decisions differed, as well as the statistics for your automatic decisions **TODO change code to calculate stats on automatic decisions**. Answer the following questions:
    * How accurately did your automatic model match up with your manual decisions?
    * For each scenario where your manual and automatic decisions disagreed, explain why. What were you considering when you made the decision manually? What did the automatic decision not take into account, or what did it take into account that it shouldn’t?

3. Change the last lines of automatic.py to run on 100,000 random scenarios. Include these statistics in your submission. Compare the simulated rates of being saved within each attribute (age, gender, etc.). Assign the attribute into one of these categories:
    * Category 1: Deliberately used in decision, and the survival rates reflect what you intended
    * Category 2: Deliberately used in decision, but the survival rates do not reflect what you intended
    * Category 3: Not explicitly used in decision, but the survival rates are not equal between groups
    * Category 4: Not explicitly used in decision, and the survival rates are equal between groups
For every attribute in Category 2, explain why the statistics do not reflect your (explicit) intented decision process. For every attribute in Category 3, explain why the survival rates are not equal despite not being used in your decision process.

4. Working with another pair, explain to each other how you made your automatic decisions and compare your statistics from the previous question.
    * How do the decision processes differ? What was the reasoning behind each difference?
    * Did that lead to different statistics, in either ranking or in survival rate?
    * Which decision process would you prefer to be in a self-driving car? Why?

5. Based on this exercise, what are some challenges to building (and programming) ethical self-driving cars?

*NOTE for execution: Have students rewrite code/decision engine for HW assignment, based on their discussions.*

### Submission

*automatic.py, log files, text file w/ answers to these questions. Done as HW.*
