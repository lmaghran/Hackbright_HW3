melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00



def customer_underpayment(customer_name, melons_purchased, customer_paid, melon_cost=1):
  customer_expected= melons_purchased* melon_cost
  if customer_paid != customer_expected:
        print(f"{customer_name} paid ${customer_paid:.2f},",
          f"expected ${customer_expected:.2f}"
          )

customer_underpayment("Joe", 5, 5)
customer_underpayment("Frank", 6, 6)
customer_underpayment("Sally", 3, 3)
customer_underpayment("Sean", 9, 9.5)
customer_underpayment("David", 4, 4)
customer_underpayment("Ashley", 3,2)
