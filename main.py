"""
1. 将身份证号码17位数分别乘以不同的系数。从第一位到第十七位的系数分别为:7、9、10、5、8、4、2、1、6、3、7、9、10、5、8、4、2 ;
2、将这17位数字和系数相乘的结果相加;
3、用加出来和除以11，看余数是多少;
4、余数只可能有0、1、2、3、4、5、6、7、8、9、10这11个数字。其分别对应的最后一位身份证的号码为1、0、X、9、8、7、6、5、4、3、2，其中的X是罗马数字10;
"""
import calendar


coef_list = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]

rem_dict = {
    0 : '1',
    1 : '0',
    2 : 'X',
    3 : '9',
    4 : '8',
    5 : '7',
    6 : '6',
    7 : '5',
    8 : '4',
    9 : '3',
    10 : '2'}


def sum_mult(clist):
    sums = 0
    for i in clist:
        a,b = i
        sums += int(a) * int(b)
    return sums


def full_id_no(strs):
    id_no_list = []
    for mon in range(1,13):
        month = str(mon).zfill(2)
        for day in range(1,calendar._monthlen(int(strs[6:10]), mon)):
            days = str(day).zfill(2)
            id_no_r = strs[:10] + month + days + strs[-4:-1]
            sum_id_no = sum_mult(list(zip(list(id_no_r[:-1]), coef_list)))
            if rem_dict[sum_id_no%11] == strs[-1]:
                id_no_list.append(id_no_r + strs[-1])

    print(id_no_list)
    print(len(id_no_list))


if __name__ == '__main__':
    full_id_no("3232321976****2393")
