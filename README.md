![ForSaleByOwner.png](/images/ScrapProprties.png)

<br/>
<p align="center">
  <!-- <a href="https://github.com/mustafahubs/ForSaleByOwner-ScraperTool">
    <img src="images/ScrapProprties.png" alt="Logo" width="640" height="480">
  </a> -->
  <h3 align="center"><a href="https://youtu.be/FuvdO7mSAkE">>>View Demo<<</a></h3>
  <h3 align="center">Python Scraper for Sale Listings on ForSaleByOwner.com</h3>

  <p align="center">
    A Useful Real Estate Property Scraping Tool and Easy Setup
    <br/>
    <br/>
    <a href="https://github.com/mustafahubs/ForSaleByOwner-ScraperTool/issues">Report Bug</a>
    .
    <a href="https://github.com/mustafahubs/ForSaleByOwner-ScraperTool/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/mustafahubs/ForSaleByOwner-ScraperTool/total) ![Contributors](https://img.shields.io/github/contributors/mustafahubs/ForSaleByOwner-ScraperTool?color=dark-green) ![Forks](https://img.shields.io/github/forks/mustafahubs/ForSaleByOwner-ScraperTool?style=social) ![Stargazers](https://img.shields.io/github/stars/mustafahubs/ForSaleByOwner-ScraperTool?style=social) ![Issues](https://img.shields.io/github/issues/mustafahubs/ForSaleByOwner-ScraperTool) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

This project is a Python web scraper designed to extract sale listings data from the ForSaleByOwner website. By utilizing web scraping techniques, the scraper automates the process of gathering valuable information from the website, such as property details, pricing, location, and contact information.

## Built With

The project relies on the following Python libraries:

Requests: for making HTTP requests and retrieving HTML content.

CSV: for handling the data export functionality.

Prettytable: To show text on the terminal in tabular form.

pyinputplus: To get input from the user and validate it.

* [Requests](https://requests.readthedocs.io/en/latest/)
* [PrettyTable](https://pypi.org/project/prettytable/)
* [Pyinputplus](https://pypi.org/project/PyInputPlus/)

## Getting Started

First of all you make sure you have Git and Python Should be installed in your machine.

And both should be accessible globally on your terminal.

### Prerequisites
* Git
* Python
* Pip

### Installation

Open your terminal in any location clone the repository by running and follow the steps below:

1. Clone this repository

```sh
git clone https://github.com/Mustafahubs/ForSaleByOwner-ScraperTool.git
```

2. Change directory

```sh
cd ForSaleByOwner-ScraperTool
```

3. Install required modules

```sh
pip install -r requirements.txt
```

## Usage

To use the scraper, simply execute the Python script ```main.py``` and provide the desired search parameters.

```sh
python main.py
```
The scraper will ask for address key words input. The best way is provide some initial address words as input it will show some suggestions to auto complete the search.

![After-First-Command](/images/usageImage1.png)

Let say if I need properties in `New York` City Then I will type `"New"` inital words.

![After-First-Command](/images/usageImage2.png)

Now select slugs by index number let's select slugs `new-your` by passing index `1`.

![After-First-Command](/images/usageImage3.png)

Now it will ask to delete the previous csv file data if you have already. As you setting it up first time so you will not have any csv just chose `Yes` by passing `a`.

The scraper will then navigate through the ForSaleByOwner website, extracting the relevant data and saving it to a CSV file. The extracted data can be easily accessed and analyzed using various data manipulation tools and techniques.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/mustafahubs/ForSaleByOwner-ScraperTool/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/mustafahubs/ForSaleByOwner-ScraperTool/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

Contributions to this project are welcome! If you have any ideas for improvements or additional features, feel free to fork the repository and submit a pull request. Please make sure to follow the project's coding style and guidelines when contributing. You can

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

* **Mustafa** - *Software Developer* - [Mustafa](https://github.com/mustafahubs/) - *Built ReadMe Template*

## Acknowledgements

* [MustafaHubs](https://github.com/Mustafahubs/)
* [ImgShields](https://shields.io/)
