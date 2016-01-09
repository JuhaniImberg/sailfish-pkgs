SPECS_DIR = SPECS
SOURCES_DIR = SOURCES

RPMBUILD = rpmbuild
RPMBUILD_FLAGS = --define "_topdir `pwd`" -bb

SPECIFY = specify
SPECIFY_FLAGS = -N -n

DL_SOURCES = ./dl-sources

YAMLS = libmodplug.yaml stow.yaml
NAMES = $(YAMLS:.yaml=)
SPEC_NAMES = $(YAMLS:.yaml=.spec)

.PHONY: $(NAMES) $(YAMLS) clean

clean:
	rm $(SOURCES_DIR)/*

$(YAMLS):
	$(SPECIFY) $(SPECIFY_FLAGS) $@ -o $(SPECS_DIR)/$(@:.yaml=.spec)
	$(DL_SOURCES) $@

$(NAMES):
	$(RPMBUILD) $(RPMBUILD_FLAGS) SPECS/$@.spec
