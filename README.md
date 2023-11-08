<div align="center">
    <h1>Joystick game - Pong🏓</h1>
</div>

---

## description

this is a simple game made using pygame that is controlled by a joystick that is connected to arduino uno micro-controller.

## gameplay

In this game, you are controlling a player that is moving up and down across the screen, then you have to move the player so that a moving ball hits the player, that causes the ball to bounce back.

The objective is prevent the ball from getting past your player.

## Getting started

to get started, make sure you have python installed in your system and then clone this repository
```bash
git clone https://github.com/Aurumdev952/joystick_game
```
install dependencies
```bash
cd
pip install pygame
```
after that, make sure you have arduino uno micro-controller and a joystick module
connect them according to this scheme

![scheme](/assets/scheme.png)

after that, upload the code in `joystick_game.ino` and make sure to modify the `PORT` constant in `PONG-GAME.py` according to the serial port you have connected to.

to run the game, use:
```bash
python PONG_GAME.py
```

# about
this game was developed by Crash Devs.
