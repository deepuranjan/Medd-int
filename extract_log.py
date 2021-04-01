def extract_file(log_file):
    err_warn_log_file = "err_warn.log"
    with open(log_file, 'r+') as f:
        logs = f.readlines()
    new_log = ""
    for line in logs:
        if 'ERROR' in line or 'WARNING' in line:
             new_log += line

    with open(err_warn_log_file, 'w+') as f:
        f.write(new_log)


log_file = "sample.log"
if __name__ == '__main__':
    extract_file(log_file)
