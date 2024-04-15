# Simulate the Iterated Prisoner's Dilemma game with selected strategies
This repository contains a script for simulating the Iterated Prisoner's Dilemma game using various strategies. The script runs a tournament among agents with different strategies and calculates the average score per move for each strategy combination. It also visualizes the score distributions for each strategy using a boxplot. Simulation parameters, such as selected strategies, number of rounds, self-play, and noise, can be customized.

## Features
Various strategies implemented in the *strategies.py* file can be selected for the tournament, including:
- **Always Cooperate**: Always cooperates, regardless of the opponent's history.
- **Always Defect**: Always defects, regardless of the opponent's history.
- **Tit for Tat**: Cooperates on the first move and then mimics the opponent's previous move.
- **Tideman and Chieruzzi**: Cooperates on the first move and defects if the opponent defected on the previous move.
- **Nydegger**: Cooperates for the first two moves and defects if the opponent defected in the last three consecutive moves.
- **Grofman**: Cooperates if the opponent has cooperated more than half the time, and defects otherwise.
- **Shubik**: Cooperates on the first move and then defects if the opponent defected on the previous move. If the opponent cooperated, it randomly chooses between cooperation and defection.
- **Stein and Rapoport**: Cooperates for the first three moves and defects if the opponent defected in the last four consecutive moves.
- **Friedman**: Cooperates on the first move and defects if the opponent has ever defected.
- **Davis**: Cooperates for the first nine moves and defects if the opponent has defected in the last ten moves.
- **Graaskamp**: Cooperates for the first four moves and defects if the opponent has defected in the last five moves.
- **Downing**: Cooperates on the first move and defects if the opponent defected in the last two consecutive moves.
- **Feld**: Cooperates for the first two moves and defects if the opponent defected in any of the last three moves.
- **Joss**: Cooperates on the first move and then defects with a probability of 0.1 if the opponent cooperated on the previous move, or always defects if the opponent defected on the previous move.
- **Tullock**: Cooperates on the first move and then defects with a probability of 0.1 if the opponent cooperated on the previous move, or always defects if the opponent defected on the previous move.
- **Random Choice**: Randomly chooses between cooperation and defection.
- **Grudger**: Cooperates until the opponent defects, and then always defects.
- **Pavlov**: Cooperates on the first move, and then cooperates if both players chose the same move on the previous round, or defects otherwise.
- **Suspicious Tit for Tat**: Defects on the first move and then plays Tit-for-Tat.
- **Hard Tit for Tat**: Cooperates on the first move and then defects if the opponent has defected in any of the previous three rounds.
- **Soft Grudger**: Cooperates until the opponent defects twice in a row, and then always defects.
- **Prober**: Starts by playing D, C, C on the first three moves. If the opponent cooperates on the second and third moves, it defects forever. Otherwise, it plays Tit-for-Tat.
- **Alternate**: Alternates between cooperation and defection, starting with cooperation.

After each tournament, average scores per move for each strategy combination is calculated and presented in table format and score distributions for each strategy are plotted.

## License
This code is licensed under the MIT license found in the LICENSE file in the root directory of this source tree.

## Usage
To run the simulation, ensure that Python is installed on your computer along with the required dependencies. Execute the `prisoner_dilemma_simulator.py` script with the desired simulation parameters.

### Parameters
- `selected_strategy_names`: List of strategy names to include in the simulation (default: 'Tit for Tat', 'Always Cooperate', 'Always Defect', 'Random Choice'])
- `num_rounds`: Number of rounds to play in each game between strategies (default: 100)
- `self_play`: Whether to include self-play matches (default: False)
- `noise`: The probability of an agent making a mistake (default: 0.0)

### Output
The script will run the tournament among the selected strategies and display the following outputs:
- Table showing the average scores per move for each strategy combination
- Boxplot visualizing the score distributions for each strategy, with the average score marked

## Installation
To run the Iterated Prisoner's Dilemma simulator, ensure that Python is installed on your computer, along with the necessary dependencies. These dependencies are specified in the `environment.yml` file. Clone this repository or download the files, install the necessary libraries, and execute the simulation script within your Python environment with desired arguments.
