import pickle
import plotly.express as px
import streamlit as st
import pandas as pd

# import get_data as GD

import constants as C
import utils as U

with open("5_sept.pkl", "rb") as f:
    df = pickle.load(f)


import json

with open("tasks.json", "rb") as f:
    TASKS = json.load(f)

df = U.process_raw_df(df)

# clean_df = df[
#     [
#         "user_id",
#         "task_rank",
#         "answer",
#         "lastUpdated",
#         "SERP_length",
#         "og_task_id",
#         "group",
#         "num_clicks",
#         "num_scrolls",
#         "avg_scroll_length",
#         "num_URLs",
#     ]
# ]


with st.sidebar:
    st.subheader("Filters")
    # t_group = st.multiselect("Treatment Group", [1, 2, 3])
    task_id = st.multiselect("Task ID", [1, 2, 3, 4, 5, 6])

    final_study_filter = st.checkbox("Only final study", value=True)
    if final_study_filter:
        this_df = df[df["lastUpdated"] > C.FINAL_STUDY_START_TIME]
    else:
        this_df = df

st.header("How do people search?")
st.subheader("Analysis of the pilot study")

st.text("Dataframe ")
st.dataframe(this_df)

st.text("Tasks")
st.text(f"Set1: {TASKS['set1']}")
st.text(f"Set2: {TASKS['set2']}")
st.text(f"Set3: {TASKS['set3']}")
# st.dataframe(U.get_display_df(this_df))


col1, col2 = st.columns(2)

with col1:
    U.plot_freq_dist(
        this_df,
        col_name="group",
        x_axis="Group Number",
        y_axis="Number of participants",
        title="Distribution of participants by group number",
        order=["1", "2", "3"],
    )

    U.plot_box_plot(
        this_df,
        col_name="num_clicks",
        x_name="group",
        x_axis="Number of clicks per task per participant",
        y_axis="Group",
        title="Click distribution across groups",
        order=["1, 2, 3"],
    )

    U.plot_box_plot(
        this_df,
        col_name="time_taken_s",
        x_name="group",
        x_axis="Time taken per task (in seconds)",
        y_axis="Group",
        title="Time taken per task across groups",
        order=["1, 2, 3"],
    )

    U.plot_box_plot(
        this_df,
        col_name="show_more_clicked",
        x_name="group",
        x_axis="`Show more` clicks per task per participant",
        y_axis="Group",
        title="Did the participant click `show more`?",
        order=["1, 2, 3"],
    )
    # st.dataframe(this_df)
    st.text(f"Mean per group:")
    st.table(this_df.groupby("group")["show_more_clicked"].mean())


with col2:
    U.plot_box_plot(
        this_df,
        col_name="num_scrolls",
        x_name="group",
        x_axis="Number of scrolls per task per participant",
        y_axis="Group",
        title="Scroll distribution across groups",
        order=["1, 2, 3"],
    )

    U.plot_box_plot(
        this_df,
        col_name="num_URLs",
        x_name="group",
        x_axis="Number of URLs per task per participant",
        y_axis="Group",
        title="Number of URLs across groups",
        order=["1, 2, 3"],
    )

    U.plot_box_plot(
        this_df,
        col_name="num_google_urls_1",
        x_name="group",
        x_axis="Number of google URLs per task per participant",
        y_axis="Group",
        title="Number of Google Search URLs",
        order=["1, 2, 3"],
    )

    U.plot_box_plot(
        this_df,
        col_name="fraction_google_urls_1",
        x_name="group",
        x_axis="Fraction of google URLs per task per participant",
        y_axis="Group",
        title="Fraction of Google Search URLs across groups",
        order=["1, 2, 3"],
    )
