
install:
	npm install
	./bin/pip install lxml
	./bin/pip install cssselect

watch:
	grunt watch

build:
	grunt build

bump:
	./bin/python bump-versions.py

release:
	make bump
