import contextlib
import mysql.connector
from datetime import date, timedelta
import bcrypt

class UserDatabase:
    def __init__(self, route) -> None:
        self.route = route

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.route.config.host,
            user=self.route.config.user,
            passwd=self.route.config.passwd,
            database=self.route.config.database,
            port=self.route.config.port
        )
    
    def close(self):
        with contextlib.suppress(Exception):
            self.connection.close()

    def register_user(self, fullDataSet):
        camposTabela = ('name, user, password, date, acesso')
        qntd = ('%s, %s, %s, %s, %s')
        sql = f"INSERT INTO users ({camposTabela}) VALUES ({qntd})"
        mycursor = self.connection.cursor()
        try:
            mycursor.execute(sql, fullDataSet)
            self.connection.commit()
            return 'success'
        except Exception as e:            
            return str(e)
        
    def select_all_users(self):
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            mycursor.execute('SELECT idUser, name, user, acesso FROM users ORDER BY name')
            return mycursor.fetchall()
        
    def select_one_user(self, id):
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            sql = 'SELECT * FROM users WHERE idUser = %s'
            mycursor.execute(sql, (int(id),))
            return mycursor.fetchone()

    def delete_user(self, id):
        try:
            mycursor = self.connection.cursor()
            sql = 'DELETE FROM users WHERE idUser = %s'
            mycursor.execute(sql, (id,))
            self.connection.commit()
            return 'success'
        except Exception as e:
            return str(e)
        
    def update_user(self, fullDataSet):
        try:
            mycursor = self.connection.cursor()
            sql = """
                UPDATE users SET
                name = %s,
                user = %s,
                password = %s,
                date = %s,
                acesso = %s

                WHERE idUser = %s;
            """
            mycursor.execute(sql, fullDataSet[1:] + fullDataSet[:1])
            self.connection.commit()
            return 'success'
        except Exception as e:
            return str(e)
       
    def verify_pass(self, password, saved_hash):
        return bcrypt.checkpw(password.encode('utf-8'), saved_hash.encode('utf-8'))
    
    def login_verify(self, data):
        try:
            mycursor = self.connection.cursor()
            query = """
            SELECT name, password, acesso
            FROM users
            WHERE user = %s
            """
            mycursor.execute(query, (data[0],))
            result = mycursor.fetchone()
            
            if result:
                if self.verify_pass(data[1], result[1]):
                    return result[0].upper(), result[2]
            return None, None
        except Exception:
            return None, None
        
    def find_user(self, text):
        try:
            mycursor = self.connection.cursor()
            sql = "SELECT idUser, name, user, acesso FROM users WHERE idUser LIKE %s OR name LIKE %s OR user LIKE %s"
            pattern = f"%{text}%"
            mycursor.execute(sql, (pattern, pattern, pattern))
            return mycursor.fetchall()
        except Exception:
            return None
        
    def select_users_count(self):
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            sql = "SELECT COUNT(*) AS numb_of_users FROM users"
            mycursor.execute(sql)
            return str(mycursor.fetchone()[0])

class CustomerDatabase:
    def __init__(self, route) -> None:
        self.route = route

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.route.config.host,
            user=self.route.config.user,
            passwd=self.route.config.passwd,
            database=self.route.config.database,
            port=self.route.config.port    
        )

    def close(self):
        with contextlib.suppress(Exception):
            self.connection.close()

    def register_customer(self, fullDataSet):
        table_fields = ('name, cpf_cnpj, tel, email, observ, date')
        placeholders = ('%s, %s, %s, %s, %s, %s')
        query = f"INSERT INTO customers ({table_fields}) VALUES ({placeholders})"
        mycursor = self.connection.cursor()
        try:
            mycursor.execute(query, fullDataSet)
            self.connection.commit()
            return 'success'
        except Exception as e:
            return str(e)
        
    def register_adress(self, fullDataSet):
        table_fields = ('cod_customer, ender, cidade, uf, CEP')
        placeholders = ('%s, %s, %s, %s, %s')
        query = f"INSERT INTO adress ({table_fields}) VALUES ({placeholders})"
        mycursor = self.connection.cursor()
        try:
            mycursor.execute(query, fullDataSet)
            self.connection.commit()
            return 'success'
        except Exception as e:
            return str(e)

    def select_customers(self):
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            mycursor.execute("SELECT idcustomers, name, cpf_cnpj, tel FROM customers ORDER BY name")
            return mycursor.fetchall()
        
    def select_one_customer(self, cpf_cnpj):
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            query = "SELECT * FROM customers WHERE cpf_cnpj = %s ORDER BY name;"
            mycursor.execute(query, (cpf_cnpj,))
            data_customer = mycursor.fetchall()
            return data_customer
    
    def select_adresses(self, cpf_cnpj):
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            query = "SELECT ender, cidade, uf, CEP FROM adress WHERE cod_customer = %s ORDER BY cidade;"
            mycursor.execute(query, (cpf_cnpj,))
            data_adress = mycursor.fetchall()
            return data_adress

    def update_customer(self, data_customer):
        try:
            mycursor = self.connection.cursor()

            # Busca o CPF_CNPJ cadastrado
            query = "SELECT cpf_cnpj FROM customers WHERE idcustomers = %s;"
            mycursor.execute(query, (data_customer[0],))
            result = mycursor.fetchall()
            cpfCust = result[0][0]

            # Apaga todos os endereços existentes
            query_del = "DELETE FROM adress WHERE cod_customer = %s;"
            mycursor.execute(query_del, (cpfCust,))
            self.connection.commit()

            #Atualiza os dados do cliente
            query_upd_Cust = """
            UPDATE customers SET
            name = %s,
            cpf_cnpj = %s,
            tel = %s,
            email = %s,
            observ = %s

            WHERE idcustomers = %s;
            """
            mycursor.execute(query_upd_Cust, data_customer[1:] + data_customer[:1])
            self.connection.commit()
            return 'success'

        except mysql.connector.Error as e:
            return str(e)
        
    def delete_customer(self, cpf_cnpj):
        try:
            sql = "DELETE FROM adress WHERE cod_customer = %s"
            mycursor = self.connection.cursor()
            mycursor.execute(sql, (cpf_cnpj,))
            self.connection.commit()
        except Exception as e:
            return f"Erro ao excluir o endereço: {str(e)}"

        try:
            sql = "DELETE FROM customers WHERE cpf_cnpj = %s"
            mycursor = self.connection.cursor()
            mycursor.execute(sql, (cpf_cnpj,))
            self.connection.commit()
            return 'success'
        except Exception as e:
            return f"Erro ao excluir o Cliente: {str(e)}"

    def find_customer(self, text):
        try:
            mycursor = self.connection.cursor()
            sql = "SELECT idcustomers, name, cpf_cnpj, tel FROM customers WHERE idcustomers LIKE %s OR name LIKE %s OR cpf_cnpj LIKE %s OR tel LIKE %s"
            pattern = f"%{text}%"
            mycursor.execute(sql, (pattern, pattern, pattern, pattern))
            return mycursor.fetchall()
        except Exception as e:
            return str(e)

class ProductsDatabase:
    def __init__(self, route) -> None:
        self.route = route

    def connect(self):
        self.connection=mysql.connector.connect(
            host=self.route.config.host,
            user=self.route.config.user,
            passwd=self.route.config.passwd,
            database=self.route.config.database,
            port=self.route.config.port
        )

    def close(self):
        with contextlib.suppress(Exception):
            self.connection.close()        
        
    def register_category(self, category):
        query = 'INSERT INTO category (category) VALUES (%s);'
        try:
            mycursor = self.connection.cursor()
            mycursor.execute(query, (category, ))
            self.connection.commit()
            return 'success'
        except Exception as e:
            return e
        
    def register_brand(self, brand):
        query = 'INSERT INTO brand (brand) VALUES (%s);'
        try:
            mycursor = self.connection.cursor()
            mycursor.execute(query, (brand, ))
            self.connection.commit()
            return 'success'
        except Exception as e:
            return e

    def select_category(self):        
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            mycursor.execute('SELECT * FROM category ORDER BY category;')
            return mycursor.fetchall()

    def select_brand(self):
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            mycursor.execute('SELECT * FROM brand ORDER BY brand;')
            return mycursor.fetchall()

    def delete_category(self, idcategory):
        try:
            mycursor = self.connection.cursor()
            sql = 'DELETE FROM category WHERE idcategory = %s;'
            mycursor.execute(sql, (idcategory, ))
            self.connection.commit()
            return 'success'
        except Exception as e:
            return e
        
    def delete_brand(self, idbrand):
        try:
            mycursor = self.connection.cursor()
            sql = 'DELETE FROM brand WHERE idbrand = %s;'
            mycursor.execute(sql, (idbrand, ))
            self.connection.commit()
            return 'success'
        except Exception as e:
            return e

    def register_products(self, fulldataset):
        # Busca os ids da categoria e da marca para registro
        try:
            fulldataset_2 = fulldataset
            mycursor = self.connection.cursor()
            sql = 'SELECT idcategory FROM category WHERE category = %s'
            mycursor.execute(sql, (fulldataset[1], ))
            result = mycursor.fetchall()
            fulldataset_2[1] = result[0][0]
            sql = 'SELECT idbrand FROM brand WHERE brand = %s'
            mycursor.execute(sql, (fulldataset[2], ))
            result = mycursor.fetchall()
            fulldataset_2[2] = result[0][0]
        except Exception as e:
            return e
        
        # Inicia o processo de registro
        table_fields = ('descr, idcategory, idbrand, stock, minstock, maxstock, observ, costs, sellprice, margin')
        quantity = ('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s')
        query = f'INSERT INTO products ({table_fields}) VALUES ({quantity})'
        mycursor = self.connection.cursor()
        try:
            mycursor.execute(query, fulldataset_2)
            self.connection.commit()
            return 'success'
        except Exception as e:
            return e

    def select_products(self):
        try:
            mycursor = self.connection.cursor()
            sql = """
                SELECT CAST(products.idproducts AS CHAR) AS id_str, products.descr, category.category, brand.brand, FORMAT(products.sellprice, 2, 'de_DE') as sell, products.stock, products.minstock 
                FROM products
                JOIN category ON category.idcategory = products.idcategory
                JOIN brand ON brand.idbrand = products.idbrand                
                ORDER BY descr
            """
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            return e
    
    def select_products_full(self, idproducts):
        try:
            mycursor = self.connection.cursor()
            sql = """
                SELECT
                CAST(products.idproducts AS CHAR) AS idproducts_str,
                products.descr,
                category.category,
                brand.brand,
                CAST(products.stock AS CHAR) AS stock_str,
                CAST(products.minstock AS CHAR) AS minstock_str,
                CAST(products.maxstock AS CHAR) AS maxstock_str,
                products.observ,
                CAST(products.costs AS CHAR) AS costs_str,
                CAST(products.sellprice AS CHAR) AS sellprice_str,
                CAST(products.margin AS CHAR) AS margin_str
                FROM products
                JOIN category ON products.idcategory = category.idcategory
                JOIN brand ON products.idbrand = brand.idbrand
                WHERE IDPRODUCTS = %s
            """
            mycursor.execute(sql, (idproducts, ))
            return mycursor.fetchone()
        except Exception as e:
            print(e)

    def update_products(self, data_products):
        try:
            mycursor = self.connection.cursor()

            sql = "SELECT category.idcategory, brand.idbrand FROM category JOIN brand ON category.category = %s AND brand.brand = %s"
            mycursor.execute(sql, (data_products[2], data_products[3]))
            data_products[2], data_products[3] = mycursor.fetchone()
            
            sql = """
                UPDATE products SET
                descr = %s,
                idcategory = %s,
                idbrand = %s,
                stock = %s,
                minstock = %s,
                maxstock = %s,
                observ = %s,
                costs = %s,
                sellprice = %s,
                margin = %s

                WHERE idproducts = %s;
            """
            mycursor.execute(sql, data_products[1:] + data_products[:1])
            self.connection.commit()
            return 'success'
        except Exception as e:
            return e

    def delete_products(self, id_product):
        try:
            mycursor = self.connection.cursor()
            sql = "DELETE FROM products WHERE idproducts = %s"
            mycursor.execute(sql, (id_product,))
            self.connection.commit()
            return 'success'
        except Exception as e:
            return e

    def find_product(self, text):
        try:
            # Pesquisa todos os dados da tabela produtos por id, ou por descrição ou por marca ou por categoria ou por preço de venda
            mycursor = self.connection.cursor()
            param = f'%{text}%'
            sql = """
                SELECT DISTINCT CAST(products.idproducts AS CHAR) AS id_str, products.descr, category.category, brand.brand, FORMAT(products.sellprice, 2, 'DE_de') AS sell, products.stock, products.minstock
                FROM products
                JOIN category ON category.idcategory = products.idcategory
                JOIN brand ON brand.idbrand = products.idbrand
                WHERE idproducts LIKE %s OR descr LIKE %s OR sellprice LIKE %s OR category LIKE %s OR brand LIKE %s
                ORDER BY products.descr
            """
            mycursor.execute(sql, (param, param, param, param, param))
            final_result = mycursor.fetchall()
            return final_result
        except Exception as e:
            return e

    def find_product_by_code(self, id):
        try:
            mycursor = self.connection.cursor()
            sql = """
                SELECT products.idproducts, products.descr, products.idcategory, products.idbrand, products.sellprice, products.costs, products.stock, brand.brand
                FROM products
                JOIN brand ON products.idbrand = brand.idbrand
                WHERE idproducts = %s
            """
            mycursor.execute(sql, (id, ))
            result = mycursor.fetchone()
            return result or None
        except Exception as e:
            return e

    def find_product_by_description(self, descr):
        try:
            mycursor = self.connection.cursor()
            param = f'%{descr}%'
            sql = """
                SELECT products.idproducts, products.descr, products.idcategory, products.idbrand, products.sellprice, products.costs, products.stock, brand.brand
                FROM products
                JOIN brand ON products.idbrand = brand.idbrand
                WHERE descr LIKE %s
            """
            mycursor.execute(sql, (param, ))
            result = mycursor.fetchall()
            return result[0] if result else None
        except Exception as e:
            return e
    
    def update_stock(self, data):
        try:
            mycursor = self.connection.cursor()
            sql = "UPDATE products SET stock = stock + %s WHERE idproducts = %s"
            mycursor.execute(sql, (data[1], data[0]))
            self.connection.commit()
            return "success"
        except Exception as e:
            return e
        
    def select_low_stock(self):
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            sql = """
                SELECT CAST(products.idproducts AS CHAR) AS id_str, products.descr, category.category, brand.brand, FORMAT(products.sellprice, 2, 'de_DE') as sell, products.stock, products.minstock 
                FROM products
                JOIN category ON category.idcategory = products.idcategory
                JOIN brand ON brand.idbrand = products.idbrand
                WHERE stock <= minstock
                ORDER BY descr
            """
            mycursor.execute(sql)
            return mycursor.fetchall()

class SalesDatabase:
    def __init__(self, route) -> None:
        self.route = route

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.route.config.host,
            user=self.route.config.user,
            passwd=self.route.config.passwd,
            database=self.route.config.database,
            port=self.route.config.port
        )
    
    def close(self):
        with contextlib.suppress(Exception):
            self.connection.close()

    def register_sale(self, fulldataset):
        table_fields = ("idcustomer, date, total")
        quantity = ("%s, %s, %s")
        query = f"INSERT INTO sales ({table_fields}) VALUES ({quantity})"
        mycursor = self.connection.cursor()
        try:
            mycursor.execute(query, fulldataset)
            self.connection.commit()
            mycursor.execute("SELECT idsale FROM sales ORDER BY idsale DESC LIMIT 1")
            result = mycursor.fetchone()
            return "success", result[0]
        except Exception as e:
            return None, e

    def register_sold_products(self, fulldataset):
        table_fields = ("idsale, idproduct, quantity, unitprice, cost, total")
        quantity = ("%s, %s, %s, %s, %s, %s")
        query = f"INSERT INTO soldproducts ({table_fields}) VALUES ({quantity})"
        mycursor = self.connection.cursor()
        try:
            mycursor.execute(query, fulldataset)
            self.connection.commit()
            return "success"
        except Exception as e:
            return e
        
    def select_all_sales(self):
        try:
            mycursor = self.connection.cursor()
            mycursor.execute(
                """SELECT sales.idsale, sales.idcustomer, DATE_FORMAT(sales.date, '%d/%m/%Y'), sales.total, customers.name, customers.cpf_cnpj FROM sales
                JOIN customers ON sales.idcustomer = customers.idcustomers ORDER BY sales.date DESC;"""
            )
            return mycursor.fetchall()
        except Exception:
            return None

    def select_one_sale(self, idsale):
        try:
            mycursor = self.connection.cursor()
            sql = """
                SELECT sales.idsale, sales.idcustomer, DATE_FORMAT(sales.date, '%d/%m/%Y'), sales.total, customers.name, customers.cpf_cnpj FROM sales
                JOIN customers ON sales.idcustomer = customers.idcustomers WHERE idsale = %s;
            """
            mycursor.execute(sql, (idsale, ))
            return mycursor.fetchone()
        except Exception:
            return None

    def select_all_sold(self, idsale):
        try:
            mycursor = self.connection.cursor()
            sql = """
                SELECT idsoldproducts, idproduct, products.descr, brand.brand, quantity, unitprice, cost, total
                FROM soldproducts
                JOIN products ON products.idproducts = soldproducts.idproduct
                JOIN brand ON products.idbrand = brand.idbrand
                WHERE idsale = %s
            """
            mycursor.execute(sql, (idsale, ))
            return mycursor.fetchall()
        except Exception:
            return None

    def update_sale(self, id_sale, data_sale):
        fulldataset = data_sale
        fulldataset.append(id_sale)
        try:
            mycursor = self.connection.cursor()
            sql = """
                UPDATE sales SET
                idcustomer = %s,
                date = %s,
                total = %s

                WHERE idsale = %s;    
            """
            mycursor.execute(sql, fulldataset)
            self.connection.commit()
            return "success"
        except Exception as e:
            return e

    def delete_products_sold(self, id_sale):
        try:
            mycursor = self.connection.cursor()
            sql = "DELETE FROM soldproducts WHERE idsale = %s"
            mycursor.execute(sql, (id_sale, ))
            self.connection.commit()
            return "success"
        except Exception as e:
            return e

    def delete_sale(self, id_sale):
        try:
            mycursor = self.connection.cursor()
            sql = "DELETE FROM sales WHERE idsale = %s"
            mycursor.execute(sql, (id_sale, ))
            self.connection.commit()
            return "success"
        except Exception as e:
            return e
    
    def find_sale(self, text):
        try:
            mycursor = self.connection.cursor()
            param = f'%{text}%'
            sql = """
                SELECT sales.idsale, sales.idcustomer, DATE_FORMAT(sales.date, '%d/%m/%Y'), sales.total, customers.name, customers.cpf_cnpj
                FROM sales
                JOIN customers ON sales.idcustomer = customers.idcustomers
                WHERE sales.idsale LIKE %s OR sales.idcustomer LIKE %s OR customers.name LIKE %s OR customers.cpf_cnpj LIKE %s;
            """
            mycursor.execute(sql, (param, param, param, param))
            return mycursor.fetchall()
        except Exception as e:
            return e
    
    def select_sales_history(self, id_customer):
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            sql = "SELECT idsale, DATE_FORMAT(sales.date, '%d/%m/%Y'), total FROM sales WHERE idcustomer = %s ORDER BY sales.date"
            mycursor.execute(sql, (id_customer, ))
            return mycursor.fetchall()

    def select_sold_history(self, id_product):
        mycursor = self.connection.cursor()
        sql = """
            SELECT sales.idsale, DATE_FORMAT(sales.date, '%d/%m/%Y'), soldproducts.total FROM soldproducts
            JOIN sales ON soldproducts.idsale = sales.idsale WHERE idproduct = %s ORDER BY sales.date;
        """
        mycursor.execute(sql, (id_product,))
        return mycursor.fetchall()

    def select_sales_from_previous_tirthy(self):
        limit_date = date.today() - timedelta(days=30)
        try:
            mycursor = self.connection.cursor()
            mycursor.execute(
                f"""SELECT sales.idsale, sales.idcustomer, DATE_FORMAT(sales.date, '%d/%m/%Y'), sales.total, customers.name, customers.cpf_cnpj FROM sales
                JOIN customers ON sales.idcustomer = customers.idcustomers
                WHERE sales.date >= '{limit_date}'
                ORDER BY sales.date DESC;"""
            )
            return mycursor.fetchall()
        except Exception:
            return None
    
    def select_sales_from_previous_seven(self):
        limit_date = date.today() - timedelta(days=7)
        try:
            mycursor = self.connection.cursor()
            mycursor.execute(
                f"""SELECT sales.idsale, sales.idcustomer, DATE_FORMAT(sales.date, '%d/%m/%Y'), sales.total, customers.name, customers.cpf_cnpj FROM sales
                JOIN customers ON sales.idcustomer = customers.idcustomers
                WHERE sales.date >= '{limit_date}'
                ORDER BY sales.date DESC;"""
            )
            return mycursor.fetchall()
        except Exception:
            return None
        
    def select_sales_from_today(self):
        today = date.today()
        try:
            mycursor = self.connection.cursor()
            mycursor.execute(
                f"""SELECT sales.idsale, sales.idcustomer, DATE_FORMAT(sales.date, '%d/%m/%Y'), sales.total, customers.name, customers.cpf_cnpj FROM sales
                JOIN customers ON sales.idcustomer = customers.idcustomers
                WHERE sales.date >= '{today}'
                ORDER BY sales.date DESC;"""
            )
            return mycursor.fetchall()
        except Exception:
            return None

class DashboardDatabase:
    def __init__(self, route) -> None:
        self.route = route

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.route.config.host,
            user=self.route.config.user,
            passwd=self.route.config.passwd,
            database=self.route.config.database,
            port=self.route.config.port
        )

    def close(self):
        with contextlib.suppress(Exception):
            self.connection.close()

    def select_percent_stock(self):
        try:
            query = "SELECT (SUM(stock) / SUM(maxstock)) * 100 AS percent FROM products"
            mycursor = self.connection.cursor()
            mycursor.execute(query)
            result = mycursor.fetchone()
            if result:
                return int(result[0])
            return 0
        except Exception:
            return 0

    def select_most_profitable(self):
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            # select the five most profitable products and return: product_id, profit_value, description
            mycursor.execute("""SELECT
                             soldproducts.idproduct,
                             CAST( SUM(soldproducts.total - (soldproducts.quantity * soldproducts.cost)) AS SIGNED INTEGER ) AS profit,
                             products.descr
                             FROM soldproducts JOIN products WHERE products.idproducts = soldproducts.idproduct
                             GROUP BY soldproducts.idproduct
                             ORDER BY profit DESC
                             LIMIT 5
                             """)
            return mycursor.fetchall()

    def select_sales_by_months(self, dates_data):
        with contextlib.suppress(Exception):
            final_result = []
            mycursor = self.connection.cursor()
            sql = "SELECT SUM(total) as sum_of_total FROM sales WHERE date BETWEEN %s AND %s"
            for dates in dates_data:
                mycursor.execute(sql, dates)
                result = mycursor.fetchone()[0]
                final_result.append(0 if result is None else round(result, 2))
            return final_result

    def select_numb_of_customers(self):
        today = date.today()
        first_day_of_month = date(today.year, today.month, 1)
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            mycursor.execute("SELECT COUNT(*) AS numb_of_customers FROM customers")
            numb_of_customers = mycursor.fetchone()[0]
            mycursor.execute(f"SELECT COUNT(*) AS numb_of_cutomers_past FROM customers WHERE date < '{first_day_of_month}'")
            numb_of_customers_past = mycursor.fetchone()[0]
            return numb_of_customers, numb_of_customers_past

    def select_today_sales_billing(self):
        today = date.today()
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            mycursor.execute(f"SELECT COUNT(*), SUM(total) FROM sales WHERE date = '{today}'")
            return mycursor.fetchone()
        
    def select_numb_of_products_and_stock(self):
        with contextlib.suppress(Exception):
            mycursor = self.connection.cursor()
            mycursor.execute("SELECT COUNT(*) FROM products")
            numb_of_products = mycursor.fetchone()[0]
            mycursor.execute("SELECT COUNT(*) FROM products WHERE stock <= minstock")
            low_stock = mycursor.fetchone()[0]
            return numb_of_products, low_stock