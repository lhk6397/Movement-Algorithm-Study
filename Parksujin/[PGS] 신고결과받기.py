# 신고 중복 제거
# reporter : 신고한 유저, 신고당한 유저 / reportee : 신고당한 유저, 신고한유저

def solution(id_list, report, k):
    answer = [] # 결과값

    reporter = {}
    reportee = {}

    for i in report:
        report_user, reported_user = i.split()
        if report_user not in reporter:
            reporter[report_user] = set()
        reporter[report_user].add(reported_user)

        if reported_user not in reportee:
            reportee[reported_user] = set()
        reportee[reported_user].add(report_user)

    answer = [0 for p in range(len(id_list))]

    for r in range(len(id_list)):
        report_user = id_list[r]
        if report_user not in reporter:
            continue

        for reported_user in reporter[report_user]:
            if len(reportee[reported_user]) >= k:
                answer[r] += 1

    return answer