# a simple Makefile

SENDER = termux-share -a send
VIEWER = viewpdf

CHAPTERS := $(wildcard chapter_*/chapter.tex)
SYLLABUS := $(wildcard chapter_*/syllabus.tex)
WORKS := $(wildcard work_*/work.tex)

SECTIONS := $(wildcard chapter_*/section_*/section.tex)
SECTIONS := $(wildcard work_*/section_*/section.tex)

TIKZPICS := $(wildcard */tikzpics/*.tex)

build: course.pdf view

force:
	lunatikz build course.tex
	pdflatex -shell-escape -halt-on-error course.tex
	$(VIEWER) course.pdf

course.pdf: course.tex preamble.tex $(CHAPTERS) $(SYLLABUS) $(SECTIONS) $(WORKS) $(TIKZPICS)
	lunatikz build course.tex
	pdflatex -shell-escape -halt-on-error course.tex

view:
	$(VIEWER) course.pdf

send:
	$(SENDER) course.pdf

.PHONY: view build force
