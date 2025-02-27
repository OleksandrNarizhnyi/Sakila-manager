from add_and_update_created_db import *


def handle_user_input(query_handler):
    create_tables()

    while True:
        user_choice = input("\nВведите:\n"
                    "GENRES - для поиска по жанрам\n"
                    "KEY - для поиска по ключевому слову\n"
                    "SEARCHED - для получения самых частых запросов\n"
                    "EXIT - для выхода\n: ").strip().lower()

        if user_choice == 'exit':
            query_handler.close()
            break

        try:
            if user_choice == 'genres':
                genres = query_handler.get_all_category()
                if not genres:
                    print("\nЖанры не найдены.")
                    continue
                print("\nДоступные жанры:\n")
                for category in genres:
                    print(category.get('name'))
                genre = input("\nВведите название жанра, выбрав из выше перечисленных: ").strip().capitalize()
                years = query_handler.get_all_year()
                print("\nДоступные года:\n")
                for year in years:
                    print(year.get('release_year'))
                try:
                    year = int(input("\nВведите год выпуска фильмов, выбрав из выше перечисленных: "))
                    if year < 1980 or year > 2025:
                        print("\nПожалуйста, введите корректный год.")
                        continue
                except ValueError:
                    print("\nПожалуйста, введите число.")
                    continue
                add_or_update_count_genre_year(genre, year)
                result_gen = query_handler.get_film_by_category_and_year(genre, year)
                if result_gen:
                    print(f"\nРезультат поиска по жанру: --{genre}-- и году выпуска: --{year}--\n")
                    [print(row.get('title', 'Без названия'), row.get('description', 'Нет описания'), sep=' -- ') for row in result_gen]
                else:
                    print(f"\nВведены некорректные данные. Фильмы по жанру: --{genre}-- и году выпуска: --{year}-- не найдены\n")

            elif user_choice == 'key':
                keyword = input("\nВведите слово для поиска: ").strip()
                add_or_update_count_keywords(keyword)
                result_kw = query_handler.get_films_by_keyword(keyword)
                if not result_kw:
                    print(f"\nПо ключевому слову '{keyword}' ничего не найдено.")
                    continue
                print(f"\nРезультат поиска по ключевому слову: --{keyword}--\n")
                [print(f"Название фильма: {row.get('title')} -- Описание фильма: {row.get('description')}") for row in
                 result_kw]

            elif user_choice == 'searched':
                search_res_key = get_search_rating_keywords()
                print("\nТОП-3 запроса по ключевому полю: \n")
                for res in search_res_key:
                    print(f"Ключевое слово: {res[0]} -- Количество вводов: {res[1]}")
                search_res_gen = get_search_rating_genres()
                print("\nТОП-3 запроса по жанру и году: \n")
                for res in search_res_gen:
                    print(f"Жанр: {res[0]}, Год: {res[2]}, Количество вводов: {res[1]}")

            else:
                print("\nНекорректный выбор. Пожалуйста, выберите один из предложенных вариантов.")
        except Exception as e:
            print(f"\nПроизошла ошибка: {e}")
            continue