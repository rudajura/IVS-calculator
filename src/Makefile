.PHONY: all pack clean test doc run install

all: compile profile

run: calculator.pyc

test: test.pyc

doc: 

profile:

calculator.pyc: calculator.py
	python3 calculator.py
	
test.pyc: tests.py
	python3 tests.py

compile:
	python3 -m py_compile calculator.py

pack: doc packfolder calculator/xkaska02_xcsade00_xstebe03_xjuris02.zip

calculator/xkaska02_xcsade00_xstebe03_xjuris02.zip:
	rm -rf ../../xkaska02_xcsade00_xstebe03_xjuris02/repo/installer
	rm -rf ../../xkaska02_xcsade00_xstebe03_xjuris02/repo/doc
	cd ../.. && zip -r xkaska02_xcsade00_xstebe03_xjuris02

packfolder:
	mkdir -p ../../xkaska02_xcsade00_xstebe03_xjuris02/repo
	mkdir ../../xkaska02_xcsade00_xstebe03_xjuris02/installer
	mkdir ../../xkaska02_xcsade00_xstebe03_xjuris02/doc
	cp -a ../../calculator/. ../../xkaska02_xcsade00_xstebe03_xjuris02/repo/
	cp -a ../doc/. ../../xkaska02_xcsade00_xstebe03_xjuris02/doc/
	cp - ../installer/. ../../xkaska02_xcsade00_xstebe03_xjuris02/installer/

clean:
	rm -rf ../installer/usr ../installer/DEBIAN/ ../../xkaska02_xcsade00_xstebe03_xjuris02
	rm -rf __pycache__

install:
