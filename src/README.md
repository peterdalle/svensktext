# Programbibliotek för svensk text

Använd dessa programbibliotek för att snabbt läsa in svensk text i ditt projekt.

Här finns programbibliotek (inklusive unit tests) för:

- [C# .NET Standard 2.0 Class library (strongly typed)](csharp/) 
- [Python](python/)
- [R](r/)

*Notera: dessa är under utveckling.*

## Exempel

### C#

```csharp
using SvenskText;

foreach (Job job in SvenskText.GetJobs()) {
	Console.WriteLine(job.vocation);
	Console.WriteLine(job.gender);
}
```

### Python

```python
import svensktext

for job in SvenskText.get_jobs():
    print(job.Vocation)
    print(job.Gender)
```

### R

```r
library(svensktext)

for (job in svensktext::get_jobs()) {
    cat(job.Vocation, "\n")
    cat(job.Gender, "\n")
}
```