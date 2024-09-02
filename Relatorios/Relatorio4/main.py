from database import Database
from helper.writeAJson import writeAJson
from productAnalyser import ProductAnalyzer

db = Database(database="mercado", collection="compras")
# db.resetDatabase()

analyzer = ProductAnalyzer(db)

# Total sales per day
total_sales = analyzer.get_total_sales_per_day()
writeAJson(total_sales, "total_sales_per_day")

# Most sold product
most_sold_product = analyzer.get_most_sold_product()
writeAJson(most_sold_product, "most_sold_product")

# Customer with highest spending
highest_spending_customer = analyzer.get_highest_spending_customer()
writeAJson(highest_spending_customer, "highest_spending_customer")

# Products sold above one unit
products_above_one_unit = analyzer.get_products_sold_above_one_unit()
writeAJson(products_above_one_unit, "products_sold_above_one_unit")
