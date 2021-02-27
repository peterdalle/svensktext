# -*- coding: utf-8 -*-
"""
Module for SvenskText that makes it easy to access the content.
"""
import csv


class SvenskText():
    """Get various Swedish dictionaries and lexicons.

    Dictionaries and lexicons
    -------------------------
    - jobs
    - first names
    - last names
    - nationalities
    - organizations
    - sentiment
    - places
    - time periods
    - countries
    - stop words

    Example usage
    --------
    ```python
    jobs = SvenskText.jobs(gender='all')

    for job in jobs:
        print("Job:", job[0])
        print("Gender:", job[1])
        print()
    ```
    """

    @staticmethod
    def jobs(gender='all') -> list:
        """Get list of jobs and their gender.

        Parameters
        ----------
        gender : str
            Whether to get 'all', 'female' or 'male' jobs.

        Returns
        -------
        list
            Returns list of jobs as tuple `(job, gender)`.
        """
        if gender not in ['all', 'female', 'male']:
            raise ValueError(
                       "Parameter 'gender' must be 'all', 'female' or 'male'.")
        filename = '../yrken/vocations.csv'
        if gender == 'all':
            return SvenskText._read_csv_file(filename, skip_lines=1)
        # Return by gender.
        jobs = []
        for job in SvenskText._read_csv_file(filename, skip_lines=1):
            if job[1] == gender:
                jobs.append(job)
        return jobs

    @staticmethod
    def first_names(gender='all') -> list:
        """Get list of first names and their gender.

        Parameters
        ----------
        gender : str
            Whether to get 'all', 'female' or 'male' names.

        Returns
        -------
        list
            Returns list of names as tuple `(name, gender)`.
        """
        if gender not in ['all', 'female', 'male']:
            raise ValueError(
                       "Parameter 'gender' must be 'all', 'female' or 'male'.")
        filename = '../namn/namn.csv'
        if gender == 'all':
            return SvenskText._read_csv_file(filename, skip_lines=1)
        # Return names by gender.
        names = []
        for name in SvenskText._read_csv_file(filename, skip_lines=1):
            if name[1] == gender:
                names.append(name)
        return names

    def last_names(self) -> list:
        return []

    def lemma(self) -> list:
        return []

    def countries(self) -> list:
        return []

    def nationalities(self) -> list:
        return []

    def organizations(self, type=['news', 'government', 'eu']) -> list:
        return []

    def lan(self) -> list:
        return []

    def kommuner(self) -> list:
        return []

    def sentiment(self) -> list:
        return []

    def stop_words(self) -> list:
        return []

    def time_periods(self) -> list:
        return []

    def print_summary():
        """Print a summary of the data."""
        print(f"""SvenskText summary:

Vocations: {len(SvenskText.jobs())}
First names: {len(SvenskText.first_names())}
""")

    @staticmethod
    def _read_csv_file(filename, skip_lines=0) -> list:
        """Read a CSV file and return it as a list with tuples.

        Parameters
        ----------
        filename : str
            CSV filename to read.
        skip_lines : int
            Number of lines to skip at top of file.

        Returns
        -------
        list
            Returns a list for each row as a tuple.
        """
        lines = []
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i > skip_lines - 1:
                    lines.append(row)
        return lines
