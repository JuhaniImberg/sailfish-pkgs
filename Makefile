SPECS_DIR = SPECS
SOURCES_DIR = SOURCES

RPMBUILD = rpmbuild
RPMBUILD_FLAGS = --define "_topdir `pwd`" -bb

SPECIFY = specify
SPECIFY_FLAGS = -N -n

DL_SOURCES = ./dl-sources

YAMLS = $(wildcard *.yaml)
NAMES = $(YAMLS:.yaml=)
SPEC_NAMES = $(YAMLS:.yaml=.spec)

.PHONY: $(NAMES) clean

clean:
	rm $(SOURCES_DIR)/*

$(NAMES):
	$(SPECIFY) $(SPECIFY_FLAGS) $@.yaml -o $(SPECS_DIR)/$@.spec
	$(DL_SOURCES) $@.yaml
	$(RPMBUILD) $(RPMBUILD_FLAGS) $(SPECS_DIR)/$@.spec
