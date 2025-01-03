from sympy import Max, Min
from itertools import combinations
from ItemLeague import list_items, get_item_stats
import numpy as np

league_items = list_items()

enemy_armor = 145

initial_stats = {
    "HP": 2405, "AS": 1.153, "AD": 94, "AR": 111.2, "MR": 66.85,
    "CC": 0, "CD": 1.575, "HR": 4.05, "H": 0, "LS": 0,
    "L": 0, "ARP": 0, "A": 0
}

ap_num = 2 # Assuming equal importance
ad_num = 2 

w_ad = ad_num/(ap_num + ad_num)
w_ap = ap_num/(ap_num + ad_num)

AS_LIMIT = 2.5

def calculate_cpv(stats):

    AS = Min(stats["AS"], AS_LIMIT)
    AD, AR, MR, CD, CC, LifeSteal, HR, Haste, HP, ARP, A, L = (
        stats["AD"], stats["AR"], stats["MR"], stats["CD"], stats["CC"],
        stats["LS"], stats["HR"], stats["H"], stats["HP"], stats["ARP"], stats["A"], stats["L"]
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
    adjusted_AD = AD + (100 * excess_CC)
    effective_CC = Min(CC, 0.5)
    effective_health = (HP) * (1 + ((AR*w_ad) / 100) + ((MR*w_ap) / 100))
    
    DPS_A = AS * (adjusted_AD + adjusted_AD * (2 * effective_CC * (CD - 1)))
    Q_dps = (120 + (1.05 * adjusted_AD) + (120 + (1.05 * adjusted_AD)) * (2 * effective_CC * (0.6037 + CD - 1.575))) / Q_cd
    W_a = 412
    DPS_P = (Q_dps + W_a / W_cd) + (0.35 * (Q_dps + W_a / W_cd) / (10 * (100 / (100 + Haste))))
    denominator = ((1 - ARP) * (1 - A) * (enemy_armor)) - L
    denominator = Max(denominator, 1e-9)
    DPS_C = (DPS_A + DPS_P) * (100 / denominator)
    e_value = ((DPS_A * LifeSteal) + HR) * (1 + ((AR*w_ad) / 100) + ((MR*w_ap) / 100))
    CPV = (DPS_C) * ((effective_health / 6687) + (e_value / 6687) + ((90+ (0.45*(adjusted_AD-94)))* (1 + ((AR*w_ad) / 100) + ((MR*w_ap) / 100)))/(W_cd*6687))
    
    return CPV

def find_best_items_non_dynamic(league_items, initial_stats, max_items=5):
    mutually_exclusive_items = {"Lord Dominik's Regards", "Mortal Reminder", "Black Cleaver"}
    current_stats = initial_stats.copy()

    selected_items = set()
    best_items = []

    while len(best_items) < max_items:
        best_item = None
        best_cpv = -float('inf')

        for item_name, item_stats in league_items.items():
            if item_name in mutually_exclusive_items and any(item in selected_items for item in mutually_exclusive_items):
                continue

            if item_name in selected_items:
                continue

            temp_stats = current_stats.copy()
            for stat, value in item_stats.items():
                temp_stats[stat] += value

            cpv = calculate_cpv(temp_stats)

            if cpv > best_cpv:
                best_cpv = cpv
                best_item = item_name

        if best_item is None:
            break  

        best_items.append(best_item)
        selected_items.add(best_item)

        for stat, value in league_items[best_item].items():
            current_stats[stat] += value
            print(current_stats)

    final_cpv = calculate_cpv(current_stats)
    return best_items, final_cpv, current_stats

best_items, max_cpv, final_stats = find_best_items_non_dynamic(league_items, initial_stats)
print(f"Best items: {best_items}")
print(f"Maximum CPV: {max_cpv}")
print("Final stats with best items:")
for stat, value in final_stats.items():
    print(f"{stat}: {value}")