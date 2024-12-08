all:
	python3 bot.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
