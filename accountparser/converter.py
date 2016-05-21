
# Convert input to output file of type 'bank'

def execute(bank, in_path, out_path, prefix):
    in_file = open(in_path, 'r')
    out_file = open(out_path, 'w')
    input = in_file.readlines()
    data_list = bank.parse(input, prefix)
    write(data_list, out_file)
    in_file.close()
    out_file.close()

def write(data_list, out_file):
    output = ['Date,Payee,Category,Memo,Outflow,Inflow\n']
    for data in data_list:
        if data.type == 'credit':
            value = "," + format_value(data)
        else:
            value = format_value(data) + ","
        output += [data.year + "-" + data.month + "-" + data.day + "," + # Date
                   "," +                                                 # Payee (not used)
                   data.prefix + "," +                                   # Category
                   data.memo + "," +                                     # Memo
                   value +                                               # Outflow + Inflow
                   '\n']                                                 # writelines does not add line separators
    out_file.writelines(output)

def format_value(data):
    return data.value
