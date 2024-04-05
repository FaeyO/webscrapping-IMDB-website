# Webscraping IMDb Top 250 Movies Using Wayback Machine

This repository contains the code and data for scraping the IMDb website's Top 250 movies using the Wayback Machine. The data collected includes movie title, year, duration, movie link, genre, and rating.

### Process Overview

1. **Scraping IMDb Website**: We used Scrapy to crawl through the IMDb website's archived pages on the Wayback Machine. The spider followed various links to extract data for each movie.

2. **Data Collection**: For each movie, we collected the following information:
   - Movie title
   - Year of release
   - Duration
   - Movie link
   - Genre
   - Rating

3. **Data Saving**: The scraped data were saved in a JSON file for further analysis and processing.

4. **Deployment**: The spider was deployed to the Scrapinghub cloud platform for efficient and scalable scraping.

### Repository Structure

- **`spiders/`**: Contains the Scrapy spider (`movies.py`) used for scraping the IMDb website.
- **`data/`**: Contains the JSON file (`movies_data.json`) where the scraped data is stored.
- **`requirements.txt`**: Lists all Python dependencies required to run the spider.
- **`scrapy.cfg`**: Configuration file for Scrapy settings.

### How to Use

1. Clone this repository to your local machine:

```
git clone https://github.com/FaeyO/webscrapping-IMDB-website.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the Scrapy spider to start scraping:

```
scrapy crawl movies -o movies_data.json
```

4. Once the scraping is complete, the scraped data will be saved in the `movies_data.json` file.

### About

This project was conducted as part of a data collection and analysis effort. The collected data can be used for various purposes such as analyzing trends in popular movies, building recommendation systems, or conducting statistical analysis.

### Disclaimer

This project is for educational and research purposes only. The data collected from the IMDb website is publicly available, and no sensitive or private information was accessed or used during the scraping process.

### Contributors

- [FaeyO](https://github.com/FaeyO)

If you have any questions, suggestions, or concerns, please feel free to open an issue or contact the project contributors.

Thank you for your interest in our project! 🎬📊

### website view

![image](https://github.com/FaeyO/webscrapping-IMDB-website/assets/118575325/e1282133-0b91-43a4-bdc4-7b439ca91258)
