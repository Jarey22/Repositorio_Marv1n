import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="feedbacks",
        user="postgres",
        password="8520."
    )
    print("✅ Conexión exitosa a PostgreSQL")
    conn.close()
except psycopg2.OperationalError as e:
    print("❌ Error operativo al conectar con PostgreSQL:")
    print(repr(e))
except Exception as e:
    print("❌ Otro error al conectar con PostgreSQL:")
    print(repr(e))
