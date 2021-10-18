import pathlib

folders = {
    1: "ge_wop",
    2: "ge_p", 
    3: "ge_sp",
    4: "lu_ge_wop",
    5: "lu_ge_p",
    6: "lu_cm_wop",
    7: "cd"
}

for folder in folders.values():
    pathlib.Path('./outputs/' + folder).mkdir(parents=True, exist_ok=True) 


def output_path(method, input_filename):
    folder = folders[method]
    output_filepath = "./outputs/" + folder + "/" + "out_" + input_filename
    return output_filepath