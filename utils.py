# -*- coding: utf-8 -*-

__author__ = "Przemyslaw Marcowski"
__copyright__ = "Copyright 2024 Przemyslaw Marcowski"
__license__ = "MIT"
__email__ = "p.marcowski@gmail.com"

"""
Utility functions for the Prisoner's Dilemma simulation.

This module provides validation functions for checking the integrity of 
strategy names and simulation parameters such as the number of rounds and 
noise levels. These validations ensure that the simulation configuration is
robust and error-free prior to execution.
"""

from strategies import strategies


def validate_strategies(strategy_names):
    """
    Validates that all provided strategy names are recognized.

    Args:
        strategy_names (list): A list of strategy names to validate.

    Raises:
        ValueError: If any strategy name is not recognized within the available
        strategies defined in the system.
    """
    invalid_strategies = [name for name in strategy_names if name not in strategies]
    if invalid_strategies:
        raise ValueError(f"Invalid strategy names: {invalid_strategies}")

def validate_parameters(num_rounds, noise):
    """
    Validates the simulation parameters for number of rounds and noise level.

    Args:
        num_rounds (int): The number of rounds each pair of agents will play.
        noise (float): The probability that an agent's decision is randomly flipped.

    Raises:
        ValueError: If the number of rounds is not a positive integer or if the 
        noise level is not within the range of 0 to 1.
    """
    if not isinstance(num_rounds, int) or num_rounds < 1:
        raise ValueError("Number of rounds must be a positive integer.")
    if not (0 <= noise <= 1):
        raise ValueError("Noise must be a float between 0 and 1.")
