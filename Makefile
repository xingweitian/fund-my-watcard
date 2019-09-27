init:
		pre-commit install -f


test:
		pytest


reformat:
		black src watcard setup.py


check_format:
		flake8 src watcard setup.py


clean:
		rm -rf build dist .pytest_cache src/*.egg-info


package:
		rm dist/*
		python3 setup.py sdist bdist_wheel


upload:
		twine upload --repository=pypi dist/*


.PHONY: init test reformat check_format clean package upload
