namespace SvenskText
{
    /// <summary>
    /// Represents a last name and its frequency in the population.
    /// </summary>
    public class LastName
    {
        /// <summary>
        /// Last name.
        /// </summary>
        public string lastname { get; set; }

        /// <summary>
        /// Number of people who had the last name in 1994-1997.
        /// </summary>
        public int frequency { get; set; }
    }
}