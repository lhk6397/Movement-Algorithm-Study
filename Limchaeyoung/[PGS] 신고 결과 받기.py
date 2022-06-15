import collections

def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    reporter = []
    accused = []

    report_set = set(report)
    report = list(report_set)

    for i in report:
        reporter.append(i.split()[0])
        accused.append(i.split()[1])
    r_counters = collections.Counter(accused)

    for key, value in r_counters.items():
        if value >= k:
            r_list = [idx for idx, value in enumerate(accused) if value == key]
            for i in r_list:
                answer[id_list.index(reporter[i])] += 1
    return answer