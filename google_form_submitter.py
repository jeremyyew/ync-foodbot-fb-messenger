import requests
import re

entries = [  # Name
    '3 - Testing request with generated dictionary',
    # order items
    '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
    # Phone Number
    '81262111',
    # Special preferences
    'No special preferences']

# get link by pre-filling gform
full_url = "https://docs.google.com/forms/d/e/1FAIpQLSfaz9hJMxb1Xv7-fBVLtMurS4M06c3fRRITGzH9y9TdW9lgeg/viewform?usp=pp_url&entry.447516244=Jeremy+Yew&entry.1256482019=1&entry.263592548=1&entry.249949339=1&entry.310315149=1&entry.1653966568=1&entry.1167887241=1&entry.837529854=1&entry.1993557395=1&entry.130786044=1&entry.1053332884=1&entry.229305687=1&entry.1589583357=1&entry.745345738=1&entry.2032133328=1&entry.1805959984=1&entry.421166555=1&entry.1778596441=1&entry.1776027024=1&entry.1167614153=81262111&entry.1705101566=No+special+prefs"


# generate url and entry_keys
def parse_gform_url(full_url):
    # get url
    url_pattern = re.compile('(https.*?)(?=viewform?)')
    url = re.findall(url_pattern, full_url)[0] + 'formResponse'
    # get list of entry keys
    entry_key_pattern = re.compile('(entry\.[0-9]+)')
    entry_keys = re.findall(entry_key_pattern, full_url)
    return url, entry_keys


def generate_form_data(entry_keys, entries):
    # generate form_data dict with entry_keys and entries
    form_data = {}
    entry_keys_and_entries = zip(entry_keys, entries)
    for entry_key, entry in entry_keys_and_entries:
        form_data[entry_key] = entry
    return form_data


# submit form
def post_form():
    url, entry_keys = parse_gform_url(full_url)
    form_data = generate_form_data(entry_keys, entries)
    r = requests.post(url, data=form_data)
    if r.status_code == requests.codes.ok:
        print 'form submission success'
    else:
        print r.text


url, entry_keys = parse_gform_url(full_url)
form_data = generate_form_data(entry_keys, entries)
post_form()


# How to Replicate:
# Step 1: Go to google form edit page settings, get prefilled link
# Step 2: Copy paste the entry parameter names into a dictionary, as above or as in first answer https://stackoverflow.com/questions/17964429/google-forms-response-with-python. Do not seem to need headers.
# Step 3. Send form.
