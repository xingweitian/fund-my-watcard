init:
		@pre-commit install -f


test:
		@pytest


reformat:
		@black src watcard setup.py


check_format:
		@flake8 src watcard setup.py


clean:
		@rm -rf build dist .pytest_cache src/*.egg-info || true
		@echo "The caches and generated files are removed successfully."


package:
		@rm dist/* || true
		@python3 setup.py sdist bdist_wheel
		@echo "Fund-my-watcard is packaged successfully."


upload:
		@twine upload --repository=pypi dist/*


.PHONY: init test reformat check_format clean package upload
