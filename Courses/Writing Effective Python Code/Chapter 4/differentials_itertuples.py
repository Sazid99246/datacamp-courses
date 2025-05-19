run_diffs = []

for row in yankees_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)  # Calculate run_diff here

    run_diffs.append(run_diff)

yankees_df['RD'] = run_diffs
print(yankees_df)