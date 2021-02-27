using System.Collections.Generic;

namespace SvenskText
{
    /// <summary>
    /// Read in svensk text CSV and JSON files into strongly typed classes.
    /// </summary>
    public static class SvenskText
    {
        /// <summary>
        /// Base URL for the raw GitHub link.
        /// </summary>
        private static string _baseUrl = "https://raw.githubusercontent.com/peterdalle/svensktext/master";

        /// <summary>
        /// Get a list of jobs titles and their gender.
        /// </summary>
        /// <returns>List of <see cref="Job"/>.</returns>
        public static IEnumerable<Job> GetJobs()
        {
            return Read.ReadCsvUrl<Job>(url: _baseUrl + "/yrken/vocations.csv");
        }

        /// <summary>
        /// Get a list of names and their gender.
        /// </summary>
        /// <returns>List of <see cref="Name"/>.</returns>
        public static IEnumerable<Name> GetNames()
        {
            return Read.ReadCsvUrl<Name>(url: _baseUrl + "/namn/namn.csv");
        }

        /// <summary>
        /// Get a list of last names and their frequency.
        /// </summary>
        /// <returns>List of <see cref="LastName"/>.</returns>
        public static IEnumerable<LastName> GetLastNames()
        {
            return Read.ReadCsvUrl<LastName>(url: _baseUrl + "/namn/efternamn.csv");
        }
             
    }
}
