# NLA_computational-project-5

Detects liquid level in a glass vessel
digital camera and glass vessel are at constant locations,
e.g. in some laboratory. Vessel is filled in at various levels
and with various liquids of predefined list. Detect from video digital images:
i. if vessel is empty, full, or filled in x percent, 0 < x < 100; ii. which liquid it is

my solution:
I iterate through y coordinates and for every line I start from left and go right. 
when I see a big change in color, I mark this coordinate. I detect the change
in color by using second norm. Rgb are vectors so if changing of x coordinate by
1 cause big change in second norm of rgb vector that means we approached a border.
I do the same for right to left. I sum up how many pixels we have between every point
of height. And I get the area of the glass. This process is kind of similar Riemann
sums and integration.So, I have coordinates of border and area of glass.
Now I need to calculate how much liquid is inside glass. To do that, I calculate
average color of pixel from rightmost pixel to border for every y coordinate.
And do the same for left border to right border pixels if average color of the
inside part is not equal to outside of glass.When we count all pixels of liquid
and all pixels of glass, we can divide the first by second and get the percentage.
For color I already said I calculated average color for every line so I picked
some intervals of color for water, tea and coffee and by that I calculated approximation
of their percentages out of whole liquid.
