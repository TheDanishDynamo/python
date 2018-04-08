print "mad libs"
print "--------"
template = "Hey Ya'll, once upon a time there was a thing with a color nose"
a = ""
qa = { "thing" : "", "color" : "" }
for q in qa:
  qa[q] = raw_input(q + " : ")
print template.replace('thing',qa["thing"]).replace('color',qa["color"])

