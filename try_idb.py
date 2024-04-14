import idb
from ftfy import fix_encoding
from os import 

with idb.from_file('C:\\Users\\dimap\\Desktop\\MapleDServer\\Angel.idb') as db:
    api = idb.IDAPython(db)
    for ea in api.idautils.Functions():
        address=ea
        sub_rutine_name:str=api.idc.GetFunctionName(ea)
        with open("V83_functions.txt", "w") as file:
            if not sub_rutine_name.startswith("sub"):
                    # Write to the file
                file.write(fix_encoding(f"{address} : {sub_rutine_name}"))
