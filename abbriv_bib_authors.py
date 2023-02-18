import re 
from sys import argv


def abbreviate_name(match_raw):
    names_list = re.split(',| and ', match_raw[0])
    new_names_list = []
    for name,i  in zip(names_list, range(0,len(names_list))):
        if i%2 ==1:
            if '.' in name:
                new_names_list.append(name)
            else:
                name_stripped = name.strip()
                names_caps = re.findall('([A-Z])', name_stripped)
                new_names_list.append(' ' + ''.join([(n + '.') for n in names_caps]))

        else:
            new_names_list.append(name)
   
    return create_author_line(new_names_list)


def create_author_line(slist):
    author_line = ''
    for name, i in zip(slist,range(0,len(slist))):
        if i%2==0 and i != len(slist)-1:
            author_line = author_line + name + ', '
        elif i%2==1 and i != len(slist)-1:
            author_line = author_line + name + ' and '
        else:
            author_line = author_line + name
    return 'author={' + author_line + '}' + ', '


def create_bib(unabbriv_bib, abbriv_bib):

    # unabbriv_bib: file name/location of bib you want to abbreviate
    # abbriv_bib: file name/location of the abbreviated bib

    with open(unabbriv_bib, "r") as f:
       fread=f.read()

    open(abbriv_bib, 'w').close()

    for fline in fread.split('\n'):

        p=re.compile(r'\s*author\s*=\s*\{(.*)\}')
        with open(abbriv_bib, 'a') as file:

            match_raw = p.findall(fline)
            if match_raw != []:
                file.write(abbreviate_name(match_raw) +'\n')
            else:
                file.write(fline + '\n')


create_bib(*argv[1:])
