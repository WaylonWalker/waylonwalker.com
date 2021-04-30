#!bash
cat fonts.css archive-styles.css article.css scroll.css > main.css
cleancss main.css -o main.min.css

myfunc () {
    echo in a function $1
}


myfunc me
