all: test

SRCS := $(shell git ls-files *.py)

.PHONY: run
run:
	./main.py

.PHONY: test
test:
	pytest test_*.py

.PHONY: format
format:
	yapf -i $(SRCS)

.PHONY: format-check
format-check:
	yapf --diff $(SRCS) \
		|| (echo "Some files require formatting. Run 'make format' to fix." && exit 1)

.PHONY: clean
clean:
	git clean -Xfd

ifndef VERBOSE
.SILENT:
endif
