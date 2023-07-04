class restro:

    def __init__(self):
        self.menu_items={}
    
    def add_item_menu(self,item,price):
        self.menu_items[item]=price
    def print_menu_items(self):
        for item, price in self.menu_items.items():
            print("{}: {}".format(item, price))      
    def order_item(self,item):
        #for i in self.menu_items.items():
            print(item)        
            
r=restro()
r.add_item_menu('burger',99)
r.add_item_menu('Pizza',100)
r.add_item_menu('maxicun',200)
r.add_item_menu('sandwich',150)
r.print_menu_items()
r.order_item('burger')
