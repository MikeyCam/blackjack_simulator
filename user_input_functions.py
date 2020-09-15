def input_and_validation_from_options(list_of_options):
    player_options_shorthand = []
    for option in list_of_options:
        start = option.find('(') + 1
        end = option.find(')')
        short_option = option[start:end]
        player_options_shorthand.append(short_option)
    while True:
        print("Please enter your selection from the following options (use single letters) {}: ".format(
            list_of_options))
        selection = str(input())
        if selection.lower() not in player_options_shorthand:
            print("Invalid response")
            continue
        else:
            break
    return selection
