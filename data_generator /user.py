from faker import Faker
import sqlite3

fake = Faker()



def generate_user_data(num_user_records: int) -> None:
    for id in range(num_user_records):
        db_connection = sqlite3.connect("online_store.db")
        cursor = db_connection.cursor()
        
        cursor.execute(
            """INSERT INTO commerce.users
                (id, username, password) VALUES (%s, %s, %s)""",
                (id, fake.user_name(), fake.password()),
        )

        cursor.execute(
            """INSERT INTO commerce.products
                (id, name, description, price) VALUES (%s, %s, %s, %s)""",
                (id, fake.name(), fake.text(), fake.random_int(min=1, max=100)),
        )
        db_connection.commit()

if __name__ == "__main__":
    