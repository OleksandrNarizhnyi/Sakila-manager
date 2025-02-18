
from db_connection import DBConnector

class QueryHandler(DBConnector):
    def __init__(self, dbconfig):
        super().__init__(dbconfig)

    def get_all_category(self):
        with self.get_cursor() as cursor:
            cursor.execute("SELECT name from category")
            record = cursor.fetchall()
        return record

    def get_all_year(self):
        with self.get_cursor() as cursor:
            cursor.execute("SELECT release_year from film")
            record = cursor.fetchall()
        return record

    def get_films_by_keyword(self, keyword: str):
        with self.get_cursor() as cursor:
            cursor.execute("""
        SELECT title, release_year, description 
        from film
        where title like  %s
        or description like  %s
        """,
        (f"%{keyword}%", f"%{keyword}%"))
            record = cursor.fetchall()
        return record

    def get_film_by_category_and_year(self, category: str, year: int):
        with self.get_cursor() as cursor:
            cursor.execute("""
        select title, description 
        from film as f
        join film_category as f_c on f.film_id = f_c.film_id
        join category as c on f_c.category_id = c.category_id
        where c.name = %s or f.release_year = %s
        limit 10
        """, (category, year))
            record = cursor.fetchall()
        return record


