CREATE_TASK_TABLE = '''
    CREATE TABLE IF NOT EXISTS tasks(
        id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        due_time TIMESTAMPTZ,
        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        title TEXT NOT NULL,
        description TEXT
    )
'''

