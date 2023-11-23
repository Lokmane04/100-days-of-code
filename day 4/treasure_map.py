row1 = ['⚪','⚪','⚪','⚪','⚪']
row2 = ['⚪','⚪','⚪','⚪','⚪']
row3 = ['⚪','⚪','⚪','⚪','⚪']
row4 = ['⚪','⚪','⚪','⚪','⚪']
row5 = ['⚪','⚪','⚪','⚪','⚪']

print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n")
print("where do you want to place the treasure ? (row,column) : ")
treasure_row = int(input('type in the row number (the number should be between 1 and 3) : '))
treasure_column = int(input('type in the column number (the number should be between 1 and 3): '))
rows = [row1,row2,row3,row4,row5]
rows[treasure_column -1][treasure_row-1] = '⚫'
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n")
