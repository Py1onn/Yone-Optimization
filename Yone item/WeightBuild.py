import numpy as np
import sympy as sp
from ItemLeague import league_items
from sympy import Max, Min, Piecewise, symbols, log, exp
import math

ap_num = 2 # Assuming equal importance
ad_num = 2 

w_ad = ad_num/(ap_num + ad_num)
w_ap = ap_num/(ap_num + ad_num)

AS, AD, AR, MR, CD, CC, LS, HR, H, HP, ARP, A, L = sp.symbols(
    'AS AD AR MR CD CC LS HR H HP ARP A L')

piecewise_AS = Piecewise((AS, AS <= 2.5), (2.5, True))
bonus_attack_speed_percent = (((piecewise_AS / 0.625) - 1) * 100)

Q_cd = Piecewise(
    (4 * (1 - (0.01 * (bonus_attack_speed_percent / 1.67))), bonus_attack_speed_percent <= 120),
    (1.33, True) 
)

W_cd = Piecewise(
    (14 * (1 - (0.01 * (bonus_attack_speed_percent / 1.51))), bonus_attack_speed_percent <= 94.6),
    (14 * (1 - 0.625), True) 
)

excess_CC = Piecewise(
    (200*(CC - 0.5), CC > 0.5),
    (0, True) 
)

adjusted_AD = (AD + (excess_CC*0.5))

effective_CC = Piecewise(
    (CC, CC <= 0.5), 
    (0.5, CC > 0.5)   
)

effective_health = (HP) * (1 + ((AR*w_ad) / 100) + ((MR*w_ap) / 100))

DPS_A = piecewise_AS * (adjusted_AD + adjusted_AD * (2 * effective_CC * (CD - 1)))
Q_dps = (120 + (1.05 * adjusted_AD) + (120 + (1.05 * adjusted_AD)) * (2 * effective_CC * (0.6037 + CD - 1.575))) / Q_cd

W_a = 412

DPS_P = (Q_dps + W_a / W_cd) + (0.35 * (Q_dps + W_a / W_cd) / (10 * (100 / (100 + H))))
denominator = ((1 - ARP) * (1 - A) * (111.2)) - L
denominator = sp.Max(denominator, 1e-9)
DPS_C = (DPS_A + DPS_P) * (100 / denominator)

e_value = ((DPS_A * LS) + HR) * (1 + ((AR*w_ad) / 100) + ((MR*w_ap) / 100))
CPV = (DPS_C) * ((effective_health / 6687) + (e_value / 6687) + ((90+ (0.45*(adjusted_AD-94)))* (1 + ((AR*w_ad) / 100) + ((MR*w_ap) / 100)))/(W_cd*6687))

variables = [AS, AD, AR, MR, CD, CC, LS, HR, H, HP, ARP, A, L]

initial_stats = {
    "HP": 2405, "AS": 1.153, "AD": 94, "AR": 111.2, "MR": 66.85,
    "CC": 0, "CD": 1.575, "HR": 4.05, "H": 0, "LS": 0,
    "L": 0, "ARP": 0, "A": 0
}

def top_items_for_stats(league_items, initial_stats):

    stat_keys = ["HP", "AS", "AD", "AR", "MR", "CC", "CD", "HR", "H", "LS", "L", "ARP", "A"]
    max_values = []

    for stat in stat_keys:
        sorted_items = sorted(
            league_items.items(), key=lambda item: item[1].get(stat, 0), reverse=True
        )

        excluded_items = {"Mortal Reminder", "Black Cleaver", "Lord Dominik's Regards"}
        selected_items = []

        for item in sorted_items:
            if item[0] in excluded_items:
                if not any(ex_item in selected_items for ex_item in excluded_items):
                    selected_items.append(item[0])
            else:
                selected_items.append(item[0])

    
        top_5_items = selected_items[:5]

        total_value_from_items = sum(
            league_items[item][stat] if stat in league_items[item] else 0 for item in top_5_items
        )

        total_value = total_value_from_items + initial_stats.get(stat, 0)

        max_values.append(total_value)

    return tuple(max_values)

hp_max, as_max, ad_max, ar_max, mr_max, cc_max, cd_max, hr_max, h_max, ls_max, l_max, arp_max, a_max = top_items_for_stats(league_items, initial_stats)

def update_weights(variables, weights, current_stats, step_size=0.1):

    partial_derivatives = {var: sp.diff(CPV, var) for var in variables}
    evaluated_gradients = {}

    for var in variables:
        substituted = partial_derivatives[var].subs(current_stats)
        evaluated_gradients[var.name] = abs(substituted.evalf())  

    sorted_gradients = sorted(evaluated_gradients.items(), key=lambda x: x[1], reverse=True)
    total_variables = len(variables)
    for rank, (var_name, gradient) in enumerate(sorted_gradients, start=1):
        weights[var_name] = weights[var_name] + (step_size * (total_variables - rank + 1) / total_variables)  

    return weights


def best_build(league_items, initial_stats, max_values, weights, variables, iterations=5, step_size=0.1):
    final_build = []
    final_score = -float('inf')
    current_weights = weights.copy()

    excluded_items = {"Mortal Reminder", "Black Cleaver", "Lord Dominik's Regards"}
    
    current_stats = initial_stats.copy()

    for t in range(iterations):
        best_build = []
        best_score = -float('inf')

        for slot in range(5):  
            slot_best_item = None
            slot_best_score = -float('inf')

            for item, stats in league_items.items():
                if item in best_build:
                    continue
                if item in excluded_items and any(ex_item in best_build for ex_item in excluded_items):
                    continue

                simulated_stats = current_stats.copy()
                for stat in stats:
                    simulated_stats[stat] += stats[stat]

                normalized_stats = {
                    stat: simulated_stats[stat] / max_value  if max_value > 0 else 0
                    for stat, max_value in zip(initial_stats.keys(), max_values)
                }

                score = sum((normalized_stats[stat])**0.5 * current_weights.get(stat, 0) for stat in initial_stats.keys())

                if score > slot_best_score:
                    slot_best_score = score
                    slot_best_item = item

            if slot_best_item:
                best_build.append(slot_best_item)
                for stat in league_items[slot_best_item]:
                    current_stats[stat] += league_items[slot_best_item][stat]

                best_score = slot_best_score

        current_weights = update_weights(variables, current_weights, current_stats, step_size)
        print(current_weights)

        if best_score > final_score:
            final_build = best_build
            final_score = best_score

    return final_build, final_score, current_weights

weights = {stat: 0 for stat in ["HP", "AS", "AD", "AR", "MR", "CC", "CD", "HR", "H", "LS", "L", "ARP", "A"]}

weights = update_weights(variables, weights, initial_stats, step_size=0.3)
max_values = [hp_max, as_max, ad_max, ar_max, mr_max, cc_max, cd_max, hr_max, h_max, ls_max, l_max, arp_max, a_max]
print(max_values)
build, score, final_weights = best_build(league_items, initial_stats, max_values, weights, variables, iterations=5, step_size=1)
print(build, score)