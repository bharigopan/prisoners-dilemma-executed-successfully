# -*- coding: utf-8 -*-

__author__ = "Przemyslaw Marcowski"
__copyright__ = "Copyright 2024 Przemyslaw Marcowski"
__license__ = "MIT"
__email__ = "p.marcowski@gmail.com"

"""
Defines the Match class for conducting individual matches in the Prisoner's Dilemma.

This module includes the Match class, which manages the execution of a series 
of rounds between two agents, incorporating a specified level of noise to simulate 
errors in agent decisions.
"""

from round import Round
import random


class Match:
    def __init__(self, agent1, agent2, noise=0.0):
        """
        Initializes a match between two agents with an option for move noise.

        Args:
            agent1 (Agent): First participant in the match.
            agent2 (Agent): Second participant in the match.
            noise (float): Probability of move being flipped (C <-> D).
        """
        self.agent1 = agent1
        self.agent2 = agent2
        self.noise = noise
        self.scores = []

    def run(self, num_rounds):
        """
        Executes the match for a specified number of rounds.

        Args:
            num_rounds (int): Number of rounds to be played in the match.
        """
        for _ in range(num_rounds):
            round_instance = Round(self, self.noise)
            round_instance.play()
            self.scores.append(round_instance.score())

    def apply_noise(self, move):
        """
        Applies noise to a move, potentially flipping it based on the noise level.

        Args:
            move (str): The original move ('C' or 'D').

        Returns:
            str: The potentially flipped move.
        """
        if random.random() < self.noise:
            return "D" if move == "C" else "C"
        return move
