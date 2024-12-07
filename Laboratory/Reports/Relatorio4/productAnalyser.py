class ProductAnalyzer:
    def __init__(self, db):
        """
        Initializes the ProductAnalyzer with a MongoDB collection.

        Parameters:
        db (Database): An instance of the Database class that contains a collection to be analyzed.
        """
        self.collection = db.collection  # Using collection from MongoDB

    def get_total_sales_per_day(self):
        """
        Returns the total sales amount for each day.

        This method calculates the total amount spent on products per day by unwinding the
        'produtos' array and grouping the sales by 'data_compra'.

        Returns:
        list: A list of dictionaries containing the date and total sales amount for that date.
        """
        pipeline = [
            {
                "$unwind": "$produtos"
            },  # Breaks down the 'produtos' array into individual documents
            {
                "$group": {
                    "_id": "$data_compra",  # Groups documents by the date of purchase
                    "total_vendas": {
                        "$sum": {
                            "$multiply": [
                                "$produtos.quantidade",
                                "$produtos.preco",
                            ]  # Calculates total sales
                        }
                    },
                }
            },
            {"$sort": {"_id": 1}},  # Sorts the results by date
        ]
        result = list(
            self.collection.aggregate(pipeline)
        )  # Executes the aggregation pipeline
        return result

    def get_most_sold_product(self):
        """
        Returns the most sold product across all purchases.

        This method finds the product with the highest quantity sold by unwinding the
        'produtos' array and grouping by 'descricao'.

        Returns:
        list: A list of one dictionary containing the product description and the total quantity sold.
        """
        pipeline = [
            {
                "$unwind": "$produtos"
            },  # Breaks down the 'produtos' array into individual documents
            {
                "$group": {
                    "_id": "$produtos.descricao",  # Groups documents by product description
                    "total_vendido": {
                        "$sum": "$produtos.quantidade"
                    },  # Calculates total quantity sold
                }
            },
            {
                "$sort": {"total_vendido": -1}
            },  # Sorts the results by total quantity sold in descending order
            {"$limit": 1},  # Limits the result to the top one product
        ]
        result = self.collection.aggregate(
            pipeline
        )  # Executes the aggregation pipeline
        return list(result)

    def get_highest_spending_customer(self):
        """
        Returns the customer who spent the most in a single purchase.

        This method calculates the total amount spent by each customer in each purchase
        and returns the customer with the highest spending.

        Returns:
        list: A list of one dictionary containing the customer ID and the total amount spent.
        """
        pipeline = [
            {
                "$unwind": "$produtos"
            },  # Breaks down the 'produtos' array into individual documents
            {
                "$group": {
                    "_id": "$cliente_id",  # Groups documents by customer ID
                    "total_gasto": {
                        "$sum": {
                            "$multiply": [
                                "$produtos.quantidade",
                                "$produtos.preco",
                            ]  # Calculates total amount spent
                        }
                    },
                }
            },
            {
                "$sort": {"total_gasto": -1}
            },  # Sorts the results by total spending in descending order
            {"$limit": 1},  # Limits the result to the top one customer
        ]
        result = self.collection.aggregate(
            pipeline
        )  # Executes the aggregation pipeline
        return list(result)

    def get_products_sold_above_one_unit(self):
        """
        Returns a list of products that were sold in quantities greater than one unit.

        This method finds all products where the total quantity sold is greater than one
        by unwinding the 'produtos' array and grouping by 'descricao'.

        Returns:
        list: A list of dictionaries containing product descriptions and the total quantities sold.
        """
        pipeline = [
            {
                "$unwind": "$produtos"
            },  # Breaks down the 'produtos' array into individual documents
            {
                "$group": {
                    "_id": "$produtos.descricao",  # Groups documents by product description
                    "total_vendido": {
                        "$sum": "$produtos.quantidade"
                    },  # Calculates total quantity sold
                }
            },
            {
                "$match": {"total_vendido": {"$gt": 1}}
            },  # Filters products with a total quantity sold greater than 1
            {
                "$sort": {"total_vendido": -1}
            },  # Sorts the results by total quantity sold in descending order
        ]
        result = self.collection.aggregate(
            pipeline
        )  # Executes the aggregation pipeline
        return list(result)
