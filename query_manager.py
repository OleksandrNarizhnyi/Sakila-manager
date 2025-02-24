from pymysql.err import OperationalError
from db_connection import DBConnector

class QueryHandler(DBConnector):
    def __init__(self, dbconfig):
        super().__init__(dbconfig)

    def get_all_category(self):
        try:
            cursor = self.get_cursor()
            cursor.execute("SELECT name FROM category")
            return cursor.fetchall()
        except OperationalError as e:
            print(f"Ошибка при получении категорий: {e}")
            return []

    def get_all_year(self):
        try:
            cursor = self.get_cursor()
            cursor.execute("SELECT DISTINCT release_year FROM film ORDER BY release_year")
            return cursor.fetchall()
        except OperationalError as e:
            print(f"Ошибка при получении годов: {e}")
            return []

    def get_films_by_keyword(self, keyword: str):
        try:
            cursor = self.get_cursor()
            cursor.execute("""
            SELECT title, release_year, description 
            from film
            where title like  %s
            or description like  %s
            """,
            (f"%{keyword}%", f"%{keyword}%"))
            return cursor.fetchall()
        except OperationalError as e:
            print(f"Ошибка при поиске по ключевому слову: {e}")
            return []

    def get_film_by_category_and_year(self, category: str, year: int):
        try:
            cursor = self.get_cursor()
            cursor.execute("""
            select title, description 
            from film as f
            join film_category as f_c 
            on f.film_id = f_c.film_id
            join category as c 
            on f_c.category_id = c.category_id
            where c.name = %s and f.release_year = %s
            limit 10
            """, (category, year))
            return cursor.fetchall()
        except OperationalError as e:
            print(f"Ошибка при поиске по ключевому слову: {e}")
            return []

    def close(self):
        self.get_cursor().close()

