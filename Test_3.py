def get_ts4(items):
    row = []
    row_sec = []
    for i in range(len(items)):
        if i < (len(items) - 1):
            gap = items.iloc[i + 1] - items.iloc[i]
            ts = gap / items.iloc[i]
            row.append(ts)
            for j in range(len(row)):
                gap_2 = row[j + 1] - row [j]
                ts_sec = gap_2 / row[j + 1]
                row_sec.append(ts_sec)
    ts_new = np.mean(row_sec)
    return ts_new