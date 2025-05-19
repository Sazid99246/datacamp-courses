win_perc_preds_loop = []

for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

win_perc_preds_apply = baseball_df.apply(
    lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

win_perc_preds_np = predict_win_perc(
    baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())
