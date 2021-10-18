def out_ge_p(x, P, name, output_filepath):
    outfile = open(output_filepath, 'w')
    to_write = name
    to_write += "\n\n"
    to_write += "x\n"
    for _x in x:
        to_write += str(_x)
        to_write += "\n"
    to_write += "\n"
    to_write += "P\n"
    for _p in P:
        to_write += str(_p)
        to_write += "\n"
    # print(to_write)
    outfile.write(to_write)
    outfile.close()
