from recorder import record_audio

"""
1 Stworzyć folder -> train_voice/data/kuba
2 Ustawić liczbę próbek w record_test_author, od min 20 do max 50
3 Uruchomić ten program
4 W konsoli nastąpi informacja że nagrywanie się zaczyna
5 Powtarzać słowo kluczowe aż program się zakończy
"""

def record_test_author(who):
    #TODO Ustawić liczbę powtórzeń, od 20 do max 50
    for i in range(20):
        print('start recording file '+str(i+1))
        record_audio('train_voice/data/'+who+'_'+str(1000+i+1))
        print('recording file '+str(i+1)+' finished')

def record_test_other():
    for i in range(5):
        print('start recording file '+str(i+1))
        record_audio('train_voice/data/inny_'+str(1000+i+1))
        print('recording file '+str(i+1)+' finished')


record_test_author('kacper')
record_test_other()