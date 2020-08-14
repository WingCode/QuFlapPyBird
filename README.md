QuFlapPyBird
===============

A Quantum version of Flappy Bird implemented on IBM Qiskit.  
A fork of https://github.com/sourabhv/FlapPyBird

What is Quantum here ?
---------------------------
1. When you hit a pipe or the ground in the usual flappy bird you die. But here you get a second chance! When you hit an obstacle, a qubit is put into superposition (Hadmard gate) then it is measured. If the cat (_read Schrödinger cat_) is alive i.e probability of 1 dominates you get an another chance otherwise you die.

How-to (as tested on MacOS)
---------------------------

1. python3 -m pip install -U pygame==2.0.0.dev6 --user
2. pip install qiskit

Gameplay clip
--------------

![Gameplay clip](gameplay1.gif)

[pygame]: http://www.pygame.org
