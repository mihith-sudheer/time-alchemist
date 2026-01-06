"""
recommender.py

Loads task data from JSON and returns task recommendations for a given time bucket.

Design principles:
- Pure functions (no Streamlit, no printing)
- Safe defaults
- Easy to extend later (weights, personalization, history)
"""

from __future__ import annotations

import json
import random
from pathlib import Path

DEFAULT_TASKS_PATH = Path("data/tasks_public.json")

def load_tasks(json_path = DEFAULT_TASKS_PATH):
    """
    Load tasks from a JSON file.

    Expected JSON format:
    {
      "tiny": ["task1", "task2", ...],
      "quick": [...],
      ...
    }
    """

    if not json_path.exists():
        raise FileNotFoundError(f"Task file not found: {json_path}")

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # Clean and validate the data
    tasks = {}
    for bucket, items in data.items():
        if isinstance(items, list):
            cleaned_list = []
            for item in items:
                text = str(item).strip()
                if text:
                    cleaned_list.append(text)
            tasks[str(bucket)] = cleaned_list

    return tasks

def recommend_tasks(bucket, tasks, n = 3):
    """
    Return up to n random tasks from the given bucket.

    - If bucket doesn't exist, return empty list
    - If fewer than n tasks exist, return all of them (shuffled)
    - No duplicates
    """
    bucket_tasks = tasks.get(bucket, [])
    if not bucket_tasks:
        return []     
    
    count = min(n, len(bucket_tasks))

    return random.sample(bucket_tasks, count)

