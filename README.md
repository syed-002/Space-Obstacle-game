# Space-Obstacle-game
A game developed in python using the pygame for the course of ISS (Intro to Software Systems)

Install pygame to run the game

Installation : pip3 sudo install pygame

Command to run : python3 ggame.py

Description about the game:

1. If the Player(Bot) crosses an Asteroid, then he gains 5 points and if crosses an Alien , gains 10 points 
2. The Bot starts from left most corner of the display and if collides to the fixed obstacle i.e., Asteroid, score decreases by 5 points and if collides to moving obstacle i.e.,Aliens, score decreases by 10 points
3. If Player_1 reaches the END, its score is stored. It then becomes Player_2 and then reaches to the other end. The scores are compared and the winner is displayed.
4. The speed of the Aliens increses after each round
