VERSION?=latest
MOVIE?=Toy story

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo\$$)" | xargs rm -rf
	rm -rf .pytest_cache

initvenv:
	python3 -m venv .venv
	pip3 install -r requirements/runtime.txt

build:
	$(MAKE) clean && \
	docker build -t imdbapi:$(VERSION) .

run:
	docker run -it \
		-e "IMDB_API_KEY=${IMDB_API_KEY}" \
		-e "IMDB_USER_ID=${IMDB_USER_ID}" \
		imdbapi:$(VERSION) "$(MOVIE)"

test:
	$(MAKE) clean && \
	pytest

inittestenv:
	python3 -m venv .venv
	pip3 install -r requirements/test.txt
