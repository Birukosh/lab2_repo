def sredne (a): 
	sr=0 
	for i in range(len(a)): 
		sr=sr+a[i] 
	return(sr/len(a)) 
def minn(a): 
	min = a[0] 
	for i in range(5): 
		if a[i] < min: 
			min = a[i] 
	return min 
a = [1,2,3,6,5] 
print(min(a)) 
print(sredne(a)) 
a='dasha' 
print(a[::-1]) 
ivan={ 
"name":"ivan", 
"age":34, 
"children":[{ 
"name":"vasja", 
"age":12, 
},{ 
"name":"petja", 
"age":10, 
}], 
} 
darja={ 
"name":"darja", 
"age":41, 
"children":[{ 
"name":"kirill", 
"age":21, 
},{ 
"name":"pavel", 
"age":12, 
}], 
} 
emps=[ivan,darja] 
def d(emps): 
	for key in range (len(emps)): 
		k=False 
		mas=emps[key]["children"] 
		for key1 in range (len(mas)): 
			if mas[key1]["age"]>18: 
				k=True 
		if (k==True): 
			print (emps[key]["name"]) 
	return 0 
a=d(emps)
