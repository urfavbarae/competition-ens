import time
from datetime import datetime

t = time.time()

print(f"since january 1, 1970: it's {t:,.4f} or {t:.2e} 9 in scientific notation")


print(datetime.fromtimestamp(t).strftime("%b %d %Y"))
