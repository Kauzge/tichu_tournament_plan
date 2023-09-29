"""Utilities for the tournament script (Currently not used)."""

def count_matches_of_players(tournament_plan:list, players:list) -> list:
    """ Counts the number of matches of each player in the tournament."""
    number_of_matches_per_player = []
    for player in players:
        number_of_matches = 0
        for match in tournament_plan:
            for table in match:
                if player in table:
                    number_of_matches += 1
        number_of_matches_per_player.append(number_of_matches)
    return number_of_matches_per_player
