def journal_optimize():
    config_file_path = '/etc/systemd/journald.conf'

    reader = open(config_file_path, 'r')
    lines = reader.readlines()
    reader.close()

    i = 0
    for line in lines:
        if 'SystemMaxUse=' in line:
            lines[i] = 'SystemMaxUse=50M\n'
        i += 1

    writer = open(config_file_path, 'w')
    writer.writelines(lines)
    writer.close()
