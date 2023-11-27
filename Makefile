PY_FILES=main.py src/*.py

all: lint
	./main.py

lint:
	black -l 79 $(PY_FILES)
	flake8 $(PY_FILES)
