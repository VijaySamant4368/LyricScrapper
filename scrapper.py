import requests
from bs4 import BeautifulSoup


main_link = "https://gaana.com"
search_link = "https://gaana.com/search/"


def main():


    start, end = lyricsNumber()
    if start == end == -1:
        return
    
    filename = "lyrics.txt"
    file = open(filename, "a+")
    
    while True:
        
        song, soup =  searchSongPage()
        if song == "\\x":
            print("Exiting application")
            break
        
        first_link = soup.find('a', class_='img default_bg')    #The top result in the search page
        # print(s)
        try:
            song_hyperlink = first_link.get("href") #Hyperlink for the top song
        except AttributeError:  #If there is no result
            print("Song not found, try searching for some other song")
            continue
        
        full_lyrics = extractFullLyrics(song_hyperlink)
        
        printAndSave(full_lyrics, file, start=start, end=end)
        file.flush()    #Saves lyrics after each iteration
        
    file.close()


def printAndSave(lyrics, file, start=0, end=1, display = True)  ->None:
    """Displays the lyrics and saves it into file

    Args:
        lyrics (_type_): The total lyrics in DoM format
        file (_type_): Thye file in which to write
        start (int, optional): First line to include. Defaults to 0.
        end (int, optional): First line to not include. Defaults to 1.
    """
    
    full_cleaned_lyrics:list = lyrics.find_all("p")   #All the lyrics
    cleaned_lyrics:list = full_cleaned_lyrics[start:end]     #All the required lyrics
    for lyric in cleaned_lyrics:
        if lyric.text == "Gaana is your gateway to the best and latest in music, offering over 30 million songs across diverse languages including Hindi, English, Bollywood, and regional tracks. Stream your favourite Hindi songs, Bollywood music, English MP3 songs, radio, podcast and regional music online or download songs to enjoy anytime, anywhere!":
            print("lyrics not found")
        elif lyric.text == "� Entertainment Network India Ltd. 2024, All Rights Reserved":
            print("Song not found")
        else:
            if display:
                print(lyric.text)
            file.write (lyric.text + "\n")
            
def lyricsNumber()  ->  tuple[int, int]:
    """Returns the desired limit of lyrics based on user input

    Returns:
        tuple[int, int]: first line to include, first line to exclude
    """
    
    while True:
        try:
            start = int(input("Enter the first line to add: ")) - 1
            if start < 0:
                print("Enter a postive number for the line")
                continue
            break
        except ValueError:  #Input cannot be changes to int
            print("Not a number, try again")
        except KeyboardInterrupt:
            print("Exiting application")
            return (-1, -1)
            
    while True:
        try:
            end = int(input("Enter the last line to not add: ")) - 1
            if end < start:
                print("Entered line number should be greater than the starting line number")
                continue
            break
        except ValueError:  #Input cannot be changes to int
            print("Not a number, try again")
            continue
        except KeyboardInterrupt:
            print("Exiting application")
            return (-1, -1)
        
    return (start, end)

def searchSongPage()    -> str:
    """Searches for the song in Gaana, and returns the HTML script of the page

    Returns:
        str: The HTML script of the page
    """
    try:
        song = input("Enter song name: ")
    except KeyboardInterrupt:
        print("Exiting application")
        return "\\x", "_"
    if song.lower() == "\\x":
        return "\\x", "_"
    
    # Making a GET request
    r = requests.get(search_link + song)    #The search page for the typed song

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')  #Formats into a pretty HTML type format
    
    return song, soup   #Searched song, HTML of the page

def extractFullLyrics(song_hyperlink: str)   -> str:
    """Extracts the lyrics in the link of Gaana

    Args:
        song_hyperlink (str): The link of the song

    Returns:
        str: The HTML format str of the full lyrics
    """
    song_link = '-'.join(list(song_hyperlink.split()))
    lyrics_link = song_link.replace("/song", "/lyrics") #Changes song link to lyrics link
    # print(main_link + lyrics_link)

    r = requests.get(main_link + lyrics_link)   #Lyrics page for the lyrics link
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')  #HTML formatted str of the Lyrics page

    full_lyrics = soup.find_all('div', class_='_inner')[1]  #All the content in the div class that has lyrics
    return full_lyrics

if __name__ == "__main__":
    main()