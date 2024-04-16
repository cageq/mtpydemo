
from threading import Thread

def main():
    stat = {"piece_count": 0, "reward_count": 0}
    t1 = Thread(target=process_piece, args=(stat,))
    t2 = Thread(target=process_piece, args=(stat,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(stat)

def process_piece(stat):
    for i in range(10000000):
        if stat["piece_count"] % 10 == 0:
            reward = True
        else:
            reward = False
        if reward:
            stat["reward_count"] += 1
        stat["piece_count"] += 1

if __name__ == "__main__":
    main()
