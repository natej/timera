help:
	@echo "make install"
	@echo "make install-dev"
	@echo "make test"

install:
	pip install -r requirements.txt
	pip install .

install-dev:
	pip install -r requirements.txt
	pip install pytest
	pip install -e .

test:
	pytest tests
