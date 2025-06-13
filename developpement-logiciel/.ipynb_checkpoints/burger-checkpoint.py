import os
import time
from datetime import datetime

# Variables globales
burger_count = 0
last_burger = None
debug = True

ingredient_prices = {
    "bun": 2.0,
    "beef": 5.0,
    "chicken": 4.0,
    "cheese": 1.0,
    "tomato": 0.5,
    "lettuce": 0.5,
    "sauce": 0.3,
}


def get_order_timestamp():
    """
    Retourne la date et l'heure actuelle sous forme de chaîne.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_bun():
    """
    Demande à l'utilisateur de saisir le type de bun.

    Retour :
        str : Le type de bun choisi.
    """
    bun_type = input("Quel type de bun souhaitez-vous ? ")
    print(f"Bun sélectionné : {bun_type}")
    return bun_type


def calculate_burger_price(ingredients_list, ingredient_prices=ingredient_prices):
    """
    Calcule le prix final d'un burger en fonction des ingrédients et de leurs prix unitaires.

    Paramètres :
        ingredients_list (list) : Liste des ingrédients composant le burger.
        ingredient_prices (dict) : Dictionnaire des prix des ingrédients.

    Retour :
        float : Prix final arrondi à 2 décimales après majoration de 10 %.
    """
    base_price = 0
    for ingredient in ingredients_list:
        price = ingredient_prices.get(ingredient)
        if price is None:
            if debug:
                print(f"Attention : ingrédient inconnu '{ingredient}' détecté ! Facturé 0 €.")
            price = 0
        base_price += price

    final_price = round(base_price * 1.1, 2)
    return final_price


def get_meat():
    """
    Demande à l'utilisateur de saisir un type de viande.

    Retour :
        str : Le type de viande saisi.
    """
    return input("Entrez le type de viande : ")


def get_sauce():
    """
    Demande à l'utilisateur de saisir un type de sauce.

    Retour :
        str : Le type de sauce saisi.
    """
    return input("Entrez le type de sauce : ")



def get_cheese():
    """
    Demande à l'utilisateur le type de fromage souhaité.

    Retour :
        str : Le type de fromage choisi.
    """
    return input("Quel type de fromage souhaitez-vous ? ")


def assemble_burger():
    """
    Assemble un burger à partir des différents composants demandés à l'utilisateur.

    Retour :
        dict : Données du burger (id, description, prix, timestamp) ou None en cas d'erreur.
    """
    global burger_count, last_burger

    burger_count += 1

    try:
        bun = get_bun()
        meat = get_meat()
        sauce = get_sauce()
        cheese = get_cheese()

        ingredients = [bun, meat, cheese, "sauce"]  # "sauce" est un ingrédient fixe pour le prix
        price = calculate_burger_price(ingredients)

        burger_description = f"{bun} bun + {meat} + {sauce} + {cheese} cheese"
        timestamp = get_order_timestamp()

        burger_data = {
            "id": burger_count,
            "description": burger_description,
            "price": price,
            "timestamp": timestamp,
        }

    except Exception as e:
        if debug:
            print(f"Erreur lors de l'assemblage du burger : {e}")
        return None

    last_burger = burger_description
    print(f"Burger #{burger_count} assemblé : {burger_description} - Prix : {price}€")
    return burger_data


def save_burger_to_file(burger, filename="burgers.txt"):
    """
    Sauvegarde la description du burger dans un fichier.

    Input:
        burger (str): Description du burger à sauvegarder.
        filename (str): Nom du fichier où sauvegarder (par défaut "burgers.txt").

    Output:
        None
    """
    # Empêche la traversée de répertoire ou noms suspects
    if not filename.endswith(".txt") or "/" in filename or "\\" in filename:
        print("Nom de fichier invalide.")
        return

    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(burger + "\n")
        print(f"Burger sauvegardé dans '{filename}'.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du burger : {e}")


def main():
    """
    Fonction principale pour assembler un burger, afficher ses détails,
    et sauvegarder la description dans un fichier.
    """
    print("Bienvenue dans le constructeur de burgers !\n")

    burger_data = assemble_burger()
    if burger_data is None:
        print("Erreur lors de la création du burger. Veuillez réessayer.")
        return

    description = burger_data["description"]
    price = burger_data["price"]
    timestamp = burger_data["timestamp"]
    burger_id = burger_data["id"]

    print(f"\nVotre burger #{burger_id} a été créé avec succès.")
    print(f"Détails : {description}")
    print(f"Prix final : {price} €")
    print(f"Date de commande : {timestamp}")

    save_burger_to_file(description)

    print("\nLa description du burger a été sauvegardée. Bon appétit !")


if __name__ == "__main__":
    main()
