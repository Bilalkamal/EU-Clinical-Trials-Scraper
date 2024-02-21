# EU Clinical Trials Register Scraper

## Introduction

This project is developed to facilitate the scraping of clinical trial data from the [EU Clinical Trials Register](https://www.clinicaltrialsregister.eu/). It's specifically designed to fetch detailed information about trials within a specified date range. The scraper navigates through the register, extracts data from individual trial records, and compiles the information into structured formats for further analysis or reporting.

## Project Structure

```
.
├── README.md
├── app
│ ├── **init**.py
│ ├── constants.py
│ ├── eu_scraper.py
│ ├── parsers
│ │ ├── **init**.py
│ │ ├── card_parser.py
│ │ ├── protocol_parser.py
│ │ └── result_parser.py
│ └── utils.py
├── data
├── logs
├── main.py
└── requirements.txt

5 directories, 11 files

```

## Setup and Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory and install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

## Usage

To start the scraping process, execute the `main.py` script with the required arguments for start and end dates. The dates should be in the YYYY-MM-DD format.

For example:

```bash
python3 main.py --start-date 2022-12-01 --end-date 2022-12-31
```

Ensure the start and end dates are valid and the start date is before the end date.

## Features

- **Comprehensive Data Extraction**: Targets all key data fields available on the EU Clinical Trials Register.
- **Custom Date Range**: Allows users to specify the period for which the trial data should be fetched.
- **Structured Output**: Organizes scraped data into a coherent structure, facilitating easy access and analysis.
- **Error Handling**: Implements robust error handling to manage and log issues encountered during the scraping process.
- **Efficient Parsing**: Uses specialized parsers to extract and process trial details, protocol information, and results.

## Modules

- `eu_scraper.py`: The main scraper component that orchestrates the retrieval of trial listings and details from the EU Clinical Trials Register.
- `parsers/`: Contains parsers for different sections of the trial data, including trial cards, protocols, and results.
- `utils.py`: Utility functions supporting logging, argument parsing, and output formatting.
- `constants.py`: Configuration file holding constants used across the project, such as base URLs and request headers.

## Output

Outputs from the scraper are stored in the `data` directory. For each run, it generates 3 CSV files containing the extracted data.

## Future Improvements

- **Performance Optimization**: Explore ways to speed up the scraping process, such as using asynchronous requests or coroutines.
- **Additional Search Features**: Allow users to specify additional search criteria, such as fetching only trials with available results.
- **Testing**: Implement comprehensive unit tests to ensure the scraper's functionality and robustness.
