def generate(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]

    prev_rows = generate(numRows - 1)
    prev_row = prev_rows[-1]
    current_row = [1]

    for i in range(1, numRows-1):
        current_row.append(prev_row[i-1]+prev_row[i]) # mane prothom ar last is fixed 1 tai loop colve 1 theke numRows-1 

    current_row.append(1) # jehetu last value also fixed 1 tai after loop append 1
    prev_rows.append(current_row) # then put the entire list in our main list

    return prev_rows

print(generate(3))

