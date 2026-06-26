portfolio = {
    "APPLE": {"price": 150, "quantity": 10},
    "GOOGLE": {"price": 2800, "quantity": 2},
    "TESLA": {"price": 700, "quantity": 5}
}
def add_stock(portfolio, stock, price, shares):
    if stock in portfolio:
        portfolio[stock]["quantity"] += shares
    else:
        portfolio[stock] = {"price": price, "quantity": shares}
def view_portfolio(portfolio):
    print("Your Stock Portfolio:")
    for stock, details in portfolio.items():
        print(f"{stock}: {details['quantity']} shares at ${details['price']} each")
def total_value(portfolio):
    total = 0
    for stock, details in portfolio.items():
        total += details["price"] * details["quantity"]
    return total
def remove_stock(portfolio, stock, shares):
    if stock in portfolio:
        if portfolio[stock]["quantity"] >= shares:
            portfolio[stock]["quantity"] -= shares
            if portfolio[stock]["quantity"] == 0:
                del portfolio[stock]
        else:
            print(f"Not enough shares of {stock} to remove.")
    else:
        print(f"{stock} not found in portfolio.")
def menu():
    while True:
        print("\n1. Add stock")
        print("2. Remove stock")
        print("3. View portfolio")
        print("4. Total value")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            stock = input("Enter stock name: ")
            price = float(input("Enter stock price: "))
            shares = int(input("Enter number of shares: "))
            add_stock(portfolio, stock, price, shares)
        elif choice == "2":
            stock = input("Enter stock name: ")
            shares = int(input("Enter number of shares to remove: "))
            remove_stock(portfolio, stock, shares)
        elif choice == "3":
            view_portfolio(portfolio)
        elif choice == "4":
            print(f"Total portfolio value: ${total_value(portfolio):.2f}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")