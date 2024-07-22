# -*- coding: utf-8 -*-

__author__ = "Przemyslaw Marcowski"
__copyright__ = "Copyright 2024 Przemyslaw Marcowski"
__license__ = "MIT"
__email__ = "p.marcowski@gmail.com"

"""
Configuration settings for the Prisoner's Dilemma simulation.

This module configures key parameters for running simulations of the
Prisoner's Dilemma game, including the strategies used, number of rounds,
self-play options, and the error probability.
"""

import os

# Strategies selected for simulation
selected_strategy_names = [
    'Tit for Tat', 'Always Cooperate', 'Always Defect', 'Alternate',
    'Grudger'
]

# Number of rounds per game
num_rounds = int(os.environ.get('NUM_ROUNDS', 100))

# Enable or disable self-play
self_play = os.environ.get('SELF_PLAY', 'False') == 'True'

# Probability of making a mistake (noise)
noise = float(os.environ.get('NOISE_LEVEL', 0.0))

# Ensure noise is within valid range
assert 0.0 <= noise <= 1.0, "Noise level must be between 0.0 and 1.0"

# Payoff matrix for the Prisoner's Dilemma
payoff_matrix = {
    ("C", "C"): (3, 3),
    ("C", "D"): (0, 5),
    ("D", "C"): (5, 0),
    ("D", "D"): (1, 1)
}
