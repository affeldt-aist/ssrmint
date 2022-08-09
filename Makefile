PYTHON = python3

install:
	sudo $(PYTHON) setup.py install

uninstall: clean
	sudo rm -rf /usr/local/bin/pygmentize
	sudo rm -rf /usr/local/lib/python2.7/dist-packages/ssrmint-0.1-py2.7.egg

clean:
	sudo rm -rf ./build
	sudo rm -rf ./dist
	sudo rm -rf ./ssrmint.egg-info
	rm -rf *~ ssrmint/*~

reinstall: uninstall install
