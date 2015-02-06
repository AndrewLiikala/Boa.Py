class boa(object):
    def __init__(self, string):#Assuming that this markup language is like xml or html
        #self.f = []#First occurences of tag
        #self.l = []#Last occurences of tag
        #Plan To Include Another Module Version With MultiThreading
        self.data = string                       #Object storage of the string

    def getTagLocations(self,tag):          #Function returns a list that contains all of the locations of the called tag, each index of returned array is a grouping of an opening tag and it's closing tag
        ot = tag                            #Opening Tag
        otl = len(tag)                      #Length of Opening Tag
        otp = tag[0:otl-1] + ' '            #Incase the opening tag has parameters
        ct = tag[0] + '/' + tag[1:otl]      #Closign Tag
        x = self.data
        z = x
        #
        oti = [] #Array for containing each instance of opening tag in document
        cti = [] #Array for containing each instance of closing tag in document
        atl = [] #Master array for containg instances of tag locations in order as they appear
        stpr = 0 #Variable for stoping below loop when it finds every tag
        search = []                    #Array containing the tag variations to look for in the following order...
        search.append(ot)              #Opening tags without parameters
        search.append(otp)             #Opening tags with parameters
        search.append(ct)              #Closing tags with parameters
        si = 0
        while si != 3:                 #Algorithm that finds hte locations of all of the opening and closing tags in the order mentioned above
            z = x
            gv = 0
            stpr = 0
            while stpr != 1:
                a = z.find(search[si])
                if a==-1:
                    stpr = 1
                if si==2:
                    q = otl + 1
                elif si==0:
                    q = otl
                else:
                    qq = z[a:]
                    q = qq.find('>') + 1
                z = z[a+q:]
                coords = []
                coords.append(a + gv)
                coords.append(a+gv+q)
                if si == 2:
                    cti.append(coords)
                else:
                    oti.append(coords)
                gv = gv + a + q
            if si==0 or si==1:       #Note to self, if something bugged with outputted cti or oti, check here!
                del oti[-1]
            else:
                del cti[-1]
            si = si + 1
        #Now oti is an array that contains smaller arrays, the first index of the smaller array is the index where the tag begins, and the second index is where the tag ends
        #Now cti is an array that contains smaller arrays, the first index of the smaller array is the index where the tag begins, and the second index is where the tag ends
        a = len(oti)
        b = len(cti)
        aa = 0
        bb = 0
        while aa<a and bb<b:
            if oti[aa][0]<cti[bb]:
                atl.append(oti[aa])
                aa=aa+1
            else:
                atl.append(cti[bb])
                bb=bb+1
        if aa==a: #If oti is at end
            while bb<b:
                atl.append(cti[bb])
                bb = bb + 1
        else:
            while aa<a:
                atl.append(oti[aa])
                aa = aa + 1
        #Now we also have atl, which is a combined list of oti and cti; in numberical order of course
        sa = [] #array used for stacking algorithm
        gt = [] #Array that houses the master list for grouped tags
        a = len(atl)
        b = 0
        c = 0
        d = 0
        while b!=a: #This algorithm deterimes which tags are grouped together. Decided to have a seperate function later on determine what is nested or not, for dealing with cross-tag nesting in a document
            c = len(sa) - 1
            if atl[b] in oti:
                sa.append(atl[b])
            elif atl[b] in cti:
                tg = []
                tg.append(sa[-1])
                tg.append(atl[b])
                gt.append(tg)
                del sa[-1]
            b=b+1
        return gt  #Format of returned array looks like this [[[],[]],[[],[]]]

    def getAllTags(self):
        x = self.data
        c = x.count('<') + 1
        cc = c
        d = x.count('>') + 1
        e = 0
        g = []
        b = x
        while e!=cc:
            a = b.find('<')
            b = b[a:]
            c = b.find(' ')
            d = b.find('>')
            if d>c:
                f = b[0:c] + '>'
            else:
                f = b[0:d + 1]
            if '/' not in f and f!='':
                if not f in g:
                    g.append(f)
            h = len(f)
            b = b[h:]
            e = e + 1
        return g

    def getAllTagLocations(self):
        a = self.getAllTags()
        b = len(a) - 1
        c = 0
        f = {}
        while c!=b:
            d = self.getTagLocations(a[c])
            f[a[c]]=d
            c = c + 1
        return f

test = '''<li class="expanded"><strong>Courses</strong><ul><li><a target="_top" href="/section/default.asp?id=201540%2D44584"><span>SPRING 2015 INTERNET/INTRANET DES & DEV (WDD121-007-44584 Yaeger)</span></a></li><li><a target="_top" href="/section/default.asp?id=201540%2D43381"><span>SPRING 2015 POLITICAL SCIENCE (PSC121-006-43381 Selegean-Dostal)</span></a></li><li><a target="_top" href="/section/default.asp?id=201540%2D43834"><span>SPRING 2015 PRECALCULUS (MTH135-007-43834 Terakedis)</span></a></li><li><a target="_top" href="/section/default.asp?id=201540%2D40553"><span>SPRING 2015 SCIENCE/ENERGY AND THE ENV (BIO126-006-40553 Kane-Sutton)</span></a></li><li><a target="_top" href="/section/default.asp?id=201540%2D40031"><span>SPRING 2015 TECHNICAL REPORT WRITING (ENG221-001-40031 O'Brien)</span></a></li></ul></li>'''
x = boa(test)
y = x.getAllTagLocations()
z = list(y.keys())
print 'List of keys: ' + str(z)
print 'Tag Locations Found For ' + str(z[0])
c = y[z[0]]
a = len(c)
b = 0
while b!=a:
    print 'openingTagsFound: ' + test[c[b][0][0]:c[b][0][1]]
    print 'closingTagsFound: ' + test[c[b][1][0]:c[b][1][1]]
    b = b + 1




