import json
import sys
import re
from typing import Dict, Any, Optional

def format_phone_number(phone: str) -> Optional[str]:
    """Ensure phone number format is xxx-xxx-xxxx."""
    phone_pattern = re.compile(r'(\d{3})[^\d]*(\d{3})[^\d]*(\d{4})')
    match = phone_pattern.match(phone)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return None

def process_orders(input_file: str) -> None:
    """Process orders from the input JSON file and generate customers and items JSON files."""
    customers: Dict[str, str] = {}
    items: Dict[str, Dict[str, Any]] = {}

    try:
        with open(input_file, 'r') as file:
            orders = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file '{input_file}' is not a valid JSON file.")
        return

    for order in orders:
        # Process customer information
        phone = format_phone_number(order['phone'])
        if phone:
            customers[phone] = order['name']
        
        # Process item information
        for item in order['items']:
            item_name = item['name']
            item_price = item['price']

            if item_name not in items:
                items[item_name] = {'price': item_price, 'orders': 0}
            items[item_name]['orders'] += 1

    # Write customers to a new JSON file
    try:
        with open('customers.json', 'w') as output_file:
            json.dump(customers, output_file, indent=4)
    except IOError:
        print("Error: Could not write to 'customers.json'.")

    # Write items to a new JSON file
    try:
        with open('items.json', 'w') as output_file:
            json.dump(items, output_file, indent=4)
    except IOError:
        print("Error: Could not write to 'items.json'.")

if __name__ == "__main__":
    # Pass the input file as the first positional argument
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        process_orders(input_file)
    else:
        print("Please provide the input file name as the first argument.")
