1,/chart-top250/d
/<\/table>/,$d
/<span.*data-value.*/d
/[0-9][0-9]*,[0-9][0-9]*/s/,//g
/^\(title.*\)/s/\(.*\)>\(.*\)<\(.*\)/\2/p
/<span.*secondaryInfo.*/s/\(.*\)>(\(.*\))<\(.*\)/\2/p
/\s*[0-9]\{1,\}\.$/s/\([^0-9]*\)\([0-9]\{1,\}\)\./\2/p
/<strong/s/\([^0-9]*\)\([0-9]\.[0-9]\)[^0-9]*\([0-9]*\)[^0-9].*>.*/\2\n\3\n/p
/^<a href=.*/s/\(.*\)"\(.*\)?\(.*\)/http:\/\/www.imdb.com\2/p
/img/s/\(.*\)src="\(.*\)" width\(.*\)/\2/p
