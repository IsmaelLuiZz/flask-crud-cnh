import sqlite3

class CNHModel:
    def __init__(self, db_path='cnh.db'):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cnh (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    numero TEXT NOT NULL UNIQUE,
                    categoria TEXT NOT NULL,
                    validade TEXT NOT NULL
                )
            ''')
            conn.commit()

    def insert(self, cnh):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO cnh (nome, numero, categoria, validade)
                VALUES (?, ?, ?, ?)
            ''', (cnh['nome'], cnh['numero'], cnh['categoria'], cnh['validade']))
            conn.commit()
            return cursor.lastrowid

    def fetch_all(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM cnh')
            rows = cursor.fetchall()
            return [
                {'id': r[0], 'nome': r[1], 'numero': r[2], 'categoria': r[3], 'validade': r[4]}
                for r in rows
            ]

    def fetch_by_id(self, id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM cnh WHERE id = ?', (id,))
            r = cursor.fetchone()
            if r:
                return {'id': r[0], 'nome': r[1], 'numero': r[2], 'categoria': r[3], 'validade': r[4]}
            return None

    def update(self, id, data):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE cnh SET nome=?, numero=?, categoria=?, validade=? WHERE id=?
            ''', (data['nome'], data['numero'], data['categoria'], data['validade'], id))
            conn.commit()
            return cursor.rowcount > 0

    def delete(self, id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM cnh WHERE id=?', (id,))
            conn.commit()
            return cursor.rowcount > 0
