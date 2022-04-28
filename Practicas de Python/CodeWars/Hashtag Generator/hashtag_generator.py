def generate_hashtag(s):
    if s == "" or len(s)>140:
        return False
    
    s=s.title()
    print(s)
    s_c = s.split(" ")
    s_c.insert(0,"#")
    x= "".join(s_c)
    return x

#('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')

generate_hashtag('codewars is nice')