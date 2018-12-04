def check_valiables(variable_size_threshold = 0,list_dir = dir()):
    """
    input   : none
    output  : variables
              
    example : check_variables(variable_size_threshold = 10000)  
     """
    import sys
    
    print("{}{: >30}{}{: >16}{}".format('|','Variable Name','|','Memory','|'))
    print(" ----------------------------------------------- ")
    
    for var_name in list_dir:
        if not var_name.startswith("_") and sys.getsizeof(eval(var_name)) >= variable_size_threshold:
            print("{}{: >30}{}{: >16,}{}".format('|',var_name,'|',sys.getsizeof(eval(var_name)),'|'))