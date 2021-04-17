# Code for MA1508 Google PageRank Report

>Adopted from jsphLim/PageRank webcrawler and relation matrix Python script

## Usage:
* Open up the file Web Crawler and pass in the starting web page value in the `init` variable, eg. `init = "abc.com"`.
* Run the Web Crawler script the urls are saved in the `urls.txt` file.
* Run the Matrix generation script to obtain the relationship list in the `connection.txt` file in the form of:
  >in = [...];
  out = [...];
  urls = [...];
* Open up the `PageRankVis.m` file in matlab and replace the in, out and urls field at the top with what provided in the `connection.txt` file.
* Remember to replace the urls [ ] brackets with these { } or else the code wont work.