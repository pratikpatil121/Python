#nested list

lang=["CPP","Java","Python",["Go","Rust","Dart"]]

newList=lang.copy()
print(lang)
print(newList)

lang[3][1]="javascript"
print(lang)
print(newList)
