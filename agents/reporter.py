def create_report(
    profile,
    outliers
):

    report = f"""

Rows:
{profile['rows']}

Columns:
{profile['columns']}

Missing:
{profile['missing']}

Duplicates:
{profile['duplicates']}

Outliers:
{outliers}
"""

    return report