from pymysql.err import OperationalError
from db_connection import DBConnector
from sql_queries import SakilaQueries

class QueryHandler(DBConnector):
    def __init__(self, dbconfig):
        super().__init__(dbconfig)

    def get_all_category(self):
        try:
            cursor = self.get_cursor()
            cursor.execute(SakilaQueries.GET_ALL_CATEGORY)
            return cursor.fetchall()
        except OperationalError as e:
            print(f"Ошибка при получении категорий: {e}")
            return []

    def get_all_year(self):
        try:
            cursor = self.get_cursor()
            cursor.execute(SakilaQueries.GET_ALL_YEAR)
            return cursor.fetchall()
        except OperationalError as e:
            print(f"Ошибка при получении годов: {e}")
            return []

    def get_films_by_keyword(self, keyword: str):
        try:
            cursor = self.get_cursor()
            cursor.execute(SakilaQueries.FILMS_BY_KEYWORD,(f"%{keyword}%", f"%{keyword}%"))
            return cursor.fetchall()
        except OperationalError as e:
            print(f"Ошибка при поиске по ключевому слову: {e}")
            return []

    def get_film_by_category_and_year(self, category: str, year: int):
        try:
            cursor = self.get_cursor()
            cursor.execute(SakilaQueries.FILMS_BY_GENRE_AND_YEAR, (category, year))
            return cursor.fetchall()
        except OperationalError as e:
            print(f"Ошибка при поиске по ключевому слову: {e}")
            return []



