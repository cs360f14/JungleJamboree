# JungleJamboree

## The Game

### Description
JungleJamboree is based off of Amazon Trail which originates from Oregon Trail. It is a turn based survival trek through the jungle. 
You and your party must try to survive the jungle as long as possible by foraging for food and fending off dangerous animals.

This game has been tested on OpenSUSE 13.1 64 bit.

#### How to build the code
	1. Ensure that Pygame is installed
		- From the command line, type "python" and press enter.
		- Type "import pygame" and press enter. If no errors occur, then Pygame is installed.
		- Otherwise, you will have to install Pygame. 
		- You can install Pygame with "sudo zypper install pygame" and "sudo zypper install pygame-doc"	
		- We are using Pygame version 1.9.1
	2. Fork the repository 
	3. From the command line, type "git clone git@github.com:USER/JungleJamboree.git" where USER is your username
	4. Enter the JungleJamboree/Gameplay directory
	5. Type "python Game.py &", and press enter.
#### How to run the code
	1. Change to the JungleJamboree/GamePlay directory
	2. Type "python Game.py &", and press enter.
#### Project dependent libraries and external software:
[Pygame version 1.9.1](http://www.pygame.org/news.html)
 
## Contributors

#### To report bugs
Follow the instructions in the BUGREPORT.md file

#### To contribute code
It is not necessary to email any of the admins to contribute! You may fork the repository and do whatever you want!
However, please follow pull request rules when contributing back to the project.

Feature request:
- To request a feature, make a GitHub issue and use the labeled "enhancement".
- An admin will then get to this issue as soon as possible and provide feedback.

Feature add:
- After cloning the repository and making your changes, you should make a pull request. 
- This pull request will be visible to the community and people will be able to comment on it. 

Code commits and pull requests:
- If you believe that the project could benefit from having this code merged, make a pull request!
- In order for the code to be merged, either 3 positive reviews from other outside contributors or 1 positive review from an admin is necessary.

#### Documentation and Coding Standards
For documentation please use:
   * [Style Guide for Python Code](http://legacy.python.org/dev/peps/pep-0008/)
   * [pydoc](https://docs.python.org/3/library/pydoc.html) is required! 
   * Also if creating any new files please use the header:

```
#!/usr/bin/python
##################################
# File Name: 	Game.py
# Author: 	Group 3
# Date: 	11/10/2014
# Project:	Jungle Jamboree
# Purpose: 	Game class
##################################
```
#### Testing Requirements
For testing purposes please contribute a unit test in the corresponding unit test file.
In the future, we plan on using [Travis](https://travis-ci.org/) for testing. If this does happen, we will also require that all tests pass before merging the pull request.

#### Communication
The best way to get in touch with project leads concerning code contribution is to email eheydemann@gmail.com.
We also encourage all contributors to communicate via the IRC Channel for this project. On Freenode, our channel is #cs360f14JungleJamboree
To connect to the IRC channel:

1. Open Firefox web browser
2. Get the ChatZilla [add-on](https://addons.mozilla.org/en-us/firefox/addon/chatzilla/)
3. Open ChatZilla and type the following:
4. /server freenode
5. /join #cs360f14JungleJamboree


## Project Goals
Our goal of this project is to make a working, enjoyable game that is easy for people to contribute to! We would like this game to be able to expand with increased functions, mini-games, and more random events. For current milestones go to the milestone section this repository on github.

### New Features
Our goal would be to have new environments that can affect the party and provide situations that would allow the player to make decisions that can impact the game itself. We would also like a hunting mini game to supplement the foraging to provide a more interactive experience for the player. Right now the user really only clicks on a couple buttons for the whole game.

## License 
- Project
   - [MIT](http://opensource.org/licenses/MIT)
- Images licensed under
	- [Creative Commons Attribution 4.0 International license](http://creativecommons.org/licenses/by/4.0/)

## Original Authors
Evan Heydemann (eheydemann)
* A Junior majoring in Mathematics and Computer Science at Pacific University in Forest Grove, Oregon

Brianna Alcoran (bri-a)
* A Junior majoring in Computer Science at Pacific University in Forest Grove, Oregon

Bryan Stander (stan3971)
* A Senior majoring in Nioinformatics at Pacific University in Forest Grove, Oregon

    
