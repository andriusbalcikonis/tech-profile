PYTHON = python3
ENV = env
PYBIN = $(ENV)/bin
PIP = $(PYBIN)/pip
PIP_COMPILE = $(PYBIN)/pip-compile


.PHONY: default-setup
default-setup: check

.PHONY: help
help:
	@echo "make                       # Prepare (virtualenv, pip compile, pip install, lint) and run tests"
	

$(ENV)/.virtual-env-created:
	# Set up virtualenv
	virtualenv -p $(PYTHON) $(ENV)

	# Install pip-tools, it will help to manage requirements.txt, which will contain all other requirements
	$(PIP) install pip-tools  

	touch $(ENV)/.virtual-env-created

requirements.txt: $(ENV)/.virtual-env-created
	$(PIP_COMPILE) requirements.in -o requirements.txt

$(ENV)/.pip-install-done: $(ENV)/.virtual-env-created requirements.txt
	$(PIP) install -r requirements.txt
	touch $(ENV)/.pip-install-done

.PHONY: check
check: $(ENV)/.pip-install-done
	$(PYBIN)/flake8 queries
