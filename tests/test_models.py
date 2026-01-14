import os
import sys

# Make project root importable when running pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models import TodoItem, Priority, Status


def test_enums_values():
    assert Priority.HIGH.value == "HIGH"
    assert Priority.MID.value == "MID"
    assert Priority.LOW.value == "LOW"
    assert Status.PENDING.value == "PENDING"
    assert Status.COMPLETED.value == "COMPLETED"


def test_todo_defaults_and_to_dict():
    t = TodoItem(title="Test", details="Detail", owner="alice")
    d = t.to_dict()
    assert d["title"] == "Test"
    assert d["details"] == "Detail"
    assert d["owner"] == "alice"
    assert d["priority"] == Priority.MID.value
    assert d["status"] == Status.PENDING.value
    assert isinstance(d["id"], str) and len(d["id"]) > 0


def test_from_dict_roundtrip():
    data = {
        "id": "1234",
        "title": "T",
        "details": "D",
        "priority": "HIGH",
        "status": "COMPLETED",
        "owner": "bob",
        "created_at": "2020-01-01T00:00:00",
        "updated_at": "2020-01-01T01:00:00",
    }
    t = TodoItem.from_dict(data)
    assert t.id == "1234"
    assert t.title == "T"
    assert t.details == "D"
    assert t.priority == Priority.HIGH
    assert t.status == Status.COMPLETED
    assert t.owner == "bob"
