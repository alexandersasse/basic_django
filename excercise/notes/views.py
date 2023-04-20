from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import notes

# Create your views here.
 
def home(request):
    title = f"<h2>Welcome to my course notes!</h2>"
    go_to_sections = f"<a href='{reverse('sections')}'>Check the list of sections</a>"
    first_note = f"<a href='{reverse('notes-position', args=[1])}'>Read my first note</a>"
    return HttpResponse(f"{title}{go_to_sections} | {first_note}")

def forwarder(request, id):
    return redirect(reverse('notes-position', args=[id]))

def sections(request):
    ### Retrieve data from models.py
    navigation = ""
    section_list = []
    for data in notes:
        title = data['section']
        if title not in section_list:
            section_list.append(title)
    ### Prepare data for display
    for title in section_list:
        navigation_title = title
        url_title = title.replace(' ','').lower()
        navigation += f"<li><a href='{url_title}'>{navigation_title}</a></li>"
    page_title = f"<h2>Browse my notes by section</h2>"
    home = f"<a href='{reverse('notes')}'>Back to main page</a>"
    ### Putting it together & return
    return HttpResponse(f"{page_title}<ol>{navigation}</ol>{home}")

def slug_query(request, text_passed):
    content = ""
    ### Finding fitting endpoint & generate respective data
    if text_passed == "webframeworks": keyword = "Web Frameworks"
    if text_passed == "settingupdjango": keyword = "Setting up Django"
    if text_passed == "urlmapping": keyword = "URL Mapping"
    ### Building data for display
    title = f"<h2>Notes about: {keyword}</h2>"
    home = f"<a href='{reverse('sections')}'>Back to sections</a>"
    for data in notes:
        if data["section"] == keyword:
            content += f"<li>{data['text']}</li>"
    ### Return
    return HttpResponse(f"{title}<ol>{content}</ol>{home}")
    
def position_query(request, position):
    ### Retrieving data from models.py
    data_from_notes_in_models = notes[position - 1]
    ### Builiding data for display
    title = f"<h2>Note number {position}</h2>"
    secondary_title = f"<h3>{data_from_notes_in_models['section']}</h3>"
    paragraph = f"<p>{data_from_notes_in_models['text']}</p>"
    home =  f"<a href='{reverse('notes')}'>Back to home</a>"
    backwards = f"<a href='{reverse('notes-position', args=[position - 1])}'>Previous note</a>"
    forwards = f"<a href='{reverse('notes-position', args=[position + 1])}'>Next note</a>"
     ### Keep navigation in range
    if position == 1: backwards = "Previous entry"
    if position == len(notes): forwards = "Next entry"
    ### Putting it together and return
    return HttpResponse(f"{title}{secondary_title}{paragraph}{backwards} | {home} | {forwards}")
