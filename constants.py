import datetime
import json
import pandas as pd


USER_COLLECTION_NAME = "participant_data"

TASK_COLLECTION_NAMES = [
    "participant_task_1",
    "participant_task_2",
    "participant_task_3",
    "participant_task_4",
    "participant_task_5",
    "participant_task_6",
]

COLUMN_NAMES = {
    "main": ["createdAt", "group", "thisTaskIndex", "user_id"],
    "task_level": {
        "SERP_htmls": [],
        "clicks": ["element", "text", "timestamp", "x", "y"],
        "scrolls": [
            "bodyScreenHeight",
            "bodyScrollHeight",
            "endBodyY",
            "initBodyY",
            "timestamp",
        ],
        "start_time": 0,
        "stop_time": 0,
        "urls_visited": ["URL", "recordedSERP", "time"],
    },
}


with open("./tasks.json") as f:
    ALL_TASKS = json.load(f)

# FINAL_STUDY_START_TIME = datetime.datetime(
#     year=2025, month=8, day=28, hour=11, minute=45
# )

FINAL_STUDY_START_TIME = pd.Timestamp("2025-08-28 11:45")
