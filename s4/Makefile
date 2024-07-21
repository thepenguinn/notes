# just a makefile to build epub files

build: ss/signals_and_systems_syllabus.epub

sync: build
	kdb sync

ss/signals_and_systems_syllabus.epub: ss/*.norg
	epubconv --no-sync ss
	cp ss/signals_and_systems_syllabus.epub ${LOCAL_KINDLE_DIR}/home/imstupid/ss

.PHONY: sync
