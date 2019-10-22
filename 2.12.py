lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nibh augue, suscipit a, scelerisque sed,
lacinia in, mi. Cras vel lorem. Etiam pellentesque aliquet tellus.
Phasellus pharetra nulla ac diam. Quisque semper
justo at risus. Donec venenatis, turpis vel hendrerit interdum, dui ligula ultricies purus, sed posuere libero dui id
orci. Nam congue, pede vitae dapibus aliquet, elit magna vulputate arcu, vel tempus metus leo non est. Etiam sit amet
lectus quis est congue mollis. Phasellus congue lacus eget neque. Phasellus ornare, ante vitae consectetuer
consequat, purus sapien ultricies dolor, et mollis pede metus eget nisi. Praesent sodales velit quis augue. Cras
suscipit, urna at aliquam rhoncus, urna quam viverra nisi, in interdum massa nibh nec erat. """

lines = lorem.split('\n')
s_first = ''
s_last = ''
for line in lines:
    s_first += line[0]
    s_last += line[-1]

print("Wyraz z pierwszych znakow:", s_first)
print("Wyraz z ostatnich znakow:", s_last)
