# -*- coding: utf-8 -*-

__author__ = "Przemyslaw Marcowski"
__copyright__ = "Copyright 2024 Przemyslaw Marcowski"
__license__ = "MIT"
__email__ = "p.marcowski@gmail.com"

"""
Defines the Round class for managing individual rounds in the Prisoner's Dilemma tournament.

This module includes the Round class, which conducts a single round of the game between
two agents within a match, incorporating specified noise levels to potentially alter
the agents' decisions.
"""

from config import payoff_matrix


class Round:
    def __init__(self, match, noise):
        """
        Initializes a round within a match, setting the match reference and noise level.

        Args:
            match (Match): The match to which this round belongs.
            noise (float): Probability that an agent's move is flipped (C <-> D).
        """
        self.match = match
        self.noise = noise

    def play(self):
        """
        Executes a single round of the Prisoner's Dilemma, applying strategies and recording results.

        During play, each agent's move is potentially altered by noise. The outcome affects
        their history and scores based on the game's payoff matrix.
        """
        agent1 = self.match.agent1
        agent2 = self.match.agent2
        move1 = self.match.apply_noise(agent1.strategy(agent1.history.get(agent2.name, [])))
        move2 = self.match.apply_noise(agent2.strategy(agent2.history.get(agent1.name, [])))
        agent1.update_history(agent2.name, move2)
        agent2.update_history(agent1.name, move1)
        self.current_score = payoff_matrix[(move1, move2)]
        agent1.update_scores(agent2.name, self.current_score[0])
        agent2.update_scores(agent1.name, self.current_score[1])

    def score(self):
        """
        Returns the results of the round, detailing the scores of both agents.

        Returns:
            tuple: Contains each agent's score from this round.
        """
        return (self.match.agent1, self.match.agent2, self.current_score)
