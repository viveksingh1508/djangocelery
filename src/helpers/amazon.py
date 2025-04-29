from bs4 import BeautifulSoup


def find_product_table_data(html):
    soup = BeautifulSoup(html, features="html.parser")
    prodduct_data = soup.find("div", id="prodDetails")
    if not prodduct_data:
        return []

    table = prodduct_data.find("table")
    columns = [f"{x.text}".strip() for x in table.find_all("th")]
    table_data = []
    for i, row in enumerate(table.find_all("tr")):
        cells = row.find_all("td")
        row_data = {columns[i]: f"{cell.text}".strip() for cell in cells}
        table_data.append(row_data)
    return table_data


def find_product_rating(html):
    soup = BeautifulSoup(html, features="html.parser")
    product_rating_id = soup.find("span", id="acrPopover")
    rating = product_rating_id.get("title")
    return float(rating.split()[0])


def extract_amazon_product_data(html):
    soup = BeautifulSoup(html, features="html.parser")
    productTitle = soup.find("span", id="productTitle")
    productTitleText = f"{productTitle.text}".strip()
    productPrice = soup.find_all("span", class_="a-price-whole")[0]
    productPrice = f"{productPrice.text}".strip()
    productPriceText = "".join([x for x in productPrice if x.isdigit() or x == "."])
    productPriceNum = float(productPriceText)

    try:
        productDescription = soup.find("div", id="productDescription").text
    except Exception:
        productDescription = ""
    featureBullets = soup.find("div", id="feature-bullets").text

    return {
        "title": productTitleText,
        "price_raw": productPrice,
        "price_text": productPriceText,
        "price": productPriceNum,
        "metadata": find_product_table_data(html),
        "description": productDescription,
        "feature_bullets": featureBullets,
        "ratings": find_product_rating(html),
    }
