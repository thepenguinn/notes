creed_push: creed.epub
	adb push creed.epub /sdcard/kindle/home/creed/

creed.epub: creed.md
	pandoc creed.md --epub-title-page=false --css=${HOME}/.config/pandoc/creed.css -o creed.epub

creed.md: creed.norg
	nvim -R -c ":Neorg export to-file creed.md" -c "q!" "creed.norg" > /dev/null

.PHONY: creed_push
