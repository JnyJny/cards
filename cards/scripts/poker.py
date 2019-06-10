"""simulates a Poker game
"""

import click
from ..deck import Deck

@click.command()
@click.option("-j", "--use-jokers", is_flag=True)
@click.option("-a", "--aces-high", is_flag=True)
@click.option("-n", "--num-players")
@click.option("-w", "--jokers-wild", is_flag=True)
def cli(use_jokers, aces_high, num_players, jokers_wild):
    """Cards
    """
    deck = Deck(use_jokers=use_jokers)
    
