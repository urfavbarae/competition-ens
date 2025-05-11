import time
from datetime import datetime

t = time.time()

print(f"since january it's {t:,.4f} or {t:.2e}")


print(datetime.fromtimestamp(t).strftime("%b %d %Y"))
