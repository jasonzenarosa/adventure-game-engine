# cyoa-engine
## Introduction
The Choose Your Own Adventure Engine is a framework designed to streamline the creation of choose-your-own-adventure games. By creating this project, I was able to practice utilizing classes, files, and linked lists, while demonstrating principles of object-oriented programming. The CYOA Engine was written entirely using vanilla Python 3.9.

## Making a CYOA Game

In order to create a CYOA game using this engine, you must first understand how a CYOA game is structured.
 
A CYOA game is comprised of two parts: Prompts and Options. Prompts are comprised of two parts: the prompt itself (a description of the situation that the player is in), and a list of options that the player can choose. Options are comprised of two parts: the option itself, and the prompt that will occur as a result of that option. Prompts are linked by options. Prompts can have any arbitrary number of options, including zero. A prompt with zero prompts is also known as an ending. Each option can only lead to one prompt, but multiple options can lead to the same prompt.

A typical CYOA game can have a variety of branching plots, all leading to different endings.

Now that you understand how a CYOA game works, here's how to make one using the CYOA Engine!

### Step 1: Create Your Prompts!
  
Navigate over to the prompts.txt file and delete the example prompts. Create a new prompt by writing the name of the prompt and the description of the prompt, separated by a colon. An example of what a prompt might look like:

start:You awaken in a a dimly lit room, a bed in one corner, and a door in the other. 

Names are important because they are how you will denote which prompts are linked by which options. The first prompt of the game must always be named "start" (as seen in the example above). All other prompts can have any name consisting of alphanumeric characters.

### Step 2: Create Your Options!

Once you're done creating your prompts, navigate over to the options.txt file and delete the example options. Create a new option by specifying the starting prompt, the description of the option, and the resulting prompt, separated by colons. An example of what an option might look like:

start:Go through the door.:outside

This will add the option "Go through the door." to the prompt named "start". If you select this option, you will then arrive at the prompt named "outside".

### Step 3: Play Your Game!

After saving your prompts and options files, simply run the adventuregame.py file in the terminal. Have fun!
