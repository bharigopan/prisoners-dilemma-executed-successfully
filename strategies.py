# -*- coding: utf-8 -*-

__author__ = "Przemyslaw Marcowski"
__copyright__ = "Copyright 2024 Przemyslaw Marcowski"
__license__ = "MIT"
__email__ = "p.marcowski@gmail.com"

"""
Iterated Prisoner's Dilemma Strategies

This module contains various strategies for the Iterated Prisoner's Dilemma
game. Each strategy is implemented as a function that takes the history of the
opponent's moves and returns the next move (either "C" for cooperation or "D"
for defection). The available strategies include Always Cooperate, Always
Defect, Tit for Tat, Tideman and Chieruzzi, Nydegger, Grofman, Shubik, Stein
and Rapoport, Friedman, Davis, Graaskamp, Downing, Feld, Joss, Tullock, and
Random Choice. The strategies dictionary at the end of the module maps
strategy names to their corresponding functions, allowing easy access to the
strategies.

This code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

import random


def always_cooperate(_):
    """Always cooperate strategy.

    This strategy always cooperates, regardless of the opponent's history.

    Returns:
        str: "C" indicating cooperation.
    """
    return "C"


def always_defect(_):
    """Always defect strategy.

    This strategy always defects, regardless of the opponent's history.

    Returns:
        str: "D" indicating defection.
    """
    return "D"


def tit_for_tat(history):
    """Tit-for-Tat strategy.

    This strategy cooperates on the first move and then mimics the opponent's
    previous move for subsequent moves.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    return history[-1] if history else "C"


def tideman_and_chieruzzi(history):
    """Tideman and Chieruzzi strategy.

    This strategy cooperates on the first move and defects if the opponent
    defected on the previous move.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    return "D" if history and history[-1] == "D" else "C"


def nydegger(history):
    """Nydegger strategy.

    This strategy cooperates for the first two moves and defects if the
    opponent defected in the last three consecutive moves.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if len(history) < 3:
        return "C"
    return "D" if "".join(history[-3:]) == "DDD" else "C"


def grofman(history):
    """Grofman strategy.

    This strategy cooperates if the opponent has cooperated more than half
    the time, and defects otherwise.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    num_defects = history.count("D")
    return "D" if num_defects > len(history) / 2 else "C"


def shubik(history):
    """Shubik strategy.

    This strategy cooperates on the first move and then defects if the
    opponent defected on the previous move. If the opponent cooperated,
    it randomly chooses between cooperation and defection.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if not history:
        return "C"
    return "D" if history[-1] == "D" else random.choice(["C", "D"])


def stein_and_rapoport(history):
    """Stein and Rapoport strategy.

    This strategy cooperates for the first three moves and defects if the
    opponent defected in the last four consecutive moves.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if not history or len(history) < 4:
        return "C"
    return "D" if "".join(history[-4:]) == "DDDD" else "C"


def friedman(history):
    """Friedman strategy.

    This strategy cooperates on the first move and defects if the opponent
    has ever defected.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    return "D" if history and "D" in history else "C"


def davis(history):
    """Davis strategy.

    This strategy cooperates for the first nine moves and defects if the
    opponent has defected in the last ten moves.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if not history or len(history) < 10:
        return "C"
    return "D" if "D" in history[-10:] else "C"


def graaskamp(history):
    """Graaskamp strategy.

    This strategy cooperates for the first four moves and defects if the
    opponent has defected in the last five moves.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if not history or len(history) < 5:
        return "C"
    return "D" if "D" in history[-5:] else "C"


def downing(history):
    """Downing strategy.

    This strategy cooperates on the first move and defects if the opponent
    defected in the last two consecutive moves.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if not history or len(history) < 2:
        return "C"
    return "D" if history[-1] == "D" and history[-2] == "D" else "C"


def feld(history):
    """Feld strategy.

    This strategy cooperates for the first two moves and defects if the
    opponent defected in any of the last three moves.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if not history or len(history) < 3:
        return "C"
    return "D" if "DDD" in "".join(history[-3:]) else "C"


def joss(history):
    """Joss strategy.

    This strategy cooperates on the first move and then defects with a
    probability of 0.1 if the opponent cooperated on the previous move, or
    always defects if the opponent defected on the previous move.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if not history:
        return "C"
    return "D" if history[-1] == "D" or random.random() < 0.1 else "C"


def tullock(history):
    """Tullock strategy.

    This strategy cooperates on the first move and then defects with a
    probability of 0.1 if the opponent cooperated on the previous move, or
    always defects if the opponent defected on the previous move.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if not history:
        return "C"
    return "D" if history[-1] == "D" or random.random() < 0.1 else "C"


def random_choice(_):
    """Random choice strategy.

    This strategy randomly chooses between cooperation and defection.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    return random.choice(["C", "D"])


def grudger(history):
    """Grudger strategy.

    This strategy cooperates until the opponent defects, and then always defects.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    return "D" if "D" in history else "C"


def pavlov(history):
    """Pavlov strategy (Win-Stay, Lose-Shift).

    This strategy cooperates on the first move, and then cooperates if both 
    players chose the same move on the previous round, or defects otherwise.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if not history:
        return "C"
    return history[-1] if history[-1] == history[-2] else ("C" if history[-1] == "D" else "D")


def suspicious_tit_for_tat(history):
    """Suspicious Tit-for-Tat strategy.

    This strategy defects on the first move and then plays Tit-for-Tat.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    return "D" if not history else history[-1]


def hard_tit_for_tat(history):
    """Hard Tit-for-Tat strategy.

    This strategy cooperates on the first move and then defects if the opponent
    has defected in any of the previous three rounds.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if len(history) < 3:
        return "C"
    return "D" if "D" in history[-3:] else "C"


def soft_grudger(history):
    """Soft Grudger strategy.

    This strategy cooperates until the opponent defects twice in a row,
    and then always defects.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if len(history) < 2:
        return "C"
    return "D" if history[-1] == "D" and history[-2] == "D" else "C"


def prober(history):
    """Prober strategy.

    This strategy starts by playing D, C, C on the first three moves. If the 
    opponent cooperates on the second and third moves, it defects forever. 
    Otherwise, it plays Tit-for-Tat.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    if len(history) == 0:
        return "D"
    if len(history) == 1:
        return "C"
    if len(history) == 2:
        return "C"
    if history[1] == "C" and history[2] == "C":
        return "D"
    return history[-1]


def alternate(history):
    """Alternate strategy.

    This strategy alternates between cooperation and defection, starting with
    cooperation.

    Args:
        history (list): List of opponent's previous moves.

    Returns:
        str: "C" for cooperation or "D" for defection.
    """
    return "C" if len(history) % 2 == 0 else "D"


strategies = {
    'Always Cooperate': always_cooperate,
    'Always Defect': always_defect,
    'Tit for Tat': tit_for_tat,
    'Tideman and Chieruzzi': tideman_and_chieruzzi,
    'Nydegger': nydegger,
    'Grofman': grofman,
    'Shubik': shubik,
    'Stein and Rapoport': stein_and_rapoport,
    'Friedman': friedman,
    'Davis': davis,
    'Graaskamp': graaskamp,
    'Downing': downing,
    'Feld': feld,
    'Joss': joss,
    'Tullock': tullock,
    'Random Choice': random_choice,
    'Grudger': grudger,
    'Pavlov': pavlov,
    'Suspicious Tit for Tat': suspicious_tit_for_tat,
    'Hard Tit for Tat': hard_tit_for_tat,
    'Soft Grudger': soft_grudger,
    'Prober': prober,
    'Alternate': alternate
}
