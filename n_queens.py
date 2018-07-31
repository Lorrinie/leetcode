
def is_valid(place_dict, row, col, n):
    """
    check if the solution is valid
    :param place_dict: dict, dict storing the location of the queens, place[row] = column
    :param row: int, the number of row of the queen
    :param col: int, the number of column of the queen
    :param n: int. the size of the chessboard
    :return: bool
    """

    # check if the queens are on the same column
    for r in range(row):
        if place_dict[r] == col:
            return False

    # check if the queens are on the main diagonal line
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if place_dict[r] == c:
            return False
        r -= 1
        c -= 1

    # check if the queens are on the accessory diagonal line
    r, c = row - 1, col + 1
    while r >= 0 and c < n:
        if place_dict[r] == c:
            return False
        r -= 1
        c += 1

    return True


def put_queen(result, place_dict, row, n):
    """
    back tracking method of solving N-Queens questions, basic idea is checking if the placement is valid,
    if so, then put the next row, and check if it is valid. if not, then put the queens on the next column.
    when row equals n, means this is a valid solution
    :param result: list, list of the solution of N-Queens
    :param place_dict: dict, dict storing the location of the queens, place[row] = column
    :param row: int, the row to be checked
    :param n: int, the size of the chessboard
    """
    if row == n:        # check if all the queens has been put on the checkboard
        result.append(generate_list(place_dict, n))
        return
    for col in range(0, n):         # put a queen on (row, col)
        place_dict[row] = col
        if is_valid(place_dict, row, col, n):       # check if is a valid solution
            put_queen(result, place_dict, row + 1, n)       # put a queen on the next row
        place_dict[row] = -1        # move queen on this row


def generate_list(place_dict, n):
    """
    generate the list that the question demands
    :param place_dict: place_dict: dict, dict storing the location of the queens, place[row] = column
    :param n: int, the size of the chessboard
    :return: list
    """
    temp_list = []

    for i in range(n):
        row = ["."] * n
        if place_dict[i] >= 0:
            row[place_dict[i]] = "Q"
        temp_list.append("".join(row))

    return temp_list


class Solution:

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        results = []        # list of the solution of N-Queens

        place_dict = {}         # dict storing the location of the queens, place[row] = column

        for i in range(n):
            place_dict[i] = -1      # initialize the dict, the default value is -1

        put_queen(results, place_dict, 0, n)        # looking for the solutions by back tracking method

        return results
        # for re in results:
        #     for r in re:
        #         print(r)
        #     print()

# s = Solution()
# s.solveNQueens(10)

