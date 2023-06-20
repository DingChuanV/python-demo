board = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# 邻居数组为给定的单元格找到8个相邻的单元格
neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1),
             (1, 1)]

rows = len(board)
cols = len(board[0])

# 创建一个原始版的副本
copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

# print(copy_board)
# 逐个单元地迭代
for row in range(rows):
  for col in range(cols):
    # 对于每个单元计算邻居的数量
    live_neighbors = 0
    for neighbor in neighbors:
      r = (row + neighbor[0])
      c = (col + neighbor[1])

      # 检查相邻细胞的有效性，以及它是否原来是一个活细胞
      # 评估是针对副本进行的，因为它永远不会更新
      if (rows > r >= 0) and (cols > c >= 0) and (copy_board[r][c] == 1):
        live_neighbors += 1
    if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
      board[row][col] = 0
    if copy_board[row][col] == 0 and live_neighbors == 3:
      board[row][col] = 1

print(board)
