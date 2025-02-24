class SakilaQueries:
    GET_ALL_CATEGORY = "SELECT name FROM category"

    GET_ALL_YEAR = "SELECT DISTINCT release_year FROM film ORDER BY release_year"

    FILMS_BY_KEYWORD = """
            SELECT title, release_year, description 
            from film
            where title like  %s
            or description like  %s
            """

    FILMS_BY_GENRE_AND_YEAR = """
            select title, description 
            from film as f
            join film_category as f_c 
            on f.film_id = f_c.film_id
            join category as c 
            on f_c.category_id = c.category_id
            where c.name = %s and f.release_year = %s
            limit 10
            """


class SQLiteQueries:

    RATING_KEYWORDS = """
                    SELECT keyword, count 
                    FROM count_keywords
                    ORDER BY count desc limit 3
                """

    RATING_GENRES = """
                    SELECT genre, count, year 
                    FROM count_genre_year
                    ORDER BY count desc limit 3
                """