#!/usr/bin/env bash

./refresh_puzzles.sh > latest.log 2>&1
echo >> latest.log
source venv/bin/activate
python main.py >> latest.log
deactivate

echo
echo "1. Go to https://www.hankgreen.com/fourbythree/"
echo "2. Open the Javascript Console:"
echo "        Chrome: Windows/Linux: Ctrl+Shift+J, Mac: ⌘+⌥+J"
echo "        Firefox: Windows/Linux: Ctrl+Shift+K, Mac: ⌘+⌥+K"
echo "        Safari: ⌘+⌥+C"
echo "3. Paste the current contents of your clipboard to the Javascript Console"
echo "4. Hit Enter/Return for a perfect score and history in 4x3"
echo