import os

folder = 'letras'

for filename in os.listdir(folder):
    if filename.endswith('.txt') and 'unreleased' in filename.lower():
        file_path = os.path.join(folder, filename)
        os.remove(file_path)