VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip


all:
	make run

# Убедитесь, что виртуальное окружение создано
$(VENV_DIR)/bin/activate: 
	python3 -m venv $(VENV_DIR)
	$(PIP) install -r requirements.txt

# Запуск бота с виртуальным окружением
run: $(VENV_DIR)/bin/activate
	$(PYTHON) bot.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
