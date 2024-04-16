import os 
import random

def estimate_pi(num_points):
    """
    使用蒙特卡洛方法估计π的值。
    参数 num_points 是随机生成的点的数量。
    返回一个浮点数，表示π的估计值。
    """
    inside_circle = 0
    for _ in range(num_points):
        x, y = random.random(), random.random()
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1
    # 估计π的值，单位正方形的面积是1，单位圆的面积是π/4
    rst = (inside_circle / num_points) * 4
    print(f"Estimated value of Pi: {rst}")
    return rst 



print("start mtpi")


if __name__ == "__main__":
    from threading import Thread
    pid = os.getpid()
    print(f"The process ID is: {pid}") 
    threads = [ Thread(target = estimate_pi, args = (10000000, )) for _ in range(6)] 

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

else : 
    num_points = 1000000  # 增加点的数量可以提高估计的准确性
    print("try to estimate pi", num_points)
    #pi_estimate = estimate_pi(num_points)
