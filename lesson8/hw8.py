from datetime import date, datetime, timedelta


def main():
    users = [{"name":"Piter", "birthday":"22.05.2021"},
             {"name":"Maria", "birthday":"29.05.2021"},
             {"name":"Tod", "birthday":"26.05.2021"},
             {"name":"Bob", "birthday":"27.05.2021"},
             {"name":"Lilly", "birthday":"28.05.2021"},
             {"name":"Bill", "birthday":"30.05.2021"},
             {"name":"Jack", "birthday":"23.05.2021"},
             {"name":"Anna", "birthday":"25.05.2021"}]

    def congratulate(users):

        m = list()
        t = list()
        w = list()
        th = list()
        f = list()

        dz = datetime.now() + timedelta(days=7)

        for i in users: 
            dx = datetime.strptime(i["birthday"], "%d.%m.%Y")
            dd = dx.weekday()
            wk = dx.isocalendar()[1]
            next_wk = datetime.now().isocalendar()[1]+1

            if dx > datetime.now() and dz > dx:
                
                if datetime.now().isocalendar()[1] == wk or next_wk == wk:
                    
                    if dd == 0:
                        n = i["name"]
                        m.append(n)
                    
                    elif dd == 1:
                        n = i["name"]
                        t.append(n)
                    
                    elif dd == 2:
                        n = i["name"]
                        w.append(n)
                        
                    elif dd == 3:
                        n = i["name"]
                        th.append(n)
                    
                    elif dd == 4:
                        n = i["name"]
                        f.append(n)
                    
                    elif dd == 5:
                        n = i["name"]
                        m.append(n)
                    
                    elif dd == 6:
                        n = i["name"]
                        m.append(n)

        if len(m)>0:
            print("Monday:", *m)
        if len(t)>0:
            print("Tuesday:", *t)
        if len(w)>0:
            print("Wednesday:", *w)
        if len(th)>0:
            print("Thursday:", *th)
        if len(f)>0:
            print("Friday:", *f)
    
    congratulate(users)

if __name__=="__main__":
    main()