# Musicology

## Overview of Music in Saskantinon

PyGame has methods for playing sound files of various types. The game uses these methods to play music and sound effects. The music is played in a loop, and the sound effects are played once. Generally speaking, the music is played in the background, and the sound effects are played in the foreground. The music is played at a default volume of 0.5, and the sound effects are played at a volume of 1.0.

The game design calls for an important role to be played by music. As players navigate through the world, different musical themes are associated with places, actors and timeline events. Furthermore, the intention is for players to be able to construct unique musical themes for their own characters, and to be able to play these themes in the game. The game's music is composed by the game's composer, and is stored in the game's data directory. The themes are composed in large part by directed AI-ish software algorithms that produce a MIDI score, which can then be tweaked in various ways by the players. The MIDI score is then converted to a sound file, which is played in the game.

This highly experimental aspect of the game and the admin software is implemented so for only in the "io\_music" class.

## Tools and Technology

The python music21 and sympy libraries are used to manage the music-generation algorithms and MIDI interfaces.

I hope to also develop themes, lietmotifs, melodies and soundscapes using synths available from Arturia and other sources, with my own compositions and beats. In these cases, I would use my Arturia KeyLab88 midi controller (keyboard) in conjunction with software like Analog Lab V, Abelton Live, GarageBand, Audacity and so on to craft music files for use in the game.

I may also use recordings/mixes based on live instrumentation (acoustic guitar, electric guitar, voice, banjo, mandolin, ukulele, violin) as inputs into musical resources for the game.
