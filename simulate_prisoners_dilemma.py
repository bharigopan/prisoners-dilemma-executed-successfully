# -*- coding: utf-8 -*-

__author__ = "Przemyslaw Marcowski"
__copyright__ = "Copyright 2024 Przemyslaw Marcowski"
__license__ = "MIT"
__email__ = "p.marcowski@gmail.com"

"""
Prisoner's Dilemma Simulator

This script simulates the Prisoner's Dilemma game using different strategies.
It runs a tournament among agents with various strategies and calculates the
average score per move for each strategy combination.

The simulation parameters, such as the selected strategies, number of rounds,
and noise can be customized. The available strategies and their rules can be
inspected in the strategies.py file.

The results are printed in a tabular format using the tabulate library.

This code is licensed under the MIT License. For more information, please
refer to the LICENSE file in the root directory of this source tree.
"""

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from tabulate import tabulate
from strategies import strategies

# Initialize parameters
selected_strategy_names = [
    'Tit for Tat', 'Always Cooperate', 'Always Defect', 'Alternate',
    'Random Choice'
]
num_rounds = 100
self_play = False
noise = 0.0


class Agent:
    """Represents an agent participating in the Prisoner's Dilemma game."""

    def __init__(self, strategy, name):
        """
        Initialize an agent with a strategy and name.
        Args:
            strategy (function): The strategy function for the agent.
            name (str): The name of the agent.
        """
        self.strategy = strategy
        self.name = name
        self.history = {}
        self.scores = {}

    def update_history(self, opponent_name, move):
        """
        Updates the agent's move history against a specific opponent.
        Args:
            opponent_name (str): The name of the opponent.
            move (str): The move made by the opponent.
        """
        if opponent_name not in self.history:
            self.history[opponent_name] = [move]
        else:
            self.history[opponent_name].append(move)

    def update_scores(self, opponent_name, score):
        """
        Updates the agent's scores against a specific opponent.
        Args:
            opponent_name (str): The name of the opponent.
            score (int): The score achieved in the round.
        """
        if opponent_name not in self.scores:
            self.scores[opponent_name] = [score]
        else:
            self.scores[opponent_name].append(score)


def validate_strategies(strategy_names):
    """
    Ensure all provided strategy names are valid.
    Args:
        strategy_names (list): List of strategy names to validate.
    Raises:
        ValueError: If any strategy name is not recognized.
    """
    invalid_strategies = [name for name in strategy_names
                          if name not in strategies]
    if invalid_strategies:
        raise ValueError(f"Invalid strategy names: {invalid_strategies}")


def validate_parameters(num_rounds, noise):
    """
    Validate simulation parameters.
    Args:
        num_rounds (int): The number of rounds to play.
        noise (float): The probability of making a move error.
    Raises:
        ValueError: If parameters are outside acceptable ranges.
    """
    if not isinstance(num_rounds, int) or num_rounds < 1:
        raise ValueError("Number of rounds must be a positive integer.")
    if not (0 <= noise <= 1):
        raise ValueError("Noise must be a float between 0 and 1.")


def run_round(agent1, agent2, payoff_matrix, noise=0.0):
    """
    Play a single round of the Prisoner's Dilemma between two agents.
    Args:
        agent1 (Agent): The first agent.
        agent2 (Agent): The second agent.
        payoff_matrix (dict): The payoff matrix for the game.
        noise (float): The probability of an agent making a mistake.
    """
    move1 = agent1.strategy(agent1.history.get(agent2.name, []))
    move2 = agent2.strategy(agent2.history.get(agent1.name, []))

    # Apply noise
    if random.random() < noise:
        move1 = "D" if move1 == "C" else "C"
    if random.random() < noise:
        move2 = "D" if move2 == "C" else "C"

    # Update agents histories and scores
    agent1.update_history(agent2.name, move2)
    agent2.update_history(agent1.name, move1)
    score1, score2 = payoff_matrix[(move1, move2)]
    agent1.update_scores(agent2.name, score1)
    agent2.update_scores(agent1.name, score2)


def run_tournament(agents, num_rounds, self_play=False, noise=0.0):
    """
    Run a tournament among the agents for a specified number of rounds.
    Args:
        agents (list): A list of Agent objects participating in the tournament.
        num_rounds (int): The number of rounds to play in each game.
        self_play (bool): Whether to include self-play matches (default: False).
        noise (float): The probability of an agent making a mistake.
    """
    # Define payoff matrix for Prisoner's Dilemma game
    payoff_matrix = {("C", "C"): (3, 3), ("C", "D"): (0, 5),
                     ("D", "C"): (5, 0), ("D", "D"): (1, 1)}

    # Generate agent pairs based on self-play setting
    if self_play:
        agent_pairs = [(agent1, agent2) for agent1 in agents
                       for agent2 in agents]
    else:
        agent_pairs = [(agent1, agent2) for agent1 in agents
                       for agent2 in agents if agent1 != agent2]

    # Simulate multiple game rounds for each pair of agents
    for agent1, agent2 in agent_pairs:
        for _ in range(num_rounds):
            run_round(agent1, agent2, payoff_matrix, noise)


def run_simulation(strategy_names, num_rounds, self_play=False, noise=0.0):
    """
    Simulates the Prisoner's Dilemma game based on Axelrod's tournament.
    Each strategy plays against every other strategy (and optionally against
    itself) for the specified number of rounds. The scores are calculated using
    the payoff matrix from Axelrod's tournament. The average score per move for
    each strategy combination and the overall average score per move for each
    strategy are computed and displayed. Additionally, the score distributions
    for each strategy are plotted as a boxplot with the average score marked.

    Args:
        strategy_names (list): Names of the strategies to include in the
                               simulation.
        num_rounds (int): Number of rounds to play in each game between
                          strategies.
        self_play (bool): Whether to include self-play matches (default: False).
        noise (float): The probability of an agent making a mistake.
    """
    validate_strategies(strategy_names)
    validate_parameters(num_rounds, noise)

    # Create agents with specified strategies
    agents = [Agent(strategy=strategies[name], name=name)
              for name in strategy_names]

    # Run tournament
    run_tournament(agents, num_rounds, self_play, noise)

    # Create DataFrame to store scores for each strategy
    df_scores = pd.DataFrame()
    for agent in agents:
        for other in agents:
            scores = agent.scores.get(other.name, [])
            if scores:
                df_scores = pd.concat([df_scores, pd.DataFrame({
                    'Strategy': agent.name,
                    'Opponent': other.name,
                    'Score': scores
                })], ignore_index=True)

    # Calculate average scores per move for each strategy combination
    avg_scores = df_scores.groupby(['Strategy', 'Opponent'])['Score'].mean()
    avg_scores_per_move = avg_scores.unstack()

    # Add overall average score per move for each strategy
    avg_scores_per_move['Overall Average'] = df_scores.groupby('Strategy') \
        ['Score'].mean()

    # Round the DataFrame to two decimal places and replace NaN with "-"
    formatted_df = avg_scores_per_move.round(2).fillna('-')

    # Print table with average scores per move for each strategy combination
    print("\nAverage Scores per Move for Each Strategy Combination:")
    print(tabulate(formatted_df, headers='keys', tablefmt='pipe',
                   showindex=True, numalign="right"))
    print()

    # Plotting score distributions
    fig, ax = plt.subplots(figsize=(10, 6))

    # Calculate mean score per strategy
    grouped = df_scores.groupby('Strategy')['Score'].apply(list)
    scores = [group for name, group in grouped.items()]
    means = grouped.apply(np.mean)

    # Create boxplot
    ax.boxplot(scores, widths=0.3, patch_artist=True,
               positions=np.arange(len(scores)))

    # Plot means
    positions = np.arange(len(means))
    ax.scatter(positions, means, facecolors='none', edgecolors='black', s=50,
               zorder=3)

    # Set axis labels and title
    ax.set_title('Score Distributions per Strategy')
    ax.set_xlabel('Strategy')
    ax.set_ylabel('Score')

    # Set x-ticks
    ax.set_xticks(positions)
    ax.set_xticklabels(means.index, rotation=45)

    # Add grid
    ax.grid(True, linestyle='-', alpha=0.6)

    # Use tight layout
    plt.tight_layout()

    # Show plot
    plt.show()


if __name__ == "__main__":
    run_simulation(selected_strategy_names, num_rounds, self_play=self_play,
                   noise=noise)