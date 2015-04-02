export TEXINPUTS:=.:formatting:$(TEXINPUTS)

CROSSTEX := crosstex
CROSSTEX_ARGS := --titlecase lower --add-in --short=author --short=conference

BIBTEX   := bibtex

FIGFIGS :=
EPSFIGS := 
PNGFIGS :=
PDFFIGS :=
SVGFIGS := 
GNUPLOTFIGS :=
FIGS    := $(FIGFIGS) $(EPSFIGS) $(PDFFIGS) $(SVGFIGS) $(GNUPLOTFIGS) \
           $(PNGFIGS)

TEX_SOURCES := project.tex 

.SUFFIXES:

all: 
	pdflatex -shell-escape project
	bibtex project
	pdflatex -shell-escape project
	pdflatex -shell-escape project

pdf: project.pdf

commit: 
	git commit -m "Added stuff" -a
	git push origin master


spell: $(TEX_SOURCES)
	detex $^ | spell | env LANG=C sort -u | env LANG=C comm -23 - ok-words

clean:
	rm -f *~ *.log *.bbl *.dvi project.pdf *.blg *.aux *.ps *.out
