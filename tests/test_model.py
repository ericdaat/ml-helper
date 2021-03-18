from src.model import Session, Model, Epoch


def test_create_model():
    session = Session()

    model = Model(id="SomeModel")

    session.add(model)
    session.commit()

    retrieved_model = session\
        .query(Model)\
        .filter(Model.id=="SomeModel")\
        .first()
    assert retrieved_model
    assert retrieved_model.id == "SomeModel"


def test_create_epoch():
    session = Session()

    model = Model(id="SomeModelWithEpochs")
    for i in range(1, 3):
        epoch = Epoch(number=i)
        model.epochs.append(epoch)

    session.add(model)
    session.commit()

    retrieved_model = session\
        .query(Model)\
        .filter(Model.id=="SomeModelWithEpochs")\
        .first()
    assert retrieved_model
    assert retrieved_model.id == "SomeModelWithEpochs"
    assert len(retrieved_model.epochs) == 2
