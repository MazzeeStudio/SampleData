import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import random
import argparse

def generate_rss_feed(num_items, date_condition):
    # Create the root element
    rss = ET.Element("rss", version="2.0")

    # Create the channel element
    channel = ET.SubElement(rss, "channel")

    # Add basic channel info
    ET.SubElement(channel, "title").text = "Sample RSS Feed"
    ET.SubElement(channel, "link").text = "http://www.example.com"
    ET.SubElement(channel, "description").text = "This is a sample RSS feed for testing purposes"
    ET.SubElement(channel, "language").text = "en-us"

    # Helper function to create an item
    def create_item(i, date=None):
        item = ET.SubElement(channel, "item")
        title_variations = ["Text Only", "Text and Photo", "Photo Only", "Longer Text"]
        title = random.choice(title_variations)
        ET.SubElement(item, "title").text = f"Post {i}: {title}"
        ET.SubElement(item, "link").text = f"http://www.example.com/post{i}"
        description_text = ""

        if title == "Text Only":
            description_text = "This is a post that contains only text."
        elif title == "Text and Photo":
            description_text = "<p>This is a post that contains text and a photo.</p>"
            description_text += f'<img src="http://www.example.com/photo{i % 5}.jpg" alt="Example Photo {i}" />'
        elif title == "Photo Only":
            description_text = f'<img src="http://www.example.com/photo{i % 5}.jpg" alt="Example Photo {i}" />'
        elif title == "Longer Text":
            description_text = "This post contains a longer piece of text to showcase varied content length within the feed. It includes multiple sentences to ensure that the RSS feed can handle more extensive content without any issues."

        ET.SubElement(item, "description").text = description_text
        ET.SubElement(item, "guid").text = f"http://www.example.com/post{i}"
        if date:
            ET.SubElement(item, "pubDate").text = date.strftime('%a, %d %b %Y %H:%M:%S GMT')

    # Determine the date logic
    start_date = datetime.utcnow()
    for i in range(1, num_items + 1):
        if date_condition == 'yes':
            date = start_date + timedelta(days=i)
        elif date_condition == 'no':
            date = None
        elif date_condition == 'mixed':
            date = start_date + timedelta(days=i) if i % 3 != 0 else None

        create_item(i, date)

    # Create the XML tree and write to a file
    tree = ET.ElementTree(rss)
    tree.write("sample_rss_feed.xml", encoding="UTF-8", xml_declaration=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a sample RSS feed")
    parser.add_argument("num_items", type=int, help="Number of items to generate")
    parser.add_argument("date_condition", choices=["yes", "no", "mixed"], help="Condition for including dates (yes|no|mixed)")

    args = parser.parse_args()

    generate_rss_feed(args.num_items, args.date_condition)

