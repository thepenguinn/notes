# just a makefile to build epub files

EPUB = ss/signals_and_systems_syllabus.epub \
	   ac/analog_circuits_syllabus.epub

build: $(EPUB)

sync: build
	kdb sync

ac/analog_circuits_syllabus.epub: ac/*.norg
	epubconv --no-sync ac
	cp $@ ${LOCAL_KINDLE_DIR}/home/imstupid/ac

ss/signals_and_systems_syllabus.epub: ss/*.norg
	epubconv --no-sync ss
	cp $@ ${LOCAL_KINDLE_DIR}/home/imstupid/ss

.PHONY: sync build
