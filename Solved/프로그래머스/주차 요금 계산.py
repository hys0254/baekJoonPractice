import math
def solution(fees, records):
    answer = []
    default_time, default_fee, unit_time, unit_fee= map(int,fees)
    car_records={}
    for car_io in records:
        time, car_num, io = car_io.split()
        hour,minute= map(int,time.split(":"))
        if io =="IN":
            time=-(hour*60+minute)
            car_record=car_records.get(car_num,0)
            car_record+=time
            car_records[car_num]=car_record
        elif io =="OUT":
            time=hour*60+minute
            car_record=car_records.get(car_num,0)
            car_record+=time
            car_records[car_num]=car_record
    cars=list(car_records.keys())
    cars.sort()
    for car in cars:
        total_time= car_records[car]
        if total_time<0:
            total_time+=23*60+59
        if total_time<=default_time:
            answer.append(default_fee)
            
        else:
            total_time-=default_time
            total_fee=default_fee+math.ceil(total_time/unit_time)*unit_fee
            answer.append(total_fee)
            
   
            
    return answer