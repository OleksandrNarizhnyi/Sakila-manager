def display_results(results):
    if not results:
        print("Ничего не найдено.")
        return
    for result in results:
        print(result)