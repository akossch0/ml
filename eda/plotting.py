import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


def plot_boxplots_and_outliers(df: pd.DataFrame):
    """
    Plots boxplots for all numeric columns in a DataFrame using Seaborn,
    and draws a red line at the upper threshold for extreme outliers (+3*IQR).

    Parameters:
    - df (pd.DataFrame): The DataFrame to analyze.
    """
    numeric_cols = df.select_dtypes(include="number").columns

    n_cols = 2
    n_rows = (len(numeric_cols) + 1) // n_cols

    plt.figure(figsize=(n_cols * 6, n_rows * 4))

    for idx, col in enumerate(numeric_cols, 1):
        plt.subplot(n_rows, n_cols, idx)
        sns.boxplot(x=df[col], color="lightblue", notch=True)

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        upper_threshold = Q3 + 3 * IQR

        plt.axvline(x=upper_threshold, color="red", linestyle="--", linewidth=1.5)
        plt.text(
            upper_threshold,
            0,
            "3*IQR",
            color="red",
            ha="right",
            verticalalignment="bottom",
        )

        plt.title(f"Boxplot of {col}")
        plt.xlabel(col)

    plt.tight_layout()
    plt.show()


def plot_numeric_distributions(df: pd.DataFrame, only_columns=None):
    """
    Plots histograms (distributions) for all numeric columns in a DataFrame using Seaborn.

    Parameters:
    - df (pd.DataFrame): The DataFrame to analyze.
    """
    numeric_cols = df.select_dtypes(include="number").columns

    if only_columns:
        numeric_cols = [col for col in numeric_cols if col in only_columns]

    n_cols = 2
    n_rows = (len(numeric_cols) + 1) // n_cols

    plt.figure(figsize=(n_cols * 6, n_rows * 4))

    for idx, col in enumerate(numeric_cols, 1):
        plt.subplot(n_rows, n_cols, idx)
        sns.histplot(
            df[col], bins=20, kde=True, color="skyblue", line_kws={"linewidth": 2}
        )
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()


def plot_value_counts(df, column_name, chart_title="Value Counts", width=5, height=3):
    """
    Plots a bar chart of the value counts for a specific column in a pandas DataFrame using Seaborn
    and displays the count on top of each bar.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - column_name (str): The name of the column to analyze.
    - chart_title (str): The title of the chart.
    """
    value_counts = df[column_name].value_counts()

    plt.figure(figsize=(width, height))
    bars = sns.barplot(
        x=value_counts.index,
        y=value_counts.values,
        hue=value_counts.values,
        dodge=False,
        palette="light:#5A9",
        legend=False,
    )
    plt.title(chart_title)
    plt.xlabel("Values")
    plt.ylabel("Counts")
    plt.xticks(rotation=45)

    for bar in bars.patches:
        bars.annotate(
            format(bar.get_height(), ".0f"),
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            ha="center",
            va="bottom",
            color="black",
            xytext=(0, 8),
            textcoords="offset points",
        )
        bar.set_edgecolor("black")
        bar.set_linewidth(1)
    ymax = value_counts.max()
    plt.ylim(0, ymax + 0.25 * ymax)
    plt.tight_layout()
    plt.show()


def plot_correlation_matrix(df):
    """
    Plots a heatmap of the correlation matrix for all numeric columns in a DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame to analyze.
    """
    # Calculate the correlation matrix
    corr = df.select_dtypes(include="number").corr()

    # Set up the matplotlib figure
    plt.figure(figsize=(10, 6))

    # Draw the heatmap
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        xticklabels=corr.columns,
        yticklabels=corr.columns,
        cbar_kws={"label": "Correlation coefficient"},
    )

    plt.title("Correlation Matrix")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()


def plot_by_year_buckets(df, temporal_column, year_buckets):
    """
    Plots the number of rows grouped by specified year buckets using Seaborn.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - temporal_column (str): The name of the column containing release dates.
    - year_buckets (list of int): List of year bucket sizes.
    """
    for bucket in year_buckets:
        df_copy = df.copy()

        df_copy["year_group"] = (df_copy[temporal_column].dt.year // bucket) * bucket

        count_series = df_copy.groupby("year_group").size()

        plt.figure(figsize=(5, 3))
        bars = sns.barplot(
            x=count_series.index,
            y=count_series.values,
            hue=count_series.index,
            palette="light:#5A9",
            dodge=False,
            legend=False,
        )
        plt.title(f"Number of Rows Grouped by {bucket}-Year Buckets")
        plt.xlabel(f"{bucket}-Year Buckets")
        plt.ylabel("Number of Rows")
        plt.xticks(rotation=45)

        for bar in bars.patches:
            bars.annotate(
                format(int(bar.get_height()), ".0f"),
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                ha="center",
                va="bottom",
                color="black",
                xytext=(0, 8),
                textcoords="offset points",
            )
            bar.set_edgecolor("black")
            bar.set_linewidth(1)

        ymax = count_series.max()
        plt.ylim(0, ymax + 0.2 * ymax)

        plt.tight_layout()
        plt.show()
