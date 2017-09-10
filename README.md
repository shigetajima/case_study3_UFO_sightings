# Unsupervised Learning Case study -- UFO sightings data analysis
We analyzed UFO sighting data from  [The National UFO Reporting Center Online Database](http://www.nuforc.org/webreports.html) . The data (json file) was analyzed to get statistics and insights.
The json file is too large to push it to github.

## EDA
Analyze the report data and investigate the following things.

1. Length of UFO sighting reports
2. UFO sighting statistics. Added a US State population data to investigate which states have most sightings (per 1000 people)
3. Search for most frequent words (Unigram, bigrams, trigrams)
4. Seasonal/geological findings and Sightings over the years

## Insights/results
1. There are total 13,000 records, and description has 23 words on average.
2. UFO sighting statistics are found for each state in the US, and average sightings per 1000 people were calculated. Top 5 sighting states (states with the largest \# of sightings) are CA, FL, WA, TX, NY. Note those are basically the states with large population. On the other hands, the states with the largest \# of average sightings per 1000 people are WA, MT, VT, AK, ME.
3. Unigram: top 3 unigrams are 'sky', 'look', 'object'. Top 4 Bigrams are: 'white light', 'bright light', 'red light', 'look like', 'light move'. The most popular Trigram is 'bright white light', and its frequency is three times more than the most popular trigram (bright red light).
4. Seasonal analysis was performed by analyzing reports in January and July. data (since 2010) for each month/year is analyzed and found that top sightings happened during summer(especially July, August).

## Our team
This case study was done by our team: Shige Tajima, Anusha Mohan, Urmi Mukherjee
