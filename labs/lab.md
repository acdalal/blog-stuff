## The Ethical Engine

**Content warning: you will be making imaginary life-or-death choices in this lab.**

### Before you begin

Please work with your current partner on this lab.

Download this [zip file](allparts.zip), which contains all of the files you will need for this lab. Unzip the file before you begin.

### Introduction

One of the most disruptive technologies currently under development is the self-driving car. [Tesla announced their electric trucks](https://www.theverge.com/2017/11/16/16667366/tesla-semi-truck-announced-price-release-date-electric-self-driving) - likely to have similar self-driving capabilities as their other vehicles - which raises the question of [what will happen to the 3.5 million truckers in the US](https://www.theguardian.com/technology/2016/jun/17/self-driving-trucks-impact-on-drivers-jobs-us). Google's sister company Waymo is [set to launch a commercial driverless taxi service in Phoenix](https://arstechnica.com/cars/2017/10/report-waymo-aiming-to-launch-commercial-driverless-service-this-year/), and Uber has made it their explicit goal to [convert their entire fleet to driverless cars](https://www.washingtonpost.com/business/economy/uber-signs-deal-to-buy-24000-autonomous-vehicles-from-volvo/2017/11/20/d6038f28-ce2a-11e7-81bc-c55a220c8cbe_story.html); as you might imagine, [taxi companies are not happy about this development](http://money.cnn.com/2017/01/10/technology/new-york-self-driving-cars-ridesharing/index.html). Most major car manufacturers including Ford and Mercedes-Benz are also working on self-driving cars, with many already including lane guidance and automatic parking in their commercial models.

Much more immediate than the societal impact, however, are ethical problems about how a self-driving car should behave. This is reminiscent of the "trolley problem" in philosophy, which [Wikipedia](https://en.wikipedia.org/wiki/Trolley_problem) describes thus:

> There is a runaway trolley barreling down the railway tracks. Ahead, on the tracks, there are five people tied up and unable to move. The trolley is headed straight for them. You are standing some distance off in the train yard, next to a lever. If you pull this lever, the trolley will switch to a different set of tracks. However, you notice that there is one person tied up on the side track. You have two options:

*   Do nothing, and the trolley kills the five people on the main track.
*   Pull the lever, diverting the trolley onto the side track where it will kill one person.

> Which is the most ethical choice?

Imagine that you and some passengers are in a self-driving car, when several people suddenly run onto the road in front of the car. Should the self-driving car:

*   swerve, potentially hitting storefronts and killing you and your passengers? Or,
*   keep going, potentially hitting and killing the pedestrians?

This lab asks you to explore this ethical dilemma. Credit goes to Evan Peck of Bucknell University and Justin Li of Occidental College for developing/refining this assignment.

### Step 1

From the starter files, run `manual.py`. This file will present you with 60 scenarios, with different passengers and pedestrians, in which you must decide which group to save. As a pair, work through all 60 scenarios and decide who you would save in each. Take as long as necessary for each one, and aim to answer as truthfully as possible. Your responses will be saved into a timestamped log file, which you will submit at the end of class today.

Once you have gone through all 60 scenarios, you will be given a summary of who you have saved. Examine this summary. Talk briefly about the decision criteria you used.

Compare your statistics with a neighboring pair's results. What similarities and differences do you note? How did your decision criteria differ?

### Step 2

For this part of the lab, imagine you and your partner are the programmers writing the decision process for a self-driving car. In `automatic.py`, there is a function called `automatic_decision`. Your job is to come to a consensus with your partner on a decision process you are both comfortable with, and then replicate this decision process as much as possible in this function.

The `automatic_decision` function takes a `Scenario` instance, and must return which group to save - either `"passengers"`, or `"pedestrians"`. 

`Scenario` objects have the following methods:

*   `getPassengers()`, which returns a list of Person objects that describe the passengers in the car
*   `getPedestrians()`, which returns a list of Person objects that describe the pedestrians


`Person` objects have the following methods:

*   `getCharType()`, which returns whether the `Person` is `"human"`, `"cat"`, or `"dog"`
*   `getAge()`, which returns whether the human is `"baby"`, `"child"`, `"adult"`, or `"elderly"`
*   `getGender()`, which returns whether the human is `"male"`, `"female"`, or `"nonbinary"`
*   `getBodyType()`, which returns whether the human adult is `"overweight"`, `"athletic"`, or `"average"`
*   `getProfession()`, which returns whether the human adult is `"doctor"`, `"CEO"`, `"unemployed"`, or `"unknown"`
*   `isPregnant()`, which returns `True` if the human adult female is pregnant, and `False` otherwise
*   `isCriminal()`, which returns `True` if the human adult has a criminal (felony charge) history, and `False` otherwise
*   `isHomeless()`, which returns `True` if the human is currently homeless and `False` otherwise


**Before you begin coding**, sketch out the algorithm for your decision process **on paper**. What criteria are you using? How much weight are you giving to each criteria? In the case of "ties", what is the tiebreaker? **Please do not use your computers for this part of the lab.**

Once you've finished designing your decision algorithm, and received approval from the prefect or me, go ahead and implement it in Python (in the `automatic_decision` function). If you're stuck or want to see an example, I've written a really simple decision algorithm in the file `sample.py`. Run and test your implementation.  

**Do not** refer back to the statistics from your manual decisions as you write this function. Note that your function _must_ return either `"passengers"` or `"pedestrians"` for any given scenario. Failure to do so will result in an error. Running `automatic.py` will apply your function to 60 random scenarios.


### Step 3

Run and test `automatic.py` once you've finished implementing your automatic decision algorithm. This will apply your function to 60 random scenarios. Make a note of the statistics generated by your algorithm's decisions.

With your partner, answer the following questions:

1.  Consider your manual decision making process.
    *   Are there attributes of the passengers and pedestrians that had a higher (or lower) survival rate, but that was not a conscious factor in your decision process?
    *   What attributes went into your decisions? Does that attribute positively or negatively affect that person’s survival? Why did you consider those attributes?
    *   Is the use of those attributes to make those decision "fair" or "ethical" or "moral"? Why/Why not?
2.  Modify `main()` in `find_difference.py` so that `manual_file` refers to the name of the manual decision file you generated in Part 1 of the lab. Run `find_difference.py`, which will run your function on the same 60 scenarios you manually worked through, and show you the scenarios where your automatic and manual decisions differed. (Note: you will need to scroll up through the terminal to read through all of the output of this program. You might want to copy and paste the output to a text file, so that you can more easily read through it.) Answer the following questions:
    *   How accurately did your automatic model match up with your manual decisions?
    *   For each scenario where your manual and automatic decisions disagreed, explain why. What were you considering when you made the decision manually? What did the automatic decision not take into account, or what did it take into account that it shouldn’t?
3.  Change the last lines of `automatic.py` to run on 100,000 random scenarios. Include these statistics in your submission. Compare the simulated rates of being saved within each attribute (age, gender, etc.). Assign the attribute into one of these categories:

    *   **Category 1:** Deliberately used in decision, and the survival rates reflect what you intended
    *   **Category 2:** Deliberately used in decision, but the survival rates do not reflect what you intended
    *   **Category 3:** Not explicitly used in decision, but the survival rates are not equal between groups
    *   **Category 4:** Not explicitly used in decision, and the survival rates are equal between groups.
    
    For every attribute in Category 3, explain why the survival rates are not equal despite not being used in your decision process.

4.  Working with another pair, explain to each other how you made your automatic decisions and compare your statistics from the previous question.
    *   How do the decision processes differ? What was the reasoning behind each difference?
    *   Did that lead to different statistics, in either ranking or in survival rate?
    *   Which decision process would you prefer to be implemented in a self-driving car? Why?
5.  Based on this exercise, what are some challenges to building (and programming) ethical self-driving cars?

### Submission

Please turn in the following files:

*   `automatic.py`, with `automatic_decision()` implemented.
*   Your manual and automatic **log files**.
*   A **plain text** file with the answers to the questions above.

This lab counts as 10 points towards your Projects grade for the course.