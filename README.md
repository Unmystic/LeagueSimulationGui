# LeagueSimulationGui
A Gui, using PyQt6 for simple classic sports league simulation.


Using predetermined library of team names (like Ravens, Gorillas, Tornadoes , etc.) and descriptors (Amazing, Marvelous, Glorious, etc.) create a simulation of league tournament. The rules for the tournament are simple:

-- Every team plays with others twice: home and away game.

-- 3 points for the victory , 1 point for the draw.

-- Currenly, only points total sort positions of teams in league table

-- There is option to simulate league round by round.

-- No individual statistics , team ratings(attackRating, defenceRating, teamCohesion) generated as a whole. 

You also able to add your own team and choose its playstyle. Playstyle affects balance of your team - improves/decreases the chance of stonger offensive/defensive sides.
Current match engines takes your attackRating and opponents defenceRating to detrmine the overall goal scoring probability. The third parameter - teamCohesion, also randomly generated and improves slightly with each played game.

To  propely run python scripts you need install PyQt6:

-- pip install PyQt6

If you want just run simulations , there is a distributive version with .exe runnable.
Lattest version - 0.3. It features slightly more complicated than previous match engine.

