venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv;
	. venv/bin/activate && pip install -Ur requirements.txt;

init-db: venv/bin/activate
	. venv/bin/activate && \
	PYTHONPATH="." python ./src/init_db.py;

make tests: venv/bin/activate
	. venv/bin/activate && \
	PYTHONPATH="." pytest tests;

