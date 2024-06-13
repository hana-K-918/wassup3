
contact = {}

while True:
    print('----------전화번호부---------')
    print('1.추가 2.보기 3.검색 4.수정 5.삭제 9.종료')
    menu = int(input('메뉴를 선택해주세요.(숫자only):'))

    if menu == 1:
        print('연락처를 "추가"합니다.')
        new_name = input('이름: ')
        new_tel = input('전화번호: ')
        contact[new_name]=new_tel
        contact.setdefault(new_name, new_tel) #setdefault = 덮어쓰기 금지

    
    elif menu == 2:
        print('연락처를 "조회"합니다.')
        print(contact)
    
        for name, tel in contact.items(): #item = key value 모두 빼올 수 있어
            print (name, ':' , tel)
            
        
    elif menu == 3:
        print('연락처를 "검색"합니다.')
        search_name = input ('이름: ')
        #print(contact[search_name])
        print(contact.get(search_name, '없는 이름입니다.'))
    
    elif menu == 4:
        print('연락처를 "수정"합니다.')
        mod_name = input('수정할 이름: ')

        if mod_name in contact:
            mod_tel = input('새로운 전화번호: ')
            contact[mod_name]=mod_tel
        else:
            print('등록되지 않은 이름입니다.')
        
    elif menu == 5:
        print('연락처를 "삭제"합니다.')
        del_name = input('삭제할 이름: ')

        if del_name in contact:
            del contact[del_name]
        else:
            print('등록되지 않은 이름입니다.')
        
    elif menu == 9:
        print('연락처를 "종료"합니다.')
        break
    
    else:
        print('잘못된 입력입니다')