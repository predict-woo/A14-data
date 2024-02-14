import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# Update rcParams for all subsequent plots
plt.rcParams['font.family'] = "AppleGothic"

def main():
    # Data
    data = {
        "사망": [62, 41, 5, 1, 6, 9],
        "부상": [1406, 586, 128, 129, 90, 473],
    }
    index = ["계", "횡단중", "차도통행중", "길가장자리 통행중", "보도통행중", "기타"]
    df = pd.DataFrame(data, index=index)
    df = df.drop("계")
    # Set up the matplotlib figure
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Draw the heatmaps
    for col, ax in zip(df.columns, axes):
        sns.heatmap(df[[col]], annot=True, fmt="d", cmap="coolwarm", cbar=True, ax=ax)
        ax.set_title(col)
        ax.set_ylabel('')  # Remove y-axis label
        ax.set_xlabel('')  # Remove x-axis label

        # Remove y-axis ticks for the second heatmap
        if ax != axes[0]:
            ax.set_yticks([])

    # create a new column for the fatality rate
    df['사망률'] = df['사망'] / (df['사망'] + df['부상'])

    # Create another heatmap for the fatality rate
    fig_f, ax_f = plt.subplots(figsize=(12, 6))
    sns.heatmap(df[['사망률']], annot=True, fmt=".2%", cmap="coolwarm", cbar=True, ax=ax_f)
    ax_f.set_title("사망률")
    ax_f.set_ylabel('')  # Remove y-axis label
    ax_f.set_xlabel('')  # Remove x-axis label

    # Display the heatmaps
    st.subheader("원인에 따른 사고 결과 비교")

    tab1, tab2 = st.tabs(["⚖️ 원인에 따른 사망자수와 부상자수 비교", "💀 원인에 따른 사망률 비교"])

    tab1.subheader("원인에 따른 사망자수와 부상자수")
    tab1.pyplot(fig)

    tab2.subheader("원인에 따른 사망률")
    tab2.pyplot(fig_f)

if __name__ == '__main__':
    main()
