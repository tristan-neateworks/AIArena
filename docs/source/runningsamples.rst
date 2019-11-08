Running AI Samples
==================

AIArena comes with a number of AI samples that demonstrate various games in action. All of these are intended to run locally,
though some of them can be used with the AIArena online matchmaking and ranking. 

In order to test the demos, first clone the git repository as described in Getting Started, then ensure that the AIArena project is installed through whatever method you prefer.
All demos are in the SampleAIs directory within the project.

Sample1
-------

This runs an interactive game of Connect4 over the console. In order to play, simply enter an integer between 0 and 6 (left to 
right) representing the column in which to place a piece. The game ends when a player either places four pieces in a row, and
the winner is the first person to do so.

GymSample
---------

This runs a game of blackjack in which an AI attempts to win against another built-in AI dealer. 

GymFrozenLakeSample
-------------------

This runs a simplified version of the Gym FrozenLakev1 game where ice physics are ignored (thus making it a simple pathfinding
challenge). The AI present in the sample implements a pathfinding algorithm that avoids pitfalls in order to
reach the goal. 
