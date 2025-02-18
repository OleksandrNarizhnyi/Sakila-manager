from db_config import dbconfig
from user_interface import handle_user_input
from query_manager import QueryHandler

def main():
    query_handler = QueryHandler(dbconfig)
    handle_user_input(query_handler)

if __name__ == "__main__":
    main()

