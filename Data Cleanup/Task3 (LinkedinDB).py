import pandas as pd
import logging
import re

keywords = [
    "Report this post                         Report           ReportBackSubmit",
    "Comments                        Like          Comment                  Share            CopyLinkedInFacebookTwitter       To view or add a comment, sign in"
]

def get_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

def add_strings(new_string):
    strings.append(new_string)

def find_max_occurrence():
    return max(strings, key=strings.count)

def remove_numbers_end(text):
    return re.sub(r'\d*', '', text)

def remove_keywords(text, keywords):
    for keyword in keywords:
        text = text.replace(keyword, '')
    return text

def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for _ in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]

logging.basicConfig(level=logging.WARN, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Use a raw string for the file path to handle backslashes
file_path = r'C:\myprogs\Internship\3.Datacleanup\LinkedinPosts.xlsx'

# Read Excel file into a Pandas DataFrame
df = pd.read_excel(file_path)

# Function to process the text data and find hashtags
def process_text(text):
    Authourname = text.split('on LinkedIn', 1)[0].replace('\n', '').strip()
    count = text.count(Authourname)
    posts = text.split(Authourname)
    
    for post in posts:
        post = post.replace('Skip to main content         LinkedIn                   Discover                       People                       Learning                       Jobs                   Join now                 Sign in                                    ', ' ')
        post = post.replace('Report this post                                   Report                  Report     Back Submit', ' ')
        post = post.replace('\n', '').strip()
        print("-------------------------------------------")
        designation = post.split('ReportBackSubmit', 1)[0].replace('\n', '').strip().replace('Report this post                         Report', ' ')
        add_strings(designation)

        if 'ReportBackSubmit' in post and 'Report this comment' in post:
            post = post.split('ReportBackSubmit', 1)[1].replace('\n', '').strip().split('Report this comment', 1)[0].replace('\n', '').strip()

        toremove = longest_common_substring(designation, post)
        post = post.replace(toremove, '')
        post = remove_keywords(post, keywords)
        post = remove_numbers_end(post)
        hashtags = get_hashtags(post)
        print(hashtags)
        print(post)

    print(Authourname, find_max_occurrence())

strings = []

# Apply the process_text function to the first row of the 'Text' column in the DataFrame
process_text(df['Text'][0])
