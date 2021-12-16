def closest_mod_5(x):
    return x if x % 5 == 0 else closest_mod_5(x + 1)