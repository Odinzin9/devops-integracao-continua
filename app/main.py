from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="DevOps Task API",
    description="API desenvolvida para a atividade prática de DevOps e Integração Contínua.",
    version="1.0.0",
)


class Task(BaseModel):
    title: str
    description: str
    completed: bool = False


tasks = []
next_id = 1


@app.get("/")
def root():
    return {
        "message": "DevOps Task API funcionando!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/tasks")
def list_tasks():
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task: Task):
    global next_id

    new_task = {
        "id": next_id,
        **task.model_dump()
    }

    tasks.append(new_task)
    next_id += 1

    return new_task


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: Task):
    for task in tasks:
        if task["id"] == task_id:
            task.update(task_data.model_dump())
            return task

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {
                "message": "Tarefa removida com sucesso"
            }

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )