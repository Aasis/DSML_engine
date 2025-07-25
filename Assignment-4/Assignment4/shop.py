class Product_list:
    # i created a class attributes which has department as a key and value consist of another dictionary of item name and no of items left 
    
    def __init__(self):
        self.department=[]
        self.cart_items=[]
        self.a=1
        self.total=0
        self.discount_amount=0
        self.items_list= {
        "Apparel_Accessories": {
            1:["Men's Classic Denim Jeans",1000,10],
            2:["Women's Floral Maxi Dress",1050,10],
            3:["Unisex Basic White T-Shirt",550,10],
            4:["Leather Wallet with RFID Protection",1500,10],
            5:["Sterling Silver Pendant Necklace",3000,10],
            6:["Sporty Running Shoes",1800,10],
            7:["Cashmere Scarf",750,10],
            8:["Wool Blend Winter Coat",3500,10],
            9:["Kids' Graphic Hoodie",1250,10],
            10:["Polarized Sunglasses",5000,10]
        },
        "Home Goods & Decor":{
            1:["Ceramic Dinnerware Set (4 Place Settings)",25000,10],
            2:["Memory Foam Pillow",600,10],
            3:["Weighted Blanket",500,10],
            4:["Scented Soy Candle (Lavender)",200,10],
            5:["Decorative Throw Pillow",350,10],
            6:["Stainless Steel Cookware Set",50,10],
            7:["Art Print (Abstract Landscape)",300,10],
            8:["Plush Bath Towel Set",200,10],
            9:["Smart LED Light Bulbs",100,10],
            10:["Area Rug (Geometric Pattern)",300,10]
        },
        "Electronics":{
            1:["Wireless Noise-Canceling Headphones",3500,10],
            2:["Portable Bluetooth Speaker",650,10],
            3:["Smartwatch with Heart Rate Monitor",1200,10],
            4:["4K Ultra HD Smart TV",550000, 10],
            5:["Laptop Computer (13-inch Ultrabook)",250000,10],
            6:["External Solid State Drive (1TB)",8000,10],
            7:["Wireless Charging Pad",750,10],
            8:["Digital Instant Camera",35000,10],
            9:["Home Security Camera System",3500,10],
            10:["Gaming Mouse and Keyboard Combo",1000,10]
        },
        "Groceries & Food":{
            1:["Organic Whole Milk",120,10],
            2:["Artisan Sourdough Bread",200,10],
            3:["Fresh Berries (Mixed Pack)",350,10],
            4:["Ground Coffee (Medium Roast)",1999,10],
            5:["Extra Virgin Olive Oil",1500,10],
            6:["Pasta Sauce (Marinara)",850,10],
            7:["Assorted Cheese Platter",550,10],
            8:["Granola Bars (Variety Pack)",650,10],
            9:["Sparkling Water (Lemon-Lime)",350,10],
            10:["Dark Chocolate Bar (70% Cacao)",650,10]
            },
        "Toys & Games":{
            1:["Building Block Set (Advanced)",6500,10],
            2:["Action Figure (Superhero)",3000,10],
            3:["Board Game (Strategy)",1200,10],
            4:["Plush Animal (Large Teddy Bear)",12300,10],
            5:["Remote Control Car",6500,10],
            6:["Jigsaw Puzzle (1000 Pieces)",1000,10],
            7:["Art Supplies Kit (Deluxe)",6541,10],
            8:["Dolls House with Furniture",9000,10],
            9:["Educational Robot Kit",6890,10],
            10:["Outdoor Play Tent",15000,10]
        },
        "Books & Media":{
            1:["Bestselling Fiction Novel",350,10],
            2:["Non-Fiction Biography",350,10],
            3:["Children's Picture Book",650,10],
            4:["Cookbook (International Cuisine)",550,10],
            5:["Self-Help Guide",550,10],
            6:["Vinyl Record (Classic Rock Album)",650,10],
            7:["Blu-ray Movie (Action)",900,10],
            8:["Audiobook Subscription Card",1000,10],
            9:["E-Reader Device",660,10],
            10:["Magazine Subscription (Fashion)",36,10]
        }
    }
    def Display(self):
        self.a=1
        
        for key,value in self.items_list.items():
            self.department.append(key)
        print(" ========= SELECT DEPARTMENT =============")
        
        for i in self.department:
            print(f"{self.a}------------>>{i}")
            self.a=self.a+1
        choice = int(input("Select department ( 1-6 ):"))
        self.department[choice-1]
        ITEMS=self.items_list.copy()
        Items_list=ITEMS.get(self.department[choice-1])
        for key1,value1 in Items_list.items():
            print(f"{key1}---{value1}")
        choose_item=int(input("Select item (1-10):"))
        choose_quantity=int(input("Select Quantity :"))
      #  product.update(items_list[choose_item])
         # update garne kam garyo hai 
        self.items_list.get(self.department[choice-1])[choose_item][2] = self.items_list.get(self.department[choice-1])[choose_item][2] - choose_quantity
        Items_list[choose_item][2]= choose_quantity
        self.cart_items.append(Items_list[choose_item])
        self.a=0 # comedy bug
   
    def update(self):
        #yesma can i use lamda function ? 
        print(self.cart_items)
        #print(self.items_list) ---- yesma main list mai changes aairako xa 

    def Total_price(self,amount):
        for i in self.cart_items:
            print(i)
            self.total= self.total+ (i[1]*i[2])
        self.discount_amount=self.total*(amount/100)
        
        
       # print(self.total=i[1]*i[2])

    def show_total(self):
        print(f"before discount = {self.total}")
        print(f"Discounted amount = {self.discount_amount}")
        self.total = self.total-self.discount_amount
        print(f"after discount total amount = {self.total}")
    
    
        
        