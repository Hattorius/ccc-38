# #classic
Stressful asf, will probably never participate again (will forget that I said this). Last year I placed #193, and this year I for sure wanted to make sure that I was on the first page of the leaderboard. I've done it. Place #51 of all people participating (1555) is all mine (or #17 if you only look at solo's). 

## Level 1
The first level (just as #school) was super simple. Just required you to look up a value in the 2 dimensional array and see if the value was **L**and or **W**ater. Then respond with that value.

## Level 2
Level 2 already started to get a lot harder (a steeper step than the previous level 2 in #school). You were given 2 positions on the map, and had to determine if these 2 positions were on the same island. I created a low key path making function that just looked for new ways from the current position the cursor was on, without going back or into the water. Eventually you would have all the positions of the island mapped out and could say if the positions were on the same island.

## Level 3
All these levels so far required you to use the map, but with this level they even said that the map was irrelevant. You had to look at the route given, and see if the route intersects with itself, either by going on the same tile twice, or diagonally across from each other. I finished this level by keeping track on which tile was already stepped on (by the boat). Then also checking if the next step is diagonal, if so check if the adjecent tiles were used (so checking for an intersection diagonally across from meach other). It worked :D

## Level 4
Level 4 was basically path finding. Find a way from point A to point B without going over land. Luckily I remembered that 2 years ago we had to do a pacman exercise for the CCC. I kind of copied the path finding functions I used back then and changed a few variables. Then had to translate the outcome "U", "D", etc. to positions of the map and return that.

 ^^ I remembered that I was very proud of my path finding algorithm back then because of it just finding the shortes path, always.

## Level 5
LEVEL 5 WAS THE HARDEST. I was so stuck on this. The example worked, exercise 1 worked, exercise 2 worked BUT EXERCISE 3 GAVE AN ERROR. So I had to debug. ***But how do you debug 50+ values in this level?????*** Here is how I did it:
![How to debug](recording.gif)

Let's get back to what the question was. At level 5 they would give you a position on the map. The position would be on one of the islands on the map. Then you're required to make a circle around the map. Write down the coordinates you come by etc.

I directly interpreted this as having to make the fastest & most efficient way to do this. rather than just making a circle. It wasn't that hard but then my exercise 3 wasn't accepted. At the end it took me a total of 1 hours and 20 minutes to finish this level.

When I was done I had 15 minutes left on the clock

## Level 6
Level 6 is basically level 5 but harder. In level 6 they actually required you to take the most efficient way. As soon as I read this, I just copied my code from level 5 to level 6 and tried it out: all execrises had a green checkmark! ✅

## Level 7
The last level I saw (which only 1 participant could finish) I didn't even try. I looked at the clock saw that I had 12 minutes left. I read the assignment: level 6 but the boat, the path, can't circle around any other islands. I know it's possible to create it, and I could've probably done it too. But time was up, and honestly... it's currently almost 3 am and I'm tired!

Thank you Cloudflight team for a lot of fun. Was a real challenge!

BYEEE!
