using System;
using System.Collections.Generic;
using Xunit;
using SvenskText;
using System.Linq;

namespace Tests
{
    public class Test_SvenskText
    {
        [Fact]
        public void Jobs()
        {
            IEnumerable<Job> jobs = SvenskText.SvenskText.GetJobs();
            var value = (from x in jobs select x).ToList().Take(4).ToList();

            Assert.Equal("abbot", value[3].vocation);
            Assert.Equal(Gender.male, value[3].gender);
        }

        [Fact]
        public void Names()
        {
            IEnumerable<Name> names = SvenskText.SvenskText.GetNames();
            var value = (from x in names select x).ToList().Take(2).ToList();

            Assert.True(names.Count() > 25000);
            Assert.Equal("Aada", value[0].name);
            Assert.Equal(Gender.female, value[0].gender);
            Assert.Equal("Aagot", value[1].name);
            Assert.Equal(Gender.female, value[1].gender);
        }

        [Fact]
        public void LastNames()
        {
            IEnumerable<LastName> lastnames = SvenskText.SvenskText.GetLastNames();
            var value = (from x in lastnames select x).ToList().Take(1).ToList();

            Assert.True(lastnames.Count() >= 100);
            Assert.Equal("Abrahamsson", value[0].lastname);
            Assert.Equal(9814, value[0].frequency);
        }
    }
}
