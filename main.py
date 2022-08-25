import time
import pandas as pd
from selenium import webdriver

# Web Drivers for Browser
exec_path = r"chromedriver.exe"                                 # change path to your webdriver (chrome or firefox)
driver = webdriver.Chrome(executable_path=exec_path)            # for chrome
# driver = webdriver.Firefox(executable_path = exec_path)       # for firefox
driver.maximize_window()

# importing and conversion to proper string with+
df = pd.read_csv(r"", encoding='latin-1')                     # Provide path to your csv file containing search queries
with_comma_dot_and = df[''].to_list()                         # Specify column name for your data
print(with_comma_dot_and)

# remove comma                # if you have comma in your search query
with_dot_and = []
for i in with_comma_dot_and:
    with_dot_and.append(i.replace(",", ""))
print(with_dot_and)

# replace & with %26 for google search
with_dot = []
for i in with_dot_and:
    with_dot.append(i.replace("&", "%26"))
print(with_dot)

# now further remove dot
converted_string_final = []
for i in with_dot:
    converted_string_final.append(i.replace(".", ""))
print(converted_string_final)


# Function to add + betweet sentence for google search
def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 = str1 + ele + "+"
    return str1


# separate words from string
comma_list = []
for i in converted_string_final:
    comma_list.append(i.split())
print(comma_list)

# add + between words
final_plus_list = []
for i in comma_list:
    final_plus_list.append(list_to_string(i))
print(final_plus_list)

additional_query_at_end = r""           # for adding extra custom query

for i in range(len(final_plus_list)):
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[i + 2])
    entry_url = r"https://www.google.com/search?client=firefox-b-d&q=" + final_plus_list[
        i] + additional_query_at_end
    driver.get(entry_url)
    time.sleep(1.5)
    print(i + 1, entry_url, driver.title)

