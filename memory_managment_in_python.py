memory managment in python reffers to allocation and deallocation of objects when they are created and when they are deleted.
it manily includes memory allocation, refference count , garbage count.
1.refference count-when an object is created it will have a reffernce count like how many values it reffers to
ex: a=[]
  refference count is 1
  b=a
  Reffernce count is 2
  del a
  now reffernce count =1
  del b refference coutn is 0
2.garbage collection :
when the object refference cycle is created then the memory willl not be freed only by deleting , 
even if we delete ther will be some internal refference
  internal reffernce:a=b
                      b=a
in such case use garbage allocation
3.import gc
  impoetant functions are:
1.gc.collect()
2.gc.enable()
3.gc.diable()
4.gc.get_count()
gc.garbage
