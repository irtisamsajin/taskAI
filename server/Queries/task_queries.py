GET_TASKS_BY_ID='''
    SELECT * FROM tasks WHERE id=$1;
'''
GET_TASKS='''
    SELECT * FROM tasks;
'''

CREATE_TASK='''
    INSERT INTO tasks (title,description,due_time)
    VALUES ($1,$2,$3)
    RETURNING *;
'''