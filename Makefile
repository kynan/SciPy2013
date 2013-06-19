SLIDES = scipy2013
SLIDES_HTML = index.html
SLIDES_DEPS = index.html

REMOTE = origin

server:
	ipython notebook --pylab inline --no-browser

slides:
	nbconvert.py reveal $(SLIDES).ipynb
	mv $(SLIDES).reveal.html $(SLIDES_HTML)

publish: slides
	git add $(SLIDES_DEPS)
	-git branch -D old/gh-pages
	-git branch -m gh-pages old/gh-pages
	git checkout -b gh-pages
	-git commit -m "Create gh-pages"
	git push -f $(REMOTE) gh-pages
