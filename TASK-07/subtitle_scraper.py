import click
import requests
from bs4 import BeautifulSoup
import os
def search_subtitles(filename):
    # Replace with actual Open Subtitles API URL and query parameters
    response = requests.get('https://api.opensubtitles.org/search', params={'filename': filename})
    if response.status_code == 200:
        return response.json()  # Assuming JSON response
    else:
        raise Exception('Failed to retrieve subtitles')
def download_subtitle(subtitle_url, subtitle_path):
    response = requests.get(subtitle_url)
    with open(subtitle_path, 'wb') as file:
        file.write(response.content)
@click.command()
@click.argument('mp4_file', type=click.Path(exists=True))
def main(mp4_file):
    filename = os.path.basename(mp4_file)
    print(f"Searching subtitles for: {filename}")

    try:
        subtitles = search_subtitles(filename)
        if not subtitles:
            print("No subtitles found.")
            return

        print("Available subtitles:")
        for i, subtitle in enumerate(subtitles):
            print(f"{i + 1}: {subtitle['language']} - {subtitle['provider']}")

        choice = click.prompt("Choose a subtitle number", type=int)
        selected_subtitle = subtitles[choice - 1]

        subtitle_url = selected_subtitle['url']
        subtitle_path = f"{filename.rsplit('.', 1)[0]}.{selected_subtitle['language']}.srt"
        print(f"Downloading subtitle to: {subtitle_path}")

        download_subtitle(subtitle_url, subtitle_path)
        print(f"Subtitle downloaded successfully: {subtitle_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
