all:

CROSS   := zip-
CC      := $(CROSS)gcc
OBJDUMP := $(CROSS)objdump
OBJDIR  := obj-zip
SOURCES := dwt_steps.c dwt_write.c
OBJECTS := $(addprefix $(OBJDIR)/,$(subst .c,.o,$(SOURCES)))
HEADERS := $(wildcard *.h)
# CFLAGS  := -O3 -fdump-tree-all -fdump-rtl-all -Wall -Wextra -nostdlib -fno-builtin
CFLAGS  := -O3 -Wall -Wextra -nostdlib -fno-builtin
# CFLAGS  := -Wall -Wextra -nostdlib -fno-builtin
LDFLAGS := -T xula.ld -Wl,-Map,$(OBJDIR)/dwt_steps.map

all: $(OBJDIR)/ dwt_steps
$(OBJDIR)/:
	@bash -c "if [ ! -e $(OBJDIR) ]; then mkdir -p $(OBJDIR); fi"

%.o: $(OBJDIR)/%.o
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJDIR)/%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJDIR)/%.txt: $(OBJDIR)/%.o
	$(OBJDUMP) -d $^ -o $@

$(OBJDIR)/%.s: %.c
	$(CC) -S $(CFLAGS) -c $< -o $@

dwt_steps: $(OBJECTS) xula.ld
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

$(OBJDIR)/dwt_steps.txt: dwt_steps
	$(OBJDUMP) -d $^ > $@

define	build-depends
	@echo "Building dependency file(s)"
	@$(CC) $(CPPFLAGS) -MM $(SOURCES) > $(OBJDIR)/xdepends.txt
	@sed -e 's/^.*.o: /$(OBJDIR)\/&/' < $(OBJDIR)/xdepends.txt > $(OBJDIR)/depends.txt
	@rm $(OBJDIR)/xdepends.txt
endef

.PHONY: depends
depends: $(OBJDIR)/ tags
	$(build-depends)

tags: $(SOURCES) $(HEADERS)
	@echo "Generating tags"
	@ctags $(SOURCES) $(HEADERS)

.PHONY: clean
clean:
	rm -rf $(OBJDIR)/ dwt_steps

-include $(OBJDIR)/depends.txt
