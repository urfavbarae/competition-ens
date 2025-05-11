import sys
import time

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()

    for i, elem in enumerate(lst, 1):
        percent = int(i / total * 100)
        bar_length = 50
        filled_length = int(bar_length * i // total)
        bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length - 1)

        elapsed_time = time.time() - start_time
        speed = i / elapsed_time if elapsed_time > 0 else 0
        eta = (total - i) / speed if speed > 0 else 0

        sys.stdout.write(f"\r{percent}%|[{bar}]| {i}/{total} "
                         f"[{time.strftime('%H:%M', time.gmtime(elapsed_time))}"
                         f"<{time.strftime('%H:%M', time.gmtime(eta))}, "
                         f"{speed:.2f}it/s]")
        sys.stdout.flush()
        yield elem

    sys.stdout.write('\n')
