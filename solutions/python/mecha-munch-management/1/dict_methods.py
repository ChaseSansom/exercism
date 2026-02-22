"""Functions to manage a users shopping cart items."""
from collections import OrderedDict

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    dict = {}
    add_item(dict, notes)
    return dict


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for key, value in recipe_updates:
        if key in ideas and isinstance(ideas[key], list) and isinstance(value, list):
            ideas[key].extend(value)   # merge lists
        else:
            ideas[key] = value         # overwrite or add new key
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    combined = {item: [qty] + aisle_mapping[item] for item, qty in cart.items()}
    return OrderedDict(sorted(combined.items(), key=lambda kv: kv[0], reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    return {
        item: [
            "Out of Stock" if max(0, (qty if isinstance(qty, int) else 0) - fulfillment_cart.get(item, [0])[0]) == 0
            else max(0, (qty if isinstance(qty, int) else 0) - fulfillment_cart.get(item, [0])[0]),
            aisle,
            flag
        ]
        for item, (qty, aisle, flag) in store_inventory.items()
    }
