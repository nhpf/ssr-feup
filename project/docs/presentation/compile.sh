#!/bin/bash
pandoc presentation.md -t beamer -H custom_template.tex --slide-level 2 -o presentation.pdf

