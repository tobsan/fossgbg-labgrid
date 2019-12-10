all:
	pandoc -t beamer slides.md --highlight-style zenburn -o slides.pdf
show: all
	impressive -t WipeRight -T 500 slides.pdf
