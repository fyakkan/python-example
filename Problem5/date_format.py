from datetime import datetime

def convert_date_format(input_date):
    input_date_object = datetime.strptime(input_date, '%d/%m/%Y')
    output_date = input_date_object.strftime('%Y%m%d')
    return output_date

input_date = "21/02/2023"
output_date = convert_date_format(input_date)
print(output_date)
