# a simple Makefile

SENDER = termux-share -a send
VIEWER = viewpdf

SECTIONS := $(wildcard section_*/section.tex)

TIKZPICS := $(wildcard */**/tikzpics/*.tex)

build: work.pdf view

force:
	lunatikz build work.tex
	pdflatex -shell-escape -halt-on-error work.tex
	$(VIEWER) work.pdf

work.pdf: work.tex ../preamble.tex ../colorscheme.sty abstract.tex $(SECTIONS) $(TIKZPICS)
	lunatikz build work.tex
	pdflatex -shell-escape -halt-on-error work.tex

view:
	$(VIEWER) work.pdf

send:
	$(SENDER) work.pdf

.PHONY: view build force
