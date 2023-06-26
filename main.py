from database import create_table, insert_interface
from interface_parser import parse_json_data

def main():
    try:
        # Create table
        create_table()
        print("Table created successfully")

        # Parse JSON data
        data = parse_json_data('config.json')

        # Insert each interface into the DB
        for interface in data:
            insert_interface(interface)
        
        print("Data inserted successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
