output = """Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    618      47   311612     350616   1,343.97  14880   1 slack
   2458      67   357752     271808     497.52  17324   1 chrome"""

# Split the output into lines
lines = output.split('\n')

# Extract headers from the first line
headers = lines[0].split()

# Initialize an empty list to store dictionaries
process_list = []

# Iterate over the remaining lines (excluding the header)
for line in lines[2:]:
    values = line.split()
    if len(values) == len(headers):  # Ensure number of values matches headers
        # Create a dictionary where keys are headers and values are corresponding values
        process = {headers[i]: values[i] for i in range(len(headers))}
        process_list.append(process)

# Print the list of dictionaries
for process in process_list:
    print(process)
