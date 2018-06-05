
# Check 2 conditions using OR logical operator
album_year=1982

if (album_year<1990) or (album_year>1980):
    print("This album was made in 80's")

print("And condition ")

# Check 2 conditions using AND logical operator
album_year=int(input("Enter Album Year : "))

if (album_year<1995) and (album_year>1990):
    print("Album was made in 90's ")


print("New-------")

if (album_year>1995) and (album_year>1990):
    print("Album was not made in 90's ")

elif(album_year<1995) and (album_year>1990):
    print("Album was made in 90's ")



else:
    print("Album was made in", album_year)
