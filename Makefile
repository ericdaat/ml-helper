venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

init-db: venv/bin/activate
	PYTHONPATH="." DATABASE_URL="sqlite:///db.sqlite" python ./src/init_db.py
