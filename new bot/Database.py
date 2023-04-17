import sqlite3

def create_table_viloyat():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE regions (
    id INTEGER UNIQUE PRIMARY KEY , 
    name VARCHAR (255)
    )
    """)
    conn.commit()

def create_table_tuman():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE tumans (
    id INTEGER UNIQUE PRIMARY KEY ,
    region_id INTEGER , 
    name VARCHAR (255)
    
    )
    """)
    conn.commit()

def create_table_tugarak():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
     
    cursor.execute(""" 
    CREATE TABLE tugaraks(
    id INTEGER UNiQUE PRIMARY KEY,
    regio_id INTEGER,
    name VARCHAR(255),

    
    )
    """)
    conn.commit()
#create_table_tugarak()


def get_regions():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    cursor.execute("""
    select * from regions
        """)
    data = cursor.fetchall()
    return data


# print(get_regions())
def get_tumans(region_id):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    cursor.execute(f"""
    select * from tumans
    where region_id = {region_id}
        """)
    data = cursor.fetchall()
    return data


def get_tugaraks(tumans_id):
    conn=sqlite3.connect('db.sqlite3')
    cursor=conn.cursor()
    cursor.execute(f""" 
    select * from tugaraks 
    where regio_id ={tumans_id}
    """
    )
    data=cursor.fetchall()
    return data

def get_tugarak(tugarak_id):
    conn=sqlite3.connect('db.sqlite3')
    cursor=conn.cursor()
    cursor.execute(f""" 
    select * from tugaraks 
    where id = {tugarak_id}
    """
    )
    data=cursor.fetchall()
    return data

print(get_tumans(1))








