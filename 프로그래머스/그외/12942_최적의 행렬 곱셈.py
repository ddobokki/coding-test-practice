def solution(matrix_sizes):
    cnt = 0
    while len(matrix_sizes) != 1:

        oper_nums = []
        for i in range(len(matrix_sizes) - 1):
            oper_num = matrix_sizes[i][1]
            oper_nums.append(oper_num)

        max_oper = max(oper_nums)

        find_idx = oper_nums.index(max_oper)

        cnt += matrix_sizes[find_idx][0] * matrix_sizes[find_idx][1] * matrix_sizes[find_idx+1][1]
        matrix_sizes[find_idx][1] = matrix_sizes[find_idx+1][1]
        matrix_sizes.pop(find_idx)

    return cnt


solution([[5,3],[3,10],[10,6]])