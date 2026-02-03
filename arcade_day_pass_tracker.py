# 🕹️ Arcade Day Pass Tracker — Challenge Steps
# A simple management tool to calculate tokens and costs for arcade customers.

# --- 1) Setup & User Input
customer_name = input("Enter customer name: ")
num_passes = int(input("How many passes purchased? "))
tokens_per_pass = 30
price_per_pass = 12.50
tokens_per_game = 2

# --- 2) Business Logic ---
total_tokens = num_passes*tokens_per_pass 
total_cost = num_passes*price_per_pass 

#Using floor division (//) to ensure we only show playable whole games
games_available = total_tokens //tokens_per_game

# --- 3) Summary Output
print(f"\n {'='*10} ARCADE DAY PASS {'='*10}")
print(f"Customer:         {customer_name}")
print(f"Passes Bought:    {num_passes}")
print(f"Total Tokens:     {total_tokens}")
print(f"Total Cost:       {total_tokens}")
print(f"Games Playable:   {games_available}")
print(f"{'='*32}")
