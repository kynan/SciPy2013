SLIDES = scipy2013
SLIDES_HTML = index.html
PLOT_DEPS = parallel_12/speedup_linear_1.svg parallel_12/speedup_linear_2.svg \
            parallel_12/speedup_linear_3.svg
SLIDES_DEPS = $(SLIDES_HTML) $(PLOT_DEPS)
PORT = 8000

REMOTE = origin

notebook:
	ipython notebook --pylab inline --no-browser

slides: plot
	nbconvert.py reveal $(SLIDES).ipynb
	mv $(SLIDES).reveal.html $(SLIDES_HTML)

plot: $(PLOT_DEPS)
	(cd parallel_12; python speedup_linear.plot.py)

server: slides
	python -m SimpleHTTPServer $(PORT)

publish: slides
	git add $(SLIDES_DEPS)
	-git branch -D old/gh-pages
	-git branch -m gh-pages old/gh-pages
	git checkout -b gh-pages
	-git commit -m "Create gh-pages"
	git push -f $(REMOTE) gh-pages
	git checkout master
