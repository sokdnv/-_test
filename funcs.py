import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')


def histplots(df):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    sns.histplot(data=df, x='Количество больничных дней', ax=axes[0])
    axes[0].set_title('Количество больничных дней')

    sns.histplot(data=df, x='Возраст', ax=axes[1])
    axes[1].set_title('Возраст')

    sns.histplot(data=df, x='Пол', ax=axes[2])
    axes[2].set_title('Пол')

    plt.tight_layout()
    return fig
