# 1. Hardcoded dictionary 
stock_prices = {"AAPL": 180, "TSLA": 250}

print("--- Stock Portfolio Tracker ---")
print(f"Available Stocks: {', '.join(stock_prices.keys())}")
print("Exit karne ke liye 'done' dalein.\n")

total_investment = 0
portfolio_items = []  

# 2. Input & Calculation Loop
while True:
    stock_name = input("Stock symbol dalein: ").upper().strip()
    
    if stock_name == "DONE":
        break
        
    if stock_name in stock_prices:
        quantity = int(input(f"{stock_name} ki quantity dalein: "))
        
        
        cost = stock_prices[stock_name] * quantity
        total_investment += cost
        
        
        line = f"{stock_name}: {quantity} shares @ {stock_prices[stock_name]} = {cost}"
        portfolio_items.append(line)
        print(f"-> Added successfully!\n")
    else:
        print("Stock available nahi hai. Dobara try karein.\n")

# 3. Final Result Display
print("\n--- Final Portfolio Summary ---")
for item in portfolio_items:
    print(f"- {item}")
print(f"Total Portfolio Value: ${total_investment}")

# 4. File Handling 
if total_investment > 0:
    save_choice = input("\nKya aap details save karna chahte hain? (yes/no): ").lower().strip()
    if save_choice in ["yes", "y"]:
        with open("portfolio.txt", "w") as file:
            file.write("--- Stock Portfolio Tracker ---\n")
            for item in portfolio_items:
                file.write(f"- {item}\n")
            file.write(f"Total Portfolio Value: ${total_investment}\n")
        print("Data 'portfolio.txt' me save ho gaya!")
