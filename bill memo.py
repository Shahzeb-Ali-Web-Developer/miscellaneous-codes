class Bill:
    def __init__(self, id, name, date, address):
        self.shop = "MOBILO - Mobile City"
        self.tagline = "Deals in new and used mobile phone & accessories."
        self.cell = 923001234867
        self.location = "Shop # 12, Ghalib Market, Lahore"
        self.type = "Cash Memo"

        self.id = id
        self.name = name
        self.date = date
        self.address = address



    def __str__(self):

        return (f'{self.shop}\n{self.tagline}\nCell: {self.cell}\n'
                f'\nBill ID: {self.id}\tCustomer Name: {self.name}\tDate: {self.date}\tAddress: {self.address}\n'
                f'\n----------------{self.type}----------------\n'
                f'\nItem\t\t\tPrice\t\tQty\t\tTotal\n')

    def items(self, itemslist):
        for item in itemslist:
            for obj in item:
                print(obj, end="\t\t")
            print()

        total = 0
        for item in itemslist:
            for i, price in enumerate(item):
                if i == 3:
                    total += price

        print(f"\nSignature _________\t\t\tTotal: {total}\n"
              f"\nAddress: {self.location}")


def main():
    Hasaan = Bill(2, "Hasaan", "30/10/2023", "Gulberg")
    print(Hasaan)
    Hasaan.items([["Handsfree", 1200, 2, 2400], ["Back Cover", 1500, 2, 5000], ["9D Glass", 1000, 3, 3000]])

if __name__ == '__main__':
    main()



