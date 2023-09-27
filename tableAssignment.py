from tabulate import tabulate

def create_table(data_context):
    print(tabulate(data_context))

data = [['Meru University'],
        ['---------------------'],
        ['Reg No. BIT001'],
        ['---------------------'],
        ['Unit','Marks','Grade'],
        ['CIT1001',57,'C'],
        ['CIT3002',78,'A'],
        ['Total',135],
        ['Avg',67],
        ['Avg Grade','B']]

create_table(data)