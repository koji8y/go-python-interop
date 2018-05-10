all: run

.SUFFIXES: .go .so
.go.so:
	go build -o $@ -buildmode=c-shared $<

build: awesome.so

run: build
	python3 -m client

clean:
	rm -f awesome.so awesome.h > /dev/null 2>&1
	rm -rf __pycache__ > /dev/null 2>&1
