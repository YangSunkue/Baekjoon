def solution(today, terms, privacies):

    def to_days(date: str) -> int:
        year, month, day = map(int, date.split('.'))
        return (year * 12 * 28) + (month * 28) + day
    
    term_dict = {
        term.split(' ')[0]: int(term.split(' ')[1])
        for term in terms
    }

    today_days = to_days(today)

    result = []
    for i, privacy in enumerate(privacies):
        date, term = privacy.split(' ')

        days = to_days(date)
        expire_days = days + term_dict[term] * 28

        if expire_days <= today_days:
            result.append(i + 1)
    
    return result