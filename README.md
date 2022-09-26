# People Also Ask Scraper

This is a simple Python script that based on a query it scrapes Google people also ask questions. 

## Installation

To install and run this script we need to install the requirements.txt and the driver. Since we are using Chrome we need to download the latest chrome driver.

### Requirements

To install requirements.txt please run the following on the terminal.

```bash
pip install requirements.txt
```

## Usage

```python
if __name__ == '__main__':
    questions = get_related_questions('game')
    print(questions)
```

Result:

```python
[{'keyword': 'game', 'title': 'Can I play a game in Google?', 'answer': 'You can play games on all Assistant supported devices. To start a game, you can say: “Hey Google, play a game.” “Hey Google, talk to Are You Feeling Lucky.”', 'source_url': 'https://support.google.com/assistant/answer/9929236?hl=en'}, {'keyword': 'game', 'title': 'Does game still exist?', 'answer': 'Game Retail Limited (doing business as GAME) is a British video game retailer, owned by Frasers Group since June 2019. ... Game (retailer) Trade name GAME Digital Type Subsidiary ISIN GB00BMP36W19 Industry Gaming Founded 1992 (as Rhino Group) 14 more rows', 'source_url': 'https://en.wikipedia.org/wiki/Game_(retailer)'}, {'keyword': 'game', 'title': 'Which game can I play free?', 'answer': 'Here are the top (most popular) free online games to play right now. Mahjongg Dimensions. Mahjongg Dimensions is a 3D take on the popular tile-based game. ... Sudoku is a classic logic puzzle that first appeared in Japan in 1986. ... Spider Solitaire. ... Bubble Shooter.', 'source_url': 'https://www.arkadium.com/free-online-games/'}, {'keyword': 'game', 'title': 'What games can I play for free online?', 'answer': "Editor's Choice Microsoft Jewel. Clusterz! Mahjong Mania. Shumujong™ (digitz mahjong) Linez! Microsoft Ultimate Word Games. Bubble Number. Find Cats. ", 'source_url': 'https://wellgames.com/'}]
```
