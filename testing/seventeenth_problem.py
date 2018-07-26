import requests
from bs4 import BeautifulSoup
import csv
import re
import ast

def snowfall_data():
    complete_data = requests.get("https://www.currentresults.com/Weather/US/average-snowfall-by-state.php")
    data_html = complete_data.text
    raw_soup = BeautifulSoup(data_html, "lxml")
    table1 = raw_soup.find_all(class_="articletable tablecol-2-left tablecol-3-left smalltext")
    my_string = str(list(table1))
    first = my_string.replace("<caption>","")
    second = first.replace("</caption>","")
    third = second.replace("<thead><tr>","")
    fourth = third.replace("<th>","")
    fifth = fourth.replace("</th>",",")
    sixth = fifth.replace("</tr>","]")
    seventh = sixth.replace("</thead><tbody>","")
    eighth = seventh.replace("<tr>","[")
    ninth = eighth.replace("<td>","")
    tenth = ninth.replace("</td>",",")
    eleventh = re.sub(r'<.+">','',tenth)
    twelfth = eleventh.replace("</a>","")
    thirteenth = twelfth.replace("\n","")
    fourteenth = thirteenth.replace("Average annual snowfall","")
    fift = fourteenth.replace("\xad","")
    sixt = fift.replace("</tbody></table>","")
    seve = sixt.replace("Yearly snowfall averages","")
    eigt = seve.replace(",\t","][")
    nein = eigt.replace(",]","],")
    tien = "[" + nein + "]"
    elien = tien.replace(" ","")
    twel = elien.replace(",]]","]")
    thirt = twel.replace(",Days,State,Place,Inches,Centimetres]","")
    fourt = thirt.replace("\t","")
    print(fourt)
    fift = re.sub(r"(?P<name>[A-Za-z]+)",r'"\g<name>"',fourt)
    print(fift)
    """
    WOW = eval(fift)
    #open_csv = open("FINAL_THANK_GOD.csv","w")
    #open_csv.write(str(WOW))
    #open_csv.close()
    with open("/home/rane/testing/truefinal.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(WOW)
    """
snowfall_data()

def reformatted_snowfall_data():
    import numpy as np
    my_matrix = np.loadtxt(open("/home/rane/Documents/trying_again.csv", "rb"), dtype='str', delimiter=',')
    return my_matrix
reformatted_snowfall_data()
