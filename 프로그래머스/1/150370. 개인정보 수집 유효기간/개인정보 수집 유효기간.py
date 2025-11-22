def solution(today, terms, privacies):
    
    t_year, t_month, t_day = map(int, today.split('.'))
    
    term_dict = dict()
    for term in terms:
        key, value = term.split(' ')
        term_dict[key] = int(value)
    
    result = []
    for i, privacy in enumerate(privacies):
        date, term = privacy.split(' ')
        year, month, day = map(int, date.split('.'))
        
        # 유효기간(월)
        validity = term_dict[term]
        
        # 년
        year += (month + validity - 1) // 12
        
        # 월
        month = ((month + validity) - 1) % 12 + 1
        
        if year < t_year:
            result.append(i + 1)
        elif year == t_year and month < t_month:
            result.append(i + 1)
        elif year == t_year and month == t_month and day <= t_day:
            result.append(i + 1)
    
    return result