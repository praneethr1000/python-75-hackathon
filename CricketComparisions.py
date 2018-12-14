def Dhoni(x):
    wk=['Adam Gilchrist',
        'Kumar Sangakkara',
        'Mark Boucher',
        'Brendon Mccullum',
        'Sarafraz Ahmed']

    captians=['Grame Smith',
              'Ricky Pointing',
              'Steve Waugh',
              'Stephen Fleming',
              'Alastair Cook']

    sixers=['Chris Gayle',
            'Ab Devilliers',
            'Rohit Sharma',
            'Shahid Afridi',
            'Brendon McCullum']

    OdiScore=['Sourav Ganguly',
              'Virat Kohli',
              'Shane Watson',
              'Faf Du Plesis',
              'Sachin Tendulkar']

    OdiAverage=['H M Amala',
                'Trott',
                'Joe root',
                'Cooper',
                'Mike Hussey']

    if x==1:
        print(*wk,sep="\n")

    elif x==2:
        print(*captians,sep="\n")

    elif x==3:
        print(*sixers,sep="\n")

    elif x==4:
        print(*OdiScore,sep="\n")

    elif x==5:
        print(*OdiAverage,sep="\n")
        
    else:
        print("Invalid Choice")


print("Enter 1 for similar Wicket Keepers""\n"
      "     2 for similar Captians""\n"
      "     3 for most six hitters""\n"
      "     4 for highest OdiScore""\n"
      "     5 for similar OdiAverages")

y=int(input())
Dhoni(y)

