# Makefile for chapters

run: chapter.pdf view

chapter.pdf: chapter.tex syllabus.tex
	pdflatex -shell-escape -halt-on-error chapter.tex

view:
	viewpdf chapter.pdf

.PHONY: viewn run
