all: lint set_version install_dependencies build

lint: flake8 pylint

flake8:
	flake8 rpmbuilder/github2spec

pylint:
	pylint rpmbuilder/github2spec

set_version:
	./set_version.sh

install_dependencies:
	python -m pip install --upgrade pip
	pip install wheel twine
	pip install -r rpmbuilder/requirements.txt

build: install_dependencies publish

update_specs:
	docker-compose up -d
	docker exec rpmbuilder_rpmbuilder_1 /usr/local/bin/github2spec

publish:
	python rpmbuilder/setup.py sdist bdist_wheel
	twine check dist/*

build_rpms:
	./build_with_docker.sh
