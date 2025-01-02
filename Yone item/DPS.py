from sympy import Max, Min
from itertools import combinations
from ItemLeague import list_items, get_item_stats
import numpy as np

initial_stats = {
    "HP": 2405, "AS": 1.153, "AD": 94, "AR": 111.2, "MR": 66.85,
    "CC": 0, "CD": 1.575, "HR": 4.05, "H": 0, "LS": 0,
    "L": 0, "ARP": 0, "A": 0
}

AS_LIMIT = 2.5

def calculate_stats(stats):

    AS = Min(stats["AS"], AS_LIMIT)
    AD, AR, MR, CD, CC, LifeSteal, HR, Haste, HP, base_health, ARP, A, L = (
        stats["AD"], stats["AR"], stats["MR"], stats["CD"], stats["CC"],
        stats["LS"], stats["HR"], stats["H"], stats["HP"], stats["HP"], stats["ARP"], stats["A"], stats["L"]
    )

    bonus_attack_speed_percent = (((AS / 0.625) - 1) * 100)

    if bonus_attack_speed_percent <= 120:
        Q_cd = 4 * (1 - (0.01 * (bonus_attack_speed_percent / 1.67)))
    else:
        Q_cd = 1.33

    if bonus_attack_speed_percent <= 94.6:
        W_cd = 14 * (1 - (0.01 * (bonus_attack_speed_percent / 1.51)))
    else:
        W_cd = 14 * (1 - 0.625) 

    excess_CC = Max(CC - 0.5, 0)
    adjusted_AD = AD + (50 * excess_CC)
    effective_CC = Min(CC, 0.5)
    effective_health = (2405 + HP) * ((1 + ((AR) / 100) + ((MR) / 100))/2)
    
    DPS_A = AS * (adjusted_AD + adjusted_AD * (2 * effective_CC * (CD - 1)))
    Q_dps = (120 + (1.05 * adjusted_AD) + (120 + (1.05 * adjusted_AD)) * (2 * effective_CC * (0.6037 + CD - 1.575))) / Q_cd
    W_a = 412
    DPS_P = (Q_dps + W_a / W_cd) + (0.35 * (Q_dps + W_a / W_cd) / (10 * (100 / (100 + Haste))))
    denominator = ((1 - ARP) * (1 - A) * (111.2)) - L
    denominator = Max(denominator, 1e-9)
    DPS_C = (DPS_A + DPS_P) * (100 / denominator)
    e_value = ((DPS_A * LifeSteal) + HR) * (1 + (AR / 100) + (MR / 100))
    CPV = (DPS_C/262) * ((effective_health / base_health) + (e_value / base_health))
    
    return DPS_C, effective_health

print(calculate_stats(initial_stats))
