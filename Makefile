PKGNAME=pyconf

default: test

all: test

clean:
	python setup.py clean --all

test:
	py.test --junitxml=./reports/junit.xml -o junit_suite_name=$(PKGNAME) tests

test-cov:
	py.test --cov ./$(PKGNAME) --cov-report term-missing --cov-report xml:reports/coverage.xml --cov-report html:reports/coverage tests

.PHONY: test test-cov clean
