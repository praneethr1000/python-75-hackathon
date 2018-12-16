from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

filename="courselist10.csv"
f=open(filename,"w")
for h in range(4475,4480):
    try:
        my_url='https://www.daad.de/deutschland/studienangebote/international-programmes/en/detail/'+str(h)+'/'
        uClient=ureq(my_url)
        page_html=uClient.read()
        uClient.close()

        page_soup=soup(page_html,"html.parser")
        containers=page_soup.find("div",{"class":"c-detail-header__content"})

        z=page_soup.findAll("dt",{"class":"c-description-list__content"})

        course_name=containers.h2.span.string
        x=containers.h3.text.replace("\n","").strip()
        University_name=x.replace("  ","")

        #filename="courselist2.csv"
        #f=open(filename,"w")
        header=["course_name","University_name"]
        for i in range(len(z)):
            t = z[i].text.replace("\n", "").strip().replace(",","")
            header.append(t)

        headers=",".join(header)
        f.write(headers)
        f.write("\n")
        f.write(course_name + "," + University_name + ",")

        y=page_soup.findAll("dd",{"class":"c-description-list__content mb-0"})

        for i in range(len(z)):
            header[i+2]=y[i].text.replace("\n","").strip().replace(",","").replace("\r"," ")
            f.write(header[i+2] + ",")
        f.write("\n")
        #f.close()
    except:
        pass
f.close()