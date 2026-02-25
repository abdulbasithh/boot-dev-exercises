def get_hurt(current_health, damage):
    current_health -= damage
    print (current_health)
    return current_health

get_hurt(100,50)