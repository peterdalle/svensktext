namespace SvenskText
{
    /// <summary>
    /// Represents a job title and its gender.
    /// </summary>
    public class Job
    {
        /// <summary>
        /// Title of the job.
        /// </summary>
        public string vocation { get; set; }

        /// <summary>
        /// Gender of the job title.
        /// </summary>
        public Gender gender { get; set; }
    }
}