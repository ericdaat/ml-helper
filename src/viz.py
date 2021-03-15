import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from src.model import Session, Epoch

palette = sns.color_palette("Paired")
sns.set(style="whitegrid")


def plot_training_curves_for_model(model_id):
    session = Session()

    data = session\
            .query(Epoch.number,
                   Epoch.training_loss,
                   Epoch.training_acc)\
            .filter_by(model_id=model_id)\
            .all()
    data = pd.DataFrame(data)
    fig = plt.figure(figsize=(6, 6))

    # Loss
    ax = sns.lineplot(
        data=data,
        x="number",
        y="training_loss",
        color=palette[0],
    )

    n_epochs = data["number"].max()
    ax.set_xlim(0, data["number"].max())
    ax.set(xticks=list(range(0, n_epochs)))

    # Accuracy
    ax2 = ax.twinx()

    sns.lineplot(
        data=data,
        x="number",
        y="training_acc",
        color=palette[3],
        markers=True,
        ax=ax2)

    fig.legend(
        ("Training Loss", "Training Accuracy"),
        title="Curves",
        loc="upper right",
        ncol=1,
        bbox_to_anchor=(1.3, .87)
    )
    ax.set_xlabel("Epoch number")
    ax.set_ylabel("Loss")
    ax2.set_ylabel("Accuracy")
    plt.title(
        "Training curves ({model_id})".format(model_id=model_id),
        fontdict=dict(size=18)
    )

    return fig
