:

CROSS   := zip-
CC      := $(CROSS)gcc
OBJDUMP := $(CROSS)objdump
OBJDIR  := obj-zip
SOURCES := h2.c pushtozipcpu.c clr_sdram.c my_malloc.c lifting.c yuv.c rd_dwt_wr.c pck.c
OBJECTS := $(addprefix $(OBJDIR)/,$(subst .c,.o,$(SOURCES)))
HEADERS := $(wildcard *.h)
# CFLAGS  := -O3 -fdump-tree-all -fdump-rtl-all -Wall -Wextra -nostdlib -fno-builtin
CFLAGS  := -O3 -Wall -Wextra -nostdlib -fno-builtin
# CFLAGS  := -Wall -Wextra -nostdlib -fno-builtin
LDFLAGS := -T xula.ld -Wl,-Map,$(OBJDIR)/h2.map

all: $(OBJDIR)/ h2
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

h2: $(OBJECTS) xula.ld
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

$(OBJDIR)/h2.txt: h2
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
	rm -rf $(OBJDIR)/ h2

-include $(OBJDIR)/depends.txt
