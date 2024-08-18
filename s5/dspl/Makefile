# a simple Makefile

run: course.pdf view

course.pdf: course.tex chapter_1/chapter.tex chapter_1/syllabus.tex \
	chapter_2/chapter.tex chapter_2/syllabus.tex
	pdflatex -shell-escape -halt-on-error course.tex

view:
	viewpdf course.pdf

.PHONY: viewn run
