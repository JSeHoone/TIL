from datetime import datetime, timezone, timedelta
kst = timezone(timedelta(hours=9))
train_serial = datetime.now(tz=kst).strftime("%Y%m%d")
print(f'{train_serial[:4]}-{train_serial[4:6]}-{train_serial[6:]}')