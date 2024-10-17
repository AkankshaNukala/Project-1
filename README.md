# Dosa Restaurant Order Processing System

## Project Overview

This project helps a Dosa restaurant analyze their orders and extract meaningful data to design a better ordering system. The script processes raw JSON order data and outputs structured JSON files containing customer information and item statistics.

---

## Features

- **Customer Details Extraction:** Generates a `customers.json` file with customers' phone numbers and names.
- **Item Analysis:** Creates an `items.json` file summarizing each item's price and the number of times it was ordered.

---

## Files

- **`example_orders.json`**: Sample data representing orders received at the restaurant.
- **`customers.json`**: Output file mapping customer phone numbers to names.
- **`items.json`**: Output file with item names, prices, and order counts.

---

## Design

1. **Data Extraction:**
   - The script reads the order data from a JSON file, which is passed as the first argument.
   - It processes the data to extract relevant customer and item information.

2. **Data Output:**
   - **`customers.json`**: Stores phone numbers as keys and corresponding customer names as values.
   - **`items.json`**: Stores item names as keys, with details including price and number of orders as values.

3. **Data Structure:**
   - Orders in the input JSON are assumed to contain details like the customer name, phone number, item name, price, and quantity.

4. **Data Processing Logic:**
   - The script ensures phone numbers are formatted correctly as `xxx-xxx-xxxx`.
   - It accumulates the total number of orders per item and stores the first price it encounters for each item, assuming prices remain constant.

---

## Usage Instructions

1. **Requirements:**
   - Python 3.x
   - Install dependencies, if any, using:
     ```bash
     pip install -r requirements.txt
     ```

2. **How to Run:**
   - To execute the script, run the following command:
     ```bash
     python process_orders.py <input_file.json>
     ```
     Replace `<input_file.json>` with the path to the orders file (e.g., `example_orders.json`).

3. **Output:**
   - After running, you will find two new JSON files:
     - **customers.json:** Contains a dictionary with phone numbers and names.
     - **items.json:** Contains a dictionary with item names, prices, and the number of orders.

---

## Example

### Input (`example_orders.json`):
```json
[
  {
    "customer_name": "Karl",
    "phone_number": "609-555-0124",
    "items": [
      {"name": "Butter Masala Dosa", "price": 12.95, "quantity": 1},
      {"name": "Butter Mysore Masala Dosa", "price": 11.95, "quantity": 2}
    ]
  },
  ...
]
