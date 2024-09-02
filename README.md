# Gaana Lyrics Scraper

A simple Python script to scrape song lyrics from [Gaana.com](https://gaana.com) and save them to a text file. This tool is useful for extracting specific lines of lyrics for use in projects like creating music posters, designing lyric art, or other creative purposes.

## Features

- **Search for Songs:** The script allows you to search for any song on Gaana.com by entering the song name.
- **Extract Specific Lines:** You can specify the starting and ending lines of the lyrics you want to extract.
- **Save Lyrics to File:** The extracted lyrics are saved to a text file (`lyrics.txt`), making it easy to access and use them later.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/VijaySamant4368/gaana-lyrics-scraper.git
    ```
2. Navigate to the project directory:
    ```bash
    cd gaana-lyrics-scraper
    ```
3. Install the required Python libraries:
    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

1. Run the script:
    ```bash
    python gaana_lyrics_scraper.py
    ```
2. Enter the song name when prompted.
3. Specify the starting and ending lines of the lyrics you want to extract.
4. The script will save the extracted lyrics to `lyrics.txt`.

### Example

```bash
Enter song name: Shape of You
Enter the first line to add: 1
Enter the last line to not add: 5
```
## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/VijaySamant4368/LyricScrapper/blob/main/LICENSE.md) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This script is for educational purposes only. Scraping websites may be against their terms of service. Please ensure you have permission to scrape the content you are extracting.
