1,/chart-top250/d
/<\/table>/,$d
/<span.*data-value.*/d
/[0-9][0-9]*,[0-9][0-9]*/s/,//g
/^<a href=.*/s/\(.*\)"\(.*\)?\(.*\)/http:\/\/www.imdb.com\2/p