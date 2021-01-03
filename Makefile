SLIDES = scipy2013
SLIDES_HTML = index.html
PLOT_DEPS = parallel_12/speedup_linear_1.svg parallel_12/speedup_linear_2.svg \
            parallel_12/speedup_linear_3.svg
SLIDES_DEPS = $(SLIDES_HTML) $(PLOT_DEPS)
PORT = 8000

REMOTE = origin

notebook:
	jupyter notebook --pylab inline --no-browser

slides: plot
	jupyter nbconvert --to slides $(SLIDES).ipynb
	mv $(SLIDES).slides.html $(SLIDES_HTML)

plot: $(PLOT_DEPS)
	(cd parallel_12; python3 speedup_linear.plot.py)

server: slides
	python3 -m http.server $(PORT)

publish: slides
	git add $(SLIDES_DEPS)
	-git branch -D old/gh-pages
	-git branch -m gh-pages old/gh-pages
	git checkout -b gh-pages
	-git commit -m "Create gh-pages"
	git push -f $(REMOTE) gh-pages
	git checkout master
