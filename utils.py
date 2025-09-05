import pandas as pd
import plotly.express as px
import streamlit as st
import json

with open("tasks.json", "rb") as f:
    TASKS = json.load(f)


def plot_freq_dist(df, col_name, x_axis, y_axis, title=None, order=None):
    df2 = df
    df2["group2"] = df2["group"]
    df2 = df.groupby(["user_id", "group"])["group2"].mean()
    fig = px.histogram(df2, "group2", title=title)
    # fig = px.histogram(df, col_name, title=title)
    # fig.update_traces(y=[y / 6 for y in fig.data[0].y])
    fig.update_layout(bargap=0.2, xaxis_title=x_axis, yaxis_title=y_axis)
    fig.update_xaxes(type="category", categoryarray=order)

    return st.plotly_chart(fig)


def plot_box_plot(df, col_name, x_name, x_axis, y_axis, title=None, order=None):
    fig = px.violin(df, y=col_name, x=x_name, title=title)
    fig.update_layout(bargap=0.2, xaxis_title=x_axis, yaxis_title=y_axis)
    fig.update_xaxes(categoryorder="array", categoryarray=order)

    return st.plotly_chart(fig)


def convertMillis(millis):
    seconds = int(millis / 1000) % 60
    minutes = int(millis / (1000 * 60)) % 60
    hours = int(millis / (1000 * 60 * 60)) % 24
    return seconds, minutes, hours


def process_raw_df(df):

    df["time_taken_ms"] = df["stop_time"] - df["start_time"]
    df["time_taken_s"] = df["time_taken_ms"] / 1000
    df["time_taken_mins"] = df["time_taken_ms"] / 60000
    df["duration_min"] = (df["time_taken_ms"] // 60000).astype(int)
    df["duration_sec"] = ((df["time_taken_ms"] % 60000) // 1000).astype(int)
    df["duration_str"] = df.apply(
        lambda x: f"{x.duration_min}:{x.duration_sec:02d}", axis=1
    )
    df["num_google_urls_1"] = df["SERP_length"]
    df["fraction_google_urls_1"] = df["num_google_urls_1"] / df["num_URLs"]

    df["lastUpdated"] = (
        pd.to_datetime(df["lastUpdated"], format="mixed")
        .dt.tz_convert("Europe/Zurich")
        .dt.tz_localize(None)
    )

    return df


def get_display_df(df):
    # st.text(f"set{df['group']}")
    # df["col3"] = df.apply(lambda row: f"{row['col1']}_{row['col2']}", axis=1)

    # st.text(df.columns)

    # df["task_prompt"] = df.apply(
    #     lambda row: TASKS[f"set{row['group']}"][row["task_rank"]], axis=1
    # )
    return df[
        [
            "user_id",
            "group",
            # "task_prompt",
            "task_rank",
            "answer",
            "SERP_length",
            "og_task_id",
            "num_clicks",
            "avg_scroll_length",
            "num_URLs",
            "time_taken_s",
            "lastUpdated",
        ]
    ]
