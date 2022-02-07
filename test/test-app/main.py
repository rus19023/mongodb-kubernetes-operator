import os
import sys

from pymongo import MongoClient


def main() -> int:
    connection_string = os.getenv("CONNECTION_STRING")
    client = MongoClient(connection_string)

    try:
        client.db.col.insert_one({})
    except Exception as e:
        print(f"Error inserting document {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
