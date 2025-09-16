#!/usr/bin/env python3
"""
Main script for the cleaning pipeline.
Demonstrates how to use the MainCleaner to process TMX files.
"""

import sys
import os
import click
from MainCleaner import MainCleaner
from TMXParser import TMXParser

@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option('--data-dir', help='Directory containing TMX files')
def main(files, data_dir):
    """Main function to demonstrate the cleaning pipeline."""
    cleaner = MainCleaner()
    parser = TMXParser()

    files = list(files)

    # If data-dir is provided, add them to the files list
    if data_dir:
        #Only if they are tmx files
        files = files + list(os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".tmx"))

    # Get the absolute path to the data directory
    for file in files:
        loadedPairs = parser.load_tmx_file(file)
        print(f"Loaded {len(loadedPairs)} pairs from {file}")

    english_data = []
    japanese_data = []

    # Clean the data
    for pair in loadedPairs:
        cleaned_data, is_valid = cleaner.clean(pair['source'], pair['target'])
        if is_valid:
            english_data.append(cleaned_data['source'])
            japanese_data.append(cleaned_data['target'])
    
    # Post clean the data
    for post_cleaner in cleaner.post_cleaners:
        english_data, japanese_data = post_cleaner.clean(english_data, japanese_data)

    # Save the data to a file
    with open('english_data.txt', 'w') as f:
        for data in english_data:
            f.write(data + '\n')

    with open('japanese_data.txt', 'w') as f:
        for data in japanese_data:
            f.write(data + '\n')


    # TODO: Post clean the data

if __name__ == "__main__":
    main()
