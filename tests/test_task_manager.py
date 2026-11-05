import json

import pytest

from task_manager import TaskManager


@pytest.fixture
def tasks_file(tmp_path, monkeypatch):
    filename = tmp_path / "tasks.json"
    monkeypatch.setattr(TaskManager, "FILENAME", str(filename))
    return filename


def test_add_task_persists_task_and_assigns_id(tasks_file):
    manager = TaskManager()

    manager.add_task("Buy groceries")

    assert len(manager._tasks) == 1
    assert manager._tasks[0].id == 1
    assert manager._tasks[0].description == "Buy groceries"
    assert manager._tasks[0].completed is False
    assert json.loads(tasks_file.read_text()) == [
        {"id": 1, "description": "Buy groceries", "completed": False}
    ]


def test_complete_task_marks_task_completed_and_persists(tasks_file):
    manager = TaskManager()
    manager.add_task("Finish report")

    manager.complet_task(1)

    assert manager._tasks[0].completed is True
    assert json.loads(tasks_file.read_text())[0]["completed"] is True


def test_delete_task_removes_task_and_persists_remaining_tasks(tasks_file):
    manager = TaskManager()
    manager.add_task("First task")
    manager.add_task("Second task")

    manager.delete_task(1)

    assert [(task.id, task.description) for task in manager._tasks] == [
        (2, "Second task")
    ]
    assert json.loads(tasks_file.read_text()) == [
        {"id": 2, "description": "Second task", "completed": False}
    ]


def test_load_tasks_restores_tasks_and_next_id(tasks_file):
    tasks_file.write_text(
        json.dumps(
            [
                {"id": 3, "description": "Loaded task", "completed": True},
            ]
        )
    )

    manager = TaskManager()
    manager.add_task("New task")

    assert [(task.id, task.description, task.completed) for task in manager._tasks] == [
        (3, "Loaded task", True),
        (4, "New task", False),
    ]
    assert json.loads(tasks_file.read_text())[-1] == {
        "id": 4,
        "description": "New task",
        "completed": False,
    }