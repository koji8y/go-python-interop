all: run

.SUFFIXES: .go .so
.go.so:
	go build -o $@ -buildmode=c-shared $<

build: awesome.so

run: build
	python3 -m client

clean:
	rm awesome.so awesome.h
