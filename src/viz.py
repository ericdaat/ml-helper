import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from src.config import SEABORN_PALETTE, SEABORN_THEME
from src.model import Session, Epoch

palette = sns.color_palette(SEABORN_PALETTE)
sns.set(style=SEABORN_THEME)


def plot_training_curves_for_model(model_id):
    # Retrieve data
    session = Session()
    data = session\
            .query(Epoch.number,
                   Epoch.training_loss,
                   Epoch.eval_loss,
                   Epoch.training_acc,
                   Epoch.eval_acc)\
            .filter_by(model_id=model_id)\
            .all()
    data = pd.DataFrame(data)

    # Init figure
    fig = plt.figure(figsize=(8, 8))

    # Loss
    ax = sns.lineplot(
        data=data,
        x="number",
        y="training_loss",
        color=palette[0],
    )
    ax = sns.lineplot(
        data=data,
        x="number",
        y="eval_loss",
        color=palette[1],
    )

    # Accuracy
    ax2 = ax.twinx()
    sns.lineplot(
        data=data,
        x="number",
        y="training_acc",
        color=palette[2],
        markers=True,
        ax=ax2
    )
    sns.lineplot(
        data=data,
        x="number",
        y="eval_acc",
        color=palette[3],
        markers=True,
        ax=ax2
    )

    # Customize plot
    fig.legend(
        ("Training Loss", "Eval Loss", "Training Accuracy", "Eval Accuracy"),
        loc="upper center",
        ncol=2,
        bbox_to_anchor=(.5, .94)
    )

    n_epochs = data["number"].max()
    ax.set_xlim(0, data["number"].max())
    ax.set(xticks=list(range(0, n_epochs+1, 5)))

    ax.set_xlabel("Epoch number")
    ax.set_ylabel("Loss")
    ax2.set_ylabel("Accuracy")
    plt.title(
        "Training curves ({model_id})".format(model_id=model_id),
        fontdict=dict(size=15),
        pad=50
    )

    plt.tight_layout()

    return fig
