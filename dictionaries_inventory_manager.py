"""
⚔️  Adventure Inventory System
A creative use of nested dictionaries to manage a text adventure game inventory.
Demonstrates: nested dicts, dict comprehensions, .get(), .items(), filtering, and aggregation.
"""

# --- Item database (nested dictionary) ---

ITEM_DB = {
    "sword":         {"type": "weapon",      "weight": 3.5,   "value": 120,   "effect": "+15 attack"},
    "shield":        {"type": "armor",       "weight": 5.0,   "value": 85,    "effect": "+10 defense"},
    "health_potion": {"type": "consumable",  "weight": 0.3,   "value": 30,    "effect": "restores 50 HP"},
    "torch":         {"type": "utility",     "weight": 0.5,   "value": 5,     "effect": "lights dark areas"},
    "golden_ring":   {"type": "treasure",    "weight": 0.1,   "value": 500,   "effect": "unknown magic"},
    "rope":          {"type": "utility",     "weight": 1.0,   "value": 10,    "effect": "climbing & binding"},
    "crossbow":      {"type": "weapon",      "weight": 4.0,   "value": 200,   "effect": "+20 ranged attack"},
    "bread":         {"type": "consumable",  "weight": 0.2,   "value": 3,     "effect": "restores 10 HP"},
    "iron_helmet":   {"type": "armor",       "weight": 3.0,   "value": 65,    "effect": "+7 defense"},
    "map":           {"type": "utility",     "weight": 0.1,   "value": 15,    "effect": "reveals the area"},
}

MAX_WEIGHT = 15.0  # kg


# ====================== FUNCTIONS ======================


def show_commands():
    print("=" * 60)
    print("Commands: add <item> | remove <item>")
    print("          inventory | filter <type>")
    print("          best | shop | quit")
    print("          commands")

# Display available items


def show_available_items():
    print("\n📦  Available items in the shop:")
    print(f"  {'Name':<20} {'Type':<12} {'Weight':>7}  {'Value':>7}  Effect")
    print("  " + "-" * 65)
    for name, props in ITEM_DB.items():
        print(
            # gp = gold pieces
            f"  {name:<20} {props['type']:<12} {props['weight']:>6.1f}kg  {props['value']:>5}gp  {props['effect']}")


# Calculate inventory stats
def inventory_summary(inventory: dict) -> dict:
    """Return aggregated stats using dict comprehension and aggregation."""
    total_weight = sum(ITEM_DB[item]["weight"] *
                       qty for item, qty in inventory.items())
    total_value = sum(ITEM_DB[item]["value"] *
                      qty for item, qty in inventory.items())

    # Group items by type using a dict of lists
    by_type: dict[str, list] = {}
    for item, qty in inventory.items():
        t = ITEM_DB[item]["type"]
        by_type.setdefault(t, []).append((item, qty))

    return {"total_weight": total_weight, "total_value": total_value, "by_type": by_type}


# Display inventory
def show_inventory(inventory: dict):
    if not inventory:
        print("\n  🎒 Your inventory is empty.")
        return

    stats = inventory_summary(inventory)
    print(
        f"\n🎒  Your Inventory  |  Weight: {stats['total_weight']:.1f}/{MAX_WEIGHT}kg  |  Value: {stats['total_value']}gp")
    print("  " + "-" * 55)

    for category, items in stats["by_type"].items():
        print(f"  [{category.upper()}]")
        for item_name, qty in items:
            props = ITEM_DB[item_name]
            qty_str = f"x{qty}" if qty > 1 else "  "
            print(f"    • {item_name:<20} {qty_str}  ({props['effect']})")


# Add items
def add_item(inventory: dict, item_name: str) -> str:
    if item_name not in ITEM_DB:
        return f"❌  '{item_name}' doesn't exist in the shop."

    stats = inventory_summary(inventory)
    item_weight = ITEM_DB[item_name]["weight"]

    if stats["total_weight"] + item_weight > MAX_WEIGHT:
        return f"❌  Too heavy! Adding '{item_name}' ({item_weight}kg) would exceed your {MAX_WEIGHT}kg limit."

    # dict.get() with default — elegant way to handle first pick-up
    inventory[item_name] = inventory.get(item_name, 0) + 1
    return f"✅  Added '{item_name}' to your inventory."


# Remove items
def remove_item(inventory: dict, item_name: str) -> str:
    if item_name not in inventory:
        return f"❌  You don't have '{item_name}'."
    inventory[item_name] -= 1
    if inventory[item_name] == 0:
        del inventory[item_name]   # clean up zero-quantity entries
    return f"🗑️   Removed one '{item_name}' from your inventory."


# Filter items
def filter_by_type(inventory: dict, item_type: str) -> dict:
    """Dict comprehension to filter inventory by item category."""
    return {item: qty for item, qty in inventory.items()
            if ITEM_DB[item]["type"] == item_type}


# Find best item
def best_item(inventory: dict, key: str) -> str:
    """Find the highest-value or heaviest item using max() over a dict."""
    if not inventory:
        return "Your inventory is empty."
    winner = max(inventory, key=lambda item: ITEM_DB[item].get(key, 0))
    return f"  Most valuable by '{key}': {winner} ({ITEM_DB[winner][key]})"


# ====================== MAIN LOOP ======================

def main():
    inventory: dict[str, int] = {}  # { item_name: quantity }

    print("=" * 60)
    print("  ⚔️   ADVENTURE INVENTORY MANAGER  ⚔️")
    show_commands()

    while True:
        raw = input("\n> ").strip().lower()
        if not raw:
            continue

        parts = raw.split(maxsplit=1)
        cmd = parts[0]
        arg = parts[1] if len(parts) > 1 else ""

        if cmd == "quit":
            print("⚔️  Safe travels, adventurer!")
            break

        elif cmd == "commands":
            show_commands()

        elif cmd == "shop":
            show_available_items()

        elif cmd == "inventory":
            show_inventory(inventory)

        elif cmd == "add":
            if not arg:
                print("  Usage: add <item_name>")
            else:
                print(" ", add_item(inventory, arg))

        elif cmd == "remove":
            if not arg:
                print("  Usage: remove <item_name>")
            else:
                print(" ", remove_item(inventory, arg))

        elif cmd == "filter":
            if not arg:
                print(
                    "  Usage: filter <type>  (weapon/armor/consumable/utility/treasure)")
            else:
                result = filter_by_type(inventory, arg)
                if result:
                    print(f"\n  Items of type '{arg}':", result)
                else:
                    print(f"  No '{arg}' items in your inventory.")

        elif cmd == "best":
            print(best_item(inventory, "value"))
            print(best_item(inventory, "weight"))

        else:
            print(
                "  ❓ Unknown command. Try: add, remove, inventory, filter, best, shop, quit")


if __name__ == "__main__":
    main()
