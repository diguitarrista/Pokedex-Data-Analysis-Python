# Pokedex Python

This is an interactive Pokedex created using Python. It allows users to explore information about various Pokemon, including their names, types, abilities, and more. The data for this Pokedex is collected through data wrangling and web scraping techniques from online sources.

## Features

- Search for Pokemon by name or type.
- View detailed information about a specific Pokemon, including its abilities, stats, and more.
- Explore a list of all available Pokemon.
- Visualize Pokemon data using charts and graphs.

## Data Sources

The Pokedex data is collected from the following online sources:

1. [Serebii](https://www.serebii.net/): This source provides comprehensive information about Pokemon, including their abilities, types, and more. The data is obtained through web scraping techniques, and the script used for this purpose can be found in the `webscraper.py` file.

2. [PokeOneGuide](https://pokeoneguide.com/kanto-guides/kanto-pokemon-locations/): This source is used to determine the locations where different Pokemon can be found in the Kanto region. This information is invaluable for trainers looking to catch specific Pokemon.

## Installation

Before running the Pokedex, make sure you have the required libraries installed. You can install them using `pip`:

```bash
pip install pandas requests beautifulsoup4 matplotlib
```

## Usage

1. Clone the repository or download the source code to your local machine.

```bash
git clone https://github.com/your-username/interactive-pokedex.git
```

2. Navigate to the project directory.

```bash
cd interactive-pokedex
```

3. Run the `pokedex.py` script to start the Pokedex.

```bash
python pokedex.py
```

4. Follow the on-screen instructions to explore and search for Pokemon.

## Acknowledgments

This project was made possible thanks to the following libraries and resources:

- [Pandas](https://pandas.pydata.org/): Used for data manipulation and storage.
- [Requests](https://docs.python-requests.org/en/master/): Used for making HTTP requests to fetch data.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Used for web scraping.
- [Matplotlib](https://matplotlib.org/): Used for data visualization.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes. We welcome contributions from the community!

---

Enjoy exploring the world of Pokemon with this interactive Pokedex! If you have any questions or run into any issues, feel free to reach out to the project maintainers.

Happy Pokemon hunting!
