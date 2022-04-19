# tm_map_analyzer
An analyzer of inherent quality in the Terra Mystica boardgame maps

Usage:
`python3 map_analyzer.py map_file [skewed]`

Analyzes a map using different metrics according to the paper "Map Generation and Balance in the Terra Mystica Board Game Using Particle Swarm and Local Search", published in https://link.springer.com/chapter/10.1007/978-3-030-53956-6_15

I also created my own metric, f5, which indicates peninsular/island hexes (0 or 1 land neighboring hexes).

The default program expects a map using the base map alignment, where even rows (starting from row 0) have 1 additional hex.
To invert that, call the command with an additional "skewed" parameter, which will invert the expected map (i.e., odd rows have an additional hex).

The file example_map picks a bad map by Dave (yes, you have been a bad boy, Dave) to show its format:

<span style="font-family:Mono; font-size:4em;">
R, I, Y, U, K, Y, G, I, Y, R, B, U, I, I<br>
K, I, I, B, G, S, R, I, B, U, K, I, Y<br>
G, S, R, I, I, I, I, I, I, S, I, I, S, I<br>
K, B, G, I, Y, R, S, U, I, I, K, B, G<br>
U, Y, S, I, U, K, B, Y, S, R, Y, U, K, I<br>
R, I, I, G, S, R, K, U, K, I, B, G, R<br>
B, I, G, U, I, I, I, I, I, I, I, I, I, I<br>
I, K, B, I, G, S, R, Y, U, K, B, G, I<br>
S, R, Y, I, U, Y, B, G, S, R, Y, U, K, I<br>
</span>

I = rIver
R = Red (Wasteland)
Y = Yellow (Desert)
U = Brown (Plains)
K = Black (Swamp)
B = Blue (Reef/Island)
G = Green (Forest)
S = Gray (Mountain/Stone)

The format is similar to snellman, so go ask Juho about the choice of letters :P
I decided to stick with the snellman format due to its popularity.
One important caveat: do NOT use an initial line of river hexes as in snellman for maps with inverted lenghts for rows. Just pass the "skewed" parameter.

