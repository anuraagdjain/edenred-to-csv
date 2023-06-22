from bs4 import BeautifulSoup
from datetime import datetime

def html_file_to_csv(html_content):
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the table containing the transaction data
    table = soup.find("table")

    # Create a list to store the extracted data
    data = []
    skipped_rows = []
    if table:
        # Find all table rows
        rows = table.find_all("tr")

        for row in rows:
            # Find all table cells
            cells = row.find_all("td")

            if cells:
                # Extract the data from each cell
                raw_date = cells[0].text.strip()
                raw_time = cells[1].text.strip()
                description = cells[2].text.strip()
                type = cells[3].text.strip()
                status = cells[4].text.strip()
                amount = cells[5].text.strip()

                # Convert the raw date to "YYYY-MM-DD" format
                current_year = datetime.now().year

                # Convert the raw time to "YYYY-MM-DD" format
                formatted_time = (
                    datetime.strptime(raw_time, "%d %b, %H:%M")
                    .replace(year=current_year)
                    .strftime("%Y-%m-%d")
                )

                if (
                    not (description == "Balance load" and type == "Lounari")
                    and "Error" not in status
                ):
                    data.append([formatted_time, description, type, status, amount])
                else:
                    skipped_rows.append(
                        [formatted_time, description, type, status, amount]
                    )

    return (data, skipped_rows)
