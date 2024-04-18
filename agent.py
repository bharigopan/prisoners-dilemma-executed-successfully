# -*- coding: utf-8 -*-

__author__ = "Przemyslaw Marcowski"
__copyright__ = "Copyright 2024 Przemyslaw Marcowski"
__license__ = "MIT"
__email__ = "p.marcowski@gmail.com"

"""
Defines the Agent class for use in the Prisoner's Dilemma tournament.

This module contains the Agent class, encapsulating the behavior and state of
agents in the Prisoner's Dilemma game. Agents use specified strategies to
compete and maintain records of history and scores against each opponent.
"""


class Agent:
    def __init__(self, strategy, name):
        """
        Initializes a new Agent with a strategy and a unique name.

        Args:
            strategy (callable): Strategy function defining agent behavior.
                Takes a history list as input, returns a move ('C' or 'D').
            name (str): Name of the agent, used for identification.
        """
        self.strategy = strategy
        self.name = name
        self.history = {}
        self.scores = {}

    def update_history(self, opponent_name, move):
        """
        Updates the history of moves against a specific opponent.

        Args:
            opponent_name (str): Name of the opponent.
            move (str): Move made by the opponent, either 'C' or 'D'.
        """
        if opponent_name not in self.history:
            self.history[opponent_name] = []
        self.history[opponent_name].append(move)

    def update_scores(self, opponent_name, score):
        """
        Updates the score record against a specific opponent.

        Args:
            opponent_name (str): Name of the opponent.
            score (int): Score achieved in the round, as per payoff matrix.
        """
        if opponent_name not in self.scores:
            self.scores[opponent_name] = []
        self.scores[opponent_name].append(score)

    def reset(self):
        """
        Resets the agent's history and scores for a new simulation.

        Useful for reusing the agent in multiple simulations without reinitializing.
        """
        self.history = {}
        self.scores = {}
