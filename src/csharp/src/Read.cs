using CsvHelper;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;

namespace SvenskText
{
    public static class Read
    {
        /// <summary>
        /// Read text file from URL.
        /// </summary>
        /// <param name="url">A URL to a text file.</param>
        /// <returns>
        /// Returns a text string with the file contents.
        /// </returns>
        public static string ReadTextUrl(string url)
        {
            var sr = ReadTextstreamFromUrl(url);
            var results = sr.ReadToEnd();
            sr.Close();
            return results;
        }

        public static StreamReader ReadTextstreamFromUrl(string url)
        {
            WebRequest request = WebRequest.Create(url);
            WebResponse response = request.GetResponse();
            return new StreamReader(response.GetResponseStream(), Encoding.UTF8);
        }

        public static IEnumerable<T> ReadCsvUrl<T>(string url)
        {
            var reader = ReadTextstreamFromUrl(url);
            using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
            {
                return csv.GetRecords<T>().ToList();
            }
        }

        public static IEnumerable<T> ReadCsvFile<T>(string filename)
        {
            var reader = new StreamReader(filename);
            using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
            {
                return csv.GetRecords<T>();
            }
        }
    }
}
