def print_tournament_plan(tournament_plan, number_of_tables):
    # Print the tournament plan in a readable format
    items_per_line = number_of_tables
    items_printed = 0
    max_width = len(str(max(tournament_plan[0])))+1
    counter = 1
    first_item_in_line = True
    for round in tournament_plan:
        for table in round:
            if first_item_in_line:
                print(f"Round {counter:>2}:", end=' ')
                first_item_in_line = False
            print(f"{str(table):<{max_width+1}}", end=' ')
            items_printed += 1
            
            if items_printed >= items_per_line:
                print()  # Insert a line break
                counter += 1
                items_printed = 0
                first_item_in_line = True

    # Ensure a final line break if needed
    if items_printed > 0:
        print()