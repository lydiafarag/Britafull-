# 💧 Britafull
## 🏠 Inspiration
Britafull is inspired by the ubiquitous student experience of living with people who may drive us crazy. Some roommates never wash their dishes, some don't take out the trash, but most insidious and aggravating of all... not refilling the Brita!! It's the little things that motivate you to finally get your own place. According to our _**highly**_ scientific research, 80% of students face the **SAME** problem! 🔔🚰
##  What it does 🔔🚰
Britafull detects when the Brita's water levels get below a certain point using weight. The next person to grab the Brita and empties it to that point has seconds before the speaker _kindly_ reminds them to be a good roommate and fill up that Brita. If that's not incentive enough, waiting even longer triggers a text message reminder. That's right, the whole group chat knows now. 

Call it petty, but here at Britafull, we get results. 

## How we built it 💻
We used force sensing resistors to detect changes in force accounting for the presence or absence of the Brita. This information (analog) is passed to an Arduino which converts to a digital signal that is sent to our Raspberry Pi. We programmed primarily in Python and implemented functions to check when the Brita is empty based on the input data; if it is, we then trigger an alarm which prompts the user to refill. Lastly, if the Brita remains unfilled,  we use Twilio to send a message to the entire roommate group chat that someone needs to get on their Brita game!

## Challenges we ran into 
As with many hardware hacks, our challenges were related to finding the right parts to use, and connecting the Raspberry Pi, Arduino, and our personal computers! Once we gathered the resistors that were compatible with the sensors to take the measurements we needed, we ran into compatibility problems that came from running Twilio's API with the rest of our backend interface. Also, we needed a Brita (generously provided by a fellow hacker)!!

## Accomplishments that we're proud of
This was many of our first hackathons and first experiences doing a Hardware Hack! We are proud of ourselves for championing through the in-person experience and coming up with such a funny yet overwhelmingly practical product. 

## What we learned
For those of us without hardware experience, we learned how hardware-software system interfaces work! We also learned that the student housing experience is, indeed, universal.


## What's next for Britafull 
Britafull will never stop finding ways to manage your household and roommate problems for you. One way we could advance our platform is by implementing a machine learning algorithm that identifies the roommate in violation of the first roommate commandment: thou shalt refill the Brita as SOON AS IT'S EMPTY. 

