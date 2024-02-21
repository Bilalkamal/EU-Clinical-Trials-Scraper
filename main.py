# main.py
import argparse
from datetime import datetime, timedelta
from app.eu_scraper import EUClinicalTrialsScraper
from app.utils import setup_logging, write_csv_to_disk
import logging


def parse_args():
    parser = argparse.ArgumentParser(description='EU Clinical Trials Scraper')
    parser.add_argument('--start-date', type=str, required=True,
                        help='Start date in YYYY-MM-DD format')
    parser.add_argument('--end-date', type=str, required=True,
                        help='End date in YYYY-MM-DD format')
    return parser.parse_args()


def validate_dates(start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        if start_date > end_date:
            raise ValueError("Start date cannot be after end date.")
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Date error: {e}")
    return start_date, end_date


def scrape_by_date_range(start_date, end_date):
    scraper = EUClinicalTrialsScraper(start_date, end_date)
    results = scraper.scrape_trials()
    output = {
        "metadata": {
            "query_start_date": start_date.strftime("%Y-%m-%d"),
            "query_end_date": end_date.strftime("%Y-%m-%d"),
            "run_start_datetime": datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        },
        "errors": results["errors"],
        "successes": results["successes"]
    }
    query_details = {
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "run_date": datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    }
    return output, query_details


def main():
    setup_logging()
    args = parse_args()

    start_date, end_date = validate_dates(args.start_date, args.end_date)

    current_date = start_date
    while current_date <= end_date:
        logging.info(f"Scraping data for {current_date}")
        output, query_details = scrape_by_date_range(
            current_date, current_date)
        logging.info(f"Scraping complete for {current_date}")
        write_csv_to_disk(output, query_details)

        current_date += timedelta(days=1)


if __name__ == "__main__":
    main()
