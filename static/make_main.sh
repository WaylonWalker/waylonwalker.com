#!bash
cat fonts.css archive-styles.css article.css scroll.css > main.css
cleancss main.css -o main.min.css
cleancss archive-styles.css -o archive-styles.min.css
cleancss scroll.css -o scroll.min.css
cleancss fonts.css -o fonts.min.css

