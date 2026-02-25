def update_player_score(current_score, increment):
    # made a mistake of default the value to 0 always, now corrected
    current_score = current_score + increment
    return current_score