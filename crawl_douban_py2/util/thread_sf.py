import threading

class ThreadS (threading.Thread):
  """
  multi-thread class  
  @param thread_id  
  @param func  
  @param *args - func args  
  """
  def __init__(self, thread_id, func, args):
    threading.Thread.__init__(self)
    self.thread_id = thread_id
    self.func = func
    self.args = args

  def run(self):
    """
    open thread  
    """
    threadLock = threading.Lock()
    print (">> open thread %s" % self.thread_id)
    threadLock.acquire()
    self.func(self.args)
    threadLock.release()

def concurrence(func, arr, amount = 10):
  """
  thread concurrence  
  @param func  
  @param arr  
  @param amount  
  """
  counter = 0
  length = len(arr)
  iterater = iter(arr)
  threads = []
  while True:
    try:
      for thread_id in range(amount):
        thread = ThreadS(thread_id + 1, func, next(iterater))
        thread.start()
        threads.append(thread)
      for thread in threads:
        thread.join()
      print('>> %s threads over...' % amount)
      counter += amount
      if length - counter < amount:
        print('>> start iter one by one...')
        break
    except:
      break
  while True:
    try:
      thread = ThreadS('one', func, next(iterater))
      thread.start()
      thread.join()
      print('>> one over...')
    except:
      print('>> one by one over...')
      break
  print('>> all threads over...')
