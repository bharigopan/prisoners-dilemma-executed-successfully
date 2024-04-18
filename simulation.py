# -*- coding: utf-8 -*-

__author__ = "Przemyslaw Marcowski"
__copyright__ = "Copyright 2024 Przemyslaw Marcowski"
__license__ = "MIT"
__email__ = "p.marcowski@gmail.com"

"""
This module facilitates the simulation of the Prisoner's Dilemma tournament using
various strategies. It includes setup, execution, and analysis of results with
options for self-play and noise-induced errors in decisions.
"""

import logging
from agent import Agent
from strategies import strategies
from tournament import Tournament
from utils import validate_strategies, validate_parameters

logger = logging.getLogger(__name__)


def simulate(strategy_names, num_rounds, self_play=False, noise=0.0):
    """
    Conducts a simulation of the Prisoner's Dilemma game based on Axelrod's classic
    tournament format. This function orchestrates the setup and execution of a tournament,
    tracking detailed results.

    Args:
        strategy_names (list): Names of the strategies to include in the simulation.
        num_rounds (int): Number of rounds to play in each game between strategies.
        self_play (bool): If True, includes matches where agents compete against themselves.
        noise (float): Probability that an agent's chosen action is flipped.

    Validates strategy names and parameters, initializes agents and a tournament,
    and logs the results.
    """
    validate_strategies(strategy_names)
    validate_parameters(num_rounds, noise)
    
    logger.info("Starting the Prisoner's Dilemma simulation.")
    logger.info(f"Number of strategies: {len(strategy_names)} | Rounds: {num_rounds} "
                f"| Self-play: {self_play} | Error probability: {noise:.2%}")

    agents = [Agent(strategy=strategies[name], name=name) for name in strategy_names]

    tournament = Tournament(agents, num_rounds, self_play, noise)
    tournament.run()
    logger.info("Analyzing results...")
    tournament.analyze_results()
    logger.info("Simulation completed successfully.")
