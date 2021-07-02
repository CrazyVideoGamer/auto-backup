init:
	@echo "Installing python3..."
	sudo apt install python3
	@echo "Installing needed libraries"
	pip install -r requirements.txt -t lib # we do this so the user won't have global libraries installed that they don't want
install:
	cp auto-backup /usr/local/bin/

uninstall:
	rm /usr/local/bin/auto-backup
