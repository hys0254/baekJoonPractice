def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report_log = {}
    reportee_log={}
    for id in id_list:
        report_log[id]=set()

    
    for r_case in set(report):
        reporter, reportee = r_case.split()
        report_log[reportee]=report_log.get(reportee,0)+1
        
        
   
    for r_case in set(report):
        reporter, reportee = r_case.split()
        if report_log.get(reportee,0)>=k:
                answer[id_list.idex(reporter)]+=1
        
    return answer