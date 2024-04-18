# -*- coding: utf-8 -*-

__author__ = "Przemyslaw Marcowski"
__copyright__ = "Copyright 2024 Przemyslaw Marcowski"
__license__ = "MIT"
__email__ = "p.marcowski@gmail.com"

"""
Main module for the Prisoner's Dilemma Tournament Simulation.

This module initiates a tournament simulation of the Prisoner's Dilemma, 
utilizing selected agent strategies. The tournament tests the performance of each 
strategy through multiple rounds, calculating and displaying the average score 
per move for each strategy combination in a table format.

Configurations for strategy selection, number of rounds, self-play capability,
and noise levels are set in the config.py module.

Usage:
    Run this script directly to start the simulation with the parameters
    specified in config.py. Results will be logged and any errors encountered
    during the simulation process will be captured and reported.
"""

import logging
from simulation import simulate
import config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    try:
        simulate(config.selected_strategy_names, config.num_rounds, 
                 self_play=config.self_play, noise=config.noise)
    except Exception as e:
        logging.error(f"An error occurred during simulation: {e}")
