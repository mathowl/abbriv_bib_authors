# abbriv_bib_authors
Python script for abbreviating first names authors in .bib

You can call it from the command line:

```
python abbriv_bib_authors unabbreviated.bib abbreviated.bib
```

The first names in the author lines of `unabbreviated.bib` will be converted to initials in `abbreviated.bib`. 

It is read line by line so the author lines in the `unabbreviated.bib` cannot be on different lines. If the names in the unabbreviated.bib have already been abbreviated to initials it will not cause any error.


### Example:

````
@article{alagpulinsa2019alginate,
  title={Alginate-microencapsulation of human stem cell--derived $\beta$ cells with CXCL12 prolongs their survival and function in immunocompetent mice without systemic immunosuppression},
  author={Alagpulinsa, David A and Cao, Jenny JL and Driscoll, Riley K and S{\^\i}rbulescu, Ruxandra F and Penson, Madeline FE and Sremac, Marinko and Engquist, Elise N and Brauns, Timothy A and Markmann, James F and Melton, Douglas A and others},
  journal={American Journal of Transplantation},
  volume={19},
  number={7},
  pages={1930--1940},
  year={2019},
  publisher={Elsevier}
}
````
-> abbriv_bib_authors -> 

````
@article{alagpulinsa2019alginate,
  title={Alginate-microencapsulation of human stem cell--derived $\beta$ cells with CXCL12 prolongs their survival and function in immunocompetent mice without systemic immunosuppression},
author={Alagpulinsa,  D.A. and Cao,  J.J.L. and Driscoll,  R.K. and S{\^\i}rbulescu,  R.F. and Penson,  M.F.E. and Sremac,  M. and Engquist,  E.N. and Brauns,  T.A. and Markmann,  J.F. and Melton,  D.A. and others}, 
  journal={American Journal of Transplantation},
  volume={19},
  number={7},
  pages={1930--1940},
  year={2019},
  publisher={Elsevier}
}
````
