#!/usr/bin/env bash

echo -e "Starting setup!\n"
echo -e "Please make sure you have install python3 before the installation"
echo -e "Updating dependencies\n"
python3 -m venv venv
source venv/bin/activate
poetry run playwright install
poetry run playwright install-deps
poetry install
echo -e "Setup complete!\n"
echo -e "Running typing test now..."

python3 test_monkeytype.py