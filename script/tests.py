# pylint: skip-file
import main

def test_check_duplicate1():
    current_round = [[6, 5, 4, 1]]
    current_table = [2]
    player = 3
    assert main.check_duplicate(current_round, current_table, player) == False

def test_check_duplicate2():
    current_round = [[6, 5, 4, 1]]
    current_table = [2, 3]
    player = 3
    assert main.check_duplicate(current_round, current_table, player) == True

def test_check_duplicate3():
    current_round = [[6, 5, 4, 1]]
    current_table = [2]
    player = 6
    assert main.check_duplicate(current_round, current_table, player) == True

def test_check_duplicate4():
    current_round = [[6, 5, 4, 1], [2, 3, 7, 8]]
    current_table = [9, 10]
    player = 11
    assert main.check_duplicate(current_round, current_table, player) == False

def test_check_duplicate5():
    current_round = [[6, 5, 4, 1], [2, 3, 7, 8]]
    current_table = [9, 10]
    player = 5
    assert main.check_duplicate(current_round, current_table, player) == True

def test_check_duplicate6():
    current_round = []
    current_table = [7, 8, 9]
    player = 9
    assert main.check_duplicate(current_round, current_table, player) == True

def test_select_fitting_players1():
    remaining_players = [3, 7, 8]
    current_round = [[6, 5, 4, 1]]
    current_table = [2]
    assert main.select_fitting_player(remaining_players, current_round, current_table) == 3

def test_select_fitting_players2():
    remaining_players = [7, 8, 9, 10]
    current_round = [[6, 5, 4, 1]]
    current_table = [2, 3]
    assert main.select_fitting_player(remaining_players, current_round, current_table) == 7

def test_select_fitting_players3():
    remaining_players = [2, 3, 7, 8, 9, 10]
    current_round = [[]]
    current_table = [2, 3, 4]
    assert main.select_fitting_player(remaining_players, current_round, current_table) == 7

def test_select_fitting_players4():
    remaining_players = [6, 1, 2, 3, 4, 5, 7, 8, 9, 10]
    current_round = [[]]
    current_table = [10,6]
    assert main.select_fitting_player(remaining_players, current_round, current_table) == 1

def test_check_combinations1():
    tournament_plan = [[[6, 5, 4, 1], [7, 8, 3, 2]], 
                       [[4, 6, 5, 7], [8, 3, 1, 2]]]
    assert main.check_combinations(tournament_plan) == False

def test_check_combinations1():
    tournament_plan = [[[6, 5, 4, 1], [7, 8, 3, 2]], 
                       [[5, 6, 4, 7], [8, 3, 1, 2]]]
    assert main.check_combinations(tournament_plan) == True