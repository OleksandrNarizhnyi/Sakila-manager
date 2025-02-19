from add_and_update_created_db import *
from display import display_results
from query_manager import *

def handle_user_input(query_handler):
    create_tables()

    while True:
        user_choice = input("""Введите\n
        GENRES для поиска по жанрам\n
        KEY - для поиска по ключевому слову\n
        SEARCHED - для получения самых частых запросов\n
        EXIT - для выхода\n: """).strip().lower()

        if user_choice == 'exit':
            query_handler.close()
            break

        if user_choice == 'genres':

            genres = query_handler.get_all_category()
            if not genres:
                print("Жанры не найдены.")
                continue
            display_results(genres)
            genre = input("Введите название жанра, выбрав из выше перечисленных: ").strip().capitalize()
            years = query_handler.get_all_year()
            for year in years:
                print("Доступные года:\n", year.get('release_year'))
            year = int(input("Введите год выпуска фильмов, выбрав из выше перечисленных: "))

            if year < 1901 or year > 2155:
                print("Пожалуйста, введите корректный год.")
                continue
            add_or_update_count_genre_year(genre, year)
            result_gen = query_handler.get_film_by_category_and_year(genre, year)
            display_results(result_gen)

        elif user_choice == 'key':
            keyword = input("Введите слово для поиска: ").strip()
            add_or_update_count_keywords(keyword)
            result_kw = query_handler.get_films_by_keyword(keyword)
            display_results(result_kw)

        elif user_choice == 'searched':
            search_res_key = get_search_rating_keywords()
            print("Самые частые запросы по ключевому полю: ")
            display_results(search_res_key)
            search_res_gen = get_search_rating_genres()
            print("Самые частые запросы по жанру и году: ")
            display_results(search_res_gen)

        else:
            print("Некорректный выбор. Пожалуйста, выберите один из предложенных вариантов.")