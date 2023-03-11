import datetime


async def calculate_date(all_date):
    hours = 0
    days = 0
    for d in all_date:
        now_date = datetime.datetime.now()
        date = d['date']
        now_time = datetime.datetime.now().strftime("%H")
        user_time = d['date'].strftime("%H")
        date3_days = datetime.datetime.strptime(
            (now_date - datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M"),
            "%Y-%m-%d %H:%M"
        )

        if date > date3_days:
            days += 1
            if now_time == user_time:
                hours += 1
    return days, hours
