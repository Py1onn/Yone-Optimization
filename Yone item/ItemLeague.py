initial_stats = {
    "HP": 2405, "AS": 0.625, "AD": 94, "AR": 111.2, "MR": 66.85, 
    "CC": 0, "CD": 1.575, "HR": 4.05, "H": 0, "LS": 0, 
    "L": 0, "ARP": 0, "A": 0
}

league_items = {
  "Abyssal Mask": {"HP": 500, "AS": 0, "AD": 0, "AR": 0, "MR": 50, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Archangel's Staff": {"HP": 0, "AS": 0, "AD": 0, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 10, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Ardent Censer": {"HP": 200, "AS": 0, "AD": 0, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 10, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Axiom Arc": {"HP": 0, "AS": 0, "AD": 55, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 25, "LS": 0, "L": 10, "ARP": 0, "A": 0},
  "Banshee's Veil": {"HP": 0, "AS": 0, "AD": 0, "AR": 0, "MR": 45, "CC": 0, "CD": 0, "HR": 0, "H": 10, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Black Cleaver": {"HP": 400, "AS": 0, "AD": 40, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 30, "LS": 0, "L": 0, "ARP": 0, "A": 0.3},
  "Blade of The Ruined King": {"HP": 0, "AS": 25, "AD": 150, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 10, "L": 0, "ARP": 0, "A": 0},
  "Bloodthirster": {"HP": 315, "AS": 0, "AD": 80, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 15, "L": 0, "ARP": 0, "A": 0},
  "Cosmic Drive": {"HP": 200, "AS": 0, "AD": 0, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Dead Man's Plate": {"HP": 350, "AS": 0, "AD": 0, "AR": 55, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Death's Dance": {"HP": 0, "AS": 0, "AD": 60, "AR": 50, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 15, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Eclipse": {"HP": 160, "AS": 0, "AD": 132, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 15, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Edge of Night": {"HP": 325, "AS": 0, "AD": 55, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 10, "ARP": 0, "A": 0},
  "Essence Reaver": {"HP": 0, "AS": 0, "AD": 60, "AR": 0, "MR": 0, "CC": 0.25, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Force of Nature": {"HP": 400, "AS": 0, "AD": 0, "AR": 0, "MR": 55, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Frozen Heart": {"HP": 0, "AS": 0, "AD": 0, "AR": 75, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 20, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Guardian Angel": {"HP": 0, "AS": 0, "AD": 40, "AR": 40, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Guinsoo's Rageblade": {"HP": 0, "AS": 57, "AD": 30, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Heartsteel": {"HP": 900, "AS": 0, "AD": 0, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 40, "H": 20, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Hextech Rocketbelt": {"HP": 350, "AS": 0, "AD": 0, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Infinity Edge": {"HP": 0, "AS": 0, "AD": 70, "AR": 0, "MR": 0, "CC": 0.25, "CD": 0.36, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Kraken Slayer": {"HP": 0, "AS": 40, "AD": 145, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Phantom Dancer": {"HP": 0, "AS": 60, "AD": 0, "AR": 0, "MR": 0, "CC": 0.25, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Rabadon's Deathcap": {"HP": 0, "AS": 0, "AD": 0, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Randuin's Omen": {"HP": 400, "AS": 0, "AD": 0, "AR": 75, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Ravenous Hydra": {"HP": 0, "AS": 0, "AD": 65, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 15, "LS": 12, "L": 0, "ARP": 0, "A": 0},
  "Rod of Ages": {"HP": 300, "AS": 0, "AD": 0, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Rylai's Crystal Scepter": {"HP": 300, "AS": 0, "AD": 0, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Serpent's Fang": {"HP": 0, "AS": 0, "AD": 55, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 18, "ARP": 0, "A": 0},
  "Serylda's Grudge": {"HP": 0, "AS": 0, "AD": 45, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 20, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Shadowflame": {"HP": 200, "AS": 0, "AD": 0, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Shurelya's Battlesong": {"HP": 200, "AS": 0, "AD": 0, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 20, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Spear of Shojin": {"HP": 250, "AS": 0, "AD": 65, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 20, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Spirit Visage": {"HP": 450, "AS": 0, "AD": 0, "AR": 0, "MR": 40, "CC": 0, "CD": 0, "HR": 20, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Statikk Shiv": {"HP": 0, "AS": 35, "AD": 45, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Sterak's Gage": {"HP": 400, "AS": 0, "AD": 50, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Stridebreaker": {"HP": 300, "AS": 25, "AD": 40, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 20, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Sunfire Aegis": {"HP": 500, "AS": 0, "AD": 0, "AR": 50, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "The Collector": {"HP": 0, "AS": 0, "AD": 61, "AR": 0, "MR": 0, "CC": 0.25, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 18, "ARP": 0, "A": 0},
  "Thornmail": {"HP": 350, "AS": 0, "AD": 0, "AR": 75, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Titanic Hydra": {"HP": 600, "AS": 0, "AD": 40, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Trinity Force": {"HP": 300, "AS": 35, "AD": 35, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Umbral Glaive": {"HP": 0, "AS": 0, "AD": 55, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 12, "ARP": 0, "A": 0},
  "Void Staff": {"HP": 0, "AS": 0, "AD": 0, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Warmog's Armor": {"HP": 1000, "AS": 0, "AD": 0, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 40, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Wit's End": {"HP": 0, "AS": 50, "AD": 0, "AR": 0, "MR": 40, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Youmuu's Ghostblade": {"HP": 0, "AS": 0, "AD": 55, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 18, "ARP": 0, "A": 0},
  "Zeke's Convergence": {"HP": 250, "AS": 0, "AD": 0, "AR": 30, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 10, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Zhonya's Hourglass": {"HP": 0, "AS": 0, "AD": 0, "AR": 45, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Lord Dominik's Regards": {"HP": 0, "AS": 0, "AD": 35, "AR": 0, "MR": 0, "CC": 0.25, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 35, "A": 0},
  "Mortal Reminder": {"HP": 0, "AS": 0, "AD": 35, "AR": 0, "MR": 0, "CC": 0.25, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 30, "A": 0},
  "Jak'Sho, The Protean": {"HP": 350, "AS": 0,"AD": 0, "AR": 58.5,"MR": 58.5,"CC": 0,"CD": 0,"HR": 0,"H": 0,"LS": 0,"L": 0,"ARP": 0,"A": 0},
  "Immortal Shieldbow": {"HP": 700, "AS": 0, "AD": 55, "AR": 0, "MR": 0, "CC": 0.25, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Navori Quickblades": {"HP": 0, "AS": 40, "AD": 0, "AR": 0, "MR": 0, "CC": 0.25, "CD": 0, "HR": 0, "H": 200, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Hullbreaker": {"HP": 500, "AS": 0, "AD": 40, "AR": 0, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 0, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Iceborn": {"HP": 300, "AS": 0, "AD": 0, "AR": 50, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 15, "LS": 0, "L": 0, "ARP": 0, "A": 0},
  "Unending": {"HP": 350, "AS": 0, "AD": 0, "AR": 60, "MR": 0, "CC": 0, "CD": 0, "HR": 0, "H": 15, "LS": 0, "L": 0, "ARP": 0, "A": 0},
}

for item, stats in league_items.items():
    if 'AS' in stats:
        stats['AS'] = 0.625 * (stats['AS'] / 100)

for item, stats in league_items.items():
    for stat in ["LS", "L", "ARP"]:
        if stat in stats:
            stats[stat] = stats[stat] / 100

league_items

print(league_items)

def get_item_stats(item_name):
    item = league_items.get(item_name)
    if item:
        return {key: value for key, value in item.items() if key not in {"type", "effects"}}  # Filter out non-stat fields
    return {}

def get_item_effects(item_name):
    item = league_items.get(item_name)
    if item:
        # If the item has no effects, return a default message
        return item.get("effects", "No effects found.")
    return "Item not found."

def list_items(item_type=None):
    if item_type:
        return {name: data for name, data in league_items.items()}
    return league_items
