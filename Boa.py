class boa(object):
    def __init__(self, string, tag):#Assuming that this markup language is like xml or html
        self.f = []#First occurences of tag
        self.l = []#Last occurences of tag
        self.ot = tag                            #Opening Tag
        self.otl = len(tag)                      #Length of Opening Tag
        self.otp = tag[0:self.otl-1] + ' '       #Incase the opening tag has parameters
        self.ct = tag[0] + '/' + tag[1:self.otl] #Closign Tag
        self.data = string                       #Object storage of the string
        x = string.count(self.ot)
        y = string.count(self.otp)
        if x == -1:
            x = 0
        elif y == -1:
            y = 0
        self.oto = x + y                         #How many times the opening tag appears
        self.cto = string.count(self.ct)         #How many times the closing tag appears
        self.instances = []                      #Array of dictionaries, where each dictionary is the data collected from each instance of tag

    def parameterAnalysis(self,x,y,z):           #To deal with opening tags containing parameters
        d = {}
        if x != 'none':
            a = x.split(' ')
            b = len(a) - 1
            if b==' ':                           #This if is just incase that a tag being analyzed is like <span id="waht" > instead of <span id="what"> *the empty unecessary space in end
                del a[-1]
            while b != -1:
                c = a[b].split('=')
                c[1] = c[1].strip("'")
                c[1] = c[1].strip('"')
                d[c[0]]=c[1]
                b = b - 1
            e = list(d.keys())
            d['parameters'] = e
        else:
            d['parameters'] = 'none'
        d['content'] = z
        self.instances.append(d)

    def findMarkups(self):
        if self.oto != self.cto: #If there are an uneven distribution of opening and closing tags
            print "There are an uneven number of opening and closing tags in this string!"
            print self.oto
            print self.cto
        else:
            fci = 0
            z = self.data
            while fci != self.oto:
                h = len(z)
                a = z.find(self.ot)
                b = z.find(self.otp)
                #The if-statement determines whether or not the the plain tag or tag with parameters is first
                if a>b and b != -1:
                    v = z[b+self.otl:h]
                    l = v.find('>')
                    v = v[0:l]                #Tag Parameters In $$$="%%%" Format, Spererated By Spaces
                    f = len(v) + self.otl + 2
                    q = b
                else:
                    q = a
                    v = 'none'
                    f = self.otl + 1
                c = z.find(self.ct)
                r = z[q+f-1:c]                #Contains the content between the tags
                z = z[c+self.otl+1:h]         #Shortens string by removing the closing tag analyzed and all data before it!
                self.parameterAnalysis(v,0,r) #Sends all the different Parameter Tags and There Values To Be Indexed   ~ 1 being a temporary input, 1 will be replaced for an instance beign counted.
                fci = fci + 1
                
data = '''<strong>Courses</strong><ul><li><a target="_top" href="/section/default.asp?id=201540%2D44584"><span id="butter" class='toast'>SPRING 2015 INTERNET/INTRANET DES & DEV (WDD121-007-44584 Yaeger)</span></a></li><li><a target="_top" href="/section/default.asp?id=201540%2D43381"><span>SPRING 2015 POLITICAL SCIENCE (PSC121-006-43381 Selegean-Dostal)</span></a></li><li><a target="_top" href="/section/default.asp?id=201540%2D43834"><span>SPRING 2015 PRECALCULUS (MTH135-007-43834 Terakedis)</span></a></li><li><a target="_top" href="/section/default.asp?id=201540%2D40553"><span>SPRING 2015 SCIENCE/ENERGY AND THE ENV (BIO126-006-40553 Kane-Sutton)</span></a></li><li><a target="_top" href="/section/default.asp?id=201540%2D40031"><span>SPRING 2015 TECHNICAL REPORT WRITING (ENG221-001-40031 O'Brien)</span></a></li></ul>'''
x = boa(data, '<span>')
x.findMarkups()
y = x.instances
z = len(y)
print "There are " + str(z) + " instaces of the tag!"
print y[0]['content']
print y[1]['content']
print y[2]['content']
print y[3]['content']
print y[4]['content']
