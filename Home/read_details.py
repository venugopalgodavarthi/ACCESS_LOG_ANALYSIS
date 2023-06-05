from HOME_DETAILS import result
import re


# def fetch_ip_address(coll):
#     res = []
#     for i in coll:
#         print(re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",i))
#     return  res
# #
def fetch_ip_address(coll):
    res = [re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", i)[0] for i in coll]
    return res

def unique_ip_address(coll):
    res = {re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", i)[0] for i in coll}
    return res


def count_ip_address(coll,unique):
    return {i:coll.count(i) for i in unique}

def max_ip_address(coll):
    max = 0
    ip=""
    for i in coll:
        if max<coll[i]:
            max=coll[i]
            ip = i
    return (ip,max)

def min_ip_address(coll):
    min = len(coll)
    ip=""
    for i in coll:
        if min>coll[i]:
            min=coll[i]
            ip = i
    return (ip,min)

def list_ip_address(coll,ele):
    res=[i for i in coll if ele==coll[i]]
    return res

list_ip = lambda coll,ele:[i for i in coll if ele==coll[i]]


if __name__ == '__main__':
    res = fetch_ip_address(result)
    unique = unique_ip_address(result)
    print(res)
    print(unique)
    count_ip = count_ip_address(res,unique)
    print(count_ip)
    max = max_ip_address(count_ip)
    print("maximum used ip address:-->",max[0])
    print("maximum times ip address used:-->", max[1])


    min = min_ip_address(count_ip)
    print("minimum used ip address:-->",min[0])
    print("minimum times ip address used:-->", min[1])

    print(list_ip_address(count_ip,max[-1]))
    print(list_ip_address(count_ip, min[-1]))
    print(list_ip_address(count_ip, 16))

    print(list_ip(count_ip,2))


