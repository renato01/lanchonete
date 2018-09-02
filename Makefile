run:
	python run.py runserver

run_migrate_init:
	python run.py db init

run_migrate:
	python run.py db migrate

run_migrate_upgrade:
	python run.py db upgrade