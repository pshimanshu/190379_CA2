def out_cd(x, L, name, output_filepath):
    outfile = open(output_filepath, 'w')
    to_write = name
    to_write += "\n\n"
    to_write += "x\n"
    for _x in x:
        to_write += str(_x)
        to_write += "\n"
    to_write += "\n"
    to_write += "L\n"
    for _l in L:
        to_write += str(_l)
        to_write += "\n"
    # print(to_write)
    outfile.write(to_write)
    outfile.close()
