class Order:
    def __init__(self, items:list[str], total_price:float):
        self.items = items
        self.total_price = total_price

class InvoicePrinter:
    @staticmethod
    def print_items(order:Order):
        for item in order.items:
            print(item,end=" ")
        print(f"price: {order.total_price}")


