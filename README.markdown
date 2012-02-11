# Russian Roulette #

This is a small game written in Python, which, as the name implies, simulates a game of Russian Roulette.

### What is Russian Roulette? ###

Russian Roulette is a game in which a standard six-shooter revolver has all its rounds removed save for one. The gun gets passed around the players in a circular round robin order. Every time a player receives the gun, they spin the cylinder, which in effect "shuffles" the location of the round, put the gun against their head and pull the trigger, hoping for the best. The game either ends until someone gets shot or until there's only one player left alive.

To be honest, Russian Roulette doesn't appear to have originated from Russia at all.

### Planned features of this game ###

*   There would be two game modes, the first is single player and the other is multiplayer.
    - In single player, the player chooses either to play alone (suicide roulette) or play with bots.
    - In both game modes, the game can be chosen to end either when someone gets shot or when there is only one player left alive.
*   The early development stages of the game would probably involve it being a console application, as the logic of the game is more important. However, a proper game environment is planned, and I'll use PyGame for it.
*   Turbo Last Man Standing - a game mode where the number of bullets increase each time 30% of the players gets shot. For example, in a game of six players, if two players dies, an additional bullet is added into the gun cylinder.
*   And some other features, I won't add anything more as of now to prevent feature creep.
