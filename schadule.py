import logging


logger=logging.getLogger('schedule')
from functools import partial,update_wrapper

class scheduleERROOR(Exception):
    """ Base schedule exception"""


class achedulevalueERROR(scheduleERROOR):
   """" Base schedule value ERROR"""


class intervalERROR(scheduleERROOR):
    """An improper interval was used"""


class shceduler:
    def __init__(self):
        self.job=[]

    def every(self,interval):
        job=job(interval,self)
        return job


class job:
    def __init__(self,interval,scheduler):
        self.interval = interval
        self.job_func = None
        self.unit = None
        self.scheduler = scheduler
   
    @property
    def second(self):
        if self.interval != 1:
            raise intervalERROR('use seconds instead second')
        return self.seconds

    @property
    def seconds (self):
        self.unit = 'seconds'
        return self

    @property
    def minute(self):
        if self.interval != 1:
            raise intervalERROR('use minutes instead minute')
        return self.minutes

    @property
    def minutes (self):
        self.unit = 'minutes'
        return self

    @property
    def hour(self):
        if self.interval != 1:
            raise intervalERROR('use hours instead hour')
        return hour

    @property
    def hours (self):
        self.unit = 'hours'
        return self
    
    @property
    def day(self):
        if self.interval != 1:
            raise intervalERROR('use days instead day')
        return days

    @property
    def days (self):
        self.unit = 'days'
        return self

    @property
    def week(self):
        if self.interval != 1:
            raise intervalERROR('use weeks instead week')
        return weeks

    @property
    def weeks (self):
        self.unit = 'weeks'
        return self

    def do(self,job_func,*args,**kwargs):
        self.job_func = functools.partial(job_func,*args,**kwargs)
        functools.update_wrapper(self.job_func,job_func)
        if self.scheduler is none :
            raise scheduleERROOR(
                'unable to add job to schedule.'
             'job is not associated with an scheduler')
        self.scheduler.jobs.append(self)
        return self    
    
    def _scheduler_next_run(self):
        pass


difult_scheduler = scheduler()

def every(interval=1):
    difult_scheduler.every(interval)