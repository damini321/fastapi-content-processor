import pandas as pd
from scipy.stats import pearsonr

# Load the dataset
df = pd.read_csv('traffic.csv')

# Print the first few rows and column names to verify
print(df.head())
print(df.columns)

# 1. Total and daily pageview events
pageview_events = df[df['event'] == 'pageview']
total_pageviews = pageview_events.shape[0]
average_pageviews_per_day = pageview_events.groupby('date').size().mean() if not pageview_events.empty else 0
print(f"Total Pageviews: {total_pageviews}")
print(f"Average Pageviews per Day: {average_pageviews_per_day}")

# 2. Total count and distribution of other recorded events
event_types = df['event'].value_counts()
print(f"Event Types Distribution:\n{event_types}")

# 3. Geographical distribution of pageviews
# Since we only have pageviews, use that information
if 'country' in df.columns:
    country_pageviews = pageview_events.groupby('country').size()
    print(f"Pageviews by Country:\n{country_pageviews}")
else:
    print("Column 'country' not found.")

# 4. Click-Through Rate (CTR) analysis
# Assuming CTR should be computed where 'click' events exist
click_events = df[df['event'] == 'click']
if not pageview_events.empty and not click_events.empty:
    # Calculate CTR
    click_count = click_events.shape[0]
    ctr = click_count / total_pageviews if total_pageviews > 0 else float('inf')
    ctr_by_link = click_events.groupby('linkid').size() / pageview_events.groupby('linkid').size() if 'linkid' in df.columns else pd.Series()
    print(f"Overall CTR: {ctr}")
    print(f"CTR by Link:\n{ctr_by_link}")
else:
    print("Insufficient data for CTR analysis.")

# 5. Correlation analysis between clicks and pageviews
# Assuming 'linkid' is used to match clicks with pageviews
if 'linkid' in df.columns:
    linkid_pageviews = pageview_events.groupby('linkid').size()
    linkid_clicks = click_events.groupby('linkid').size()
    common_linkids = linkid_pageviews.index.intersection(linkid_clicks.index)
    if not common_linkids.empty:
        clicks = linkid_clicks.loc[common_linkids]
        pageviews = linkid_pageviews.loc[common_linkids]
        correlation, p_value = pearsonr(clicks, pageviews)
        print(f"Correlation between Clicks and Pageviews: {correlation}")
        print(f"P-value: {p_value}")
    else:
        print("No common link IDs found for correlation analysis.")
else:
    print("Column 'linkid' not found.")
