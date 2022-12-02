import sys
import socket
import time

TIMEOUT = 5
PORT = 33434


def get_dest_host_from_argv():
    if len(sys.argv) != 2:
        raise Exception("Needed destination address")

    return sys.argv[1]


def create_sender(ttl: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

    return s


def create_receiver():
    r = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    r.settimeout(TIMEOUT)

    return r


def print_host(i: int, addr, t):
    if i < 10:
        str_i = f" {i}"
    else:
        str_i = f"{i}"

    if addr:
        try:
            host = socket.gethostbyaddr(addr[0])
            print(f"{str_i}\t{host[0]} ({host[2][0]}) {t:.{3}f} ms")
        except socket.herror:
            print(f"{str_i}\t{addr[0]} ({addr[0]}) {t:.{3}f} ms")

    else:
        print(f"{i}\t*")


def traceroute(dst: str, max_hops=30):
    dst_ip = socket.gethostbyname(dst)

    for ttl in range(1, max_hops + 1):
        sender = create_sender(ttl)
        receiver = create_receiver()

        try:
            receiver.bind(('', PORT))
        except socket.error:
            raise Exception("Cannot bind socket")

        start = time.time()
        sender.sendto(b'Hi, honey', (dst_ip, PORT))

        try:
            _, addr = receiver.recvfrom(1024)
            end = time.time()
        except socket.error:
            addr = None
            end = time.time()

        t = (end - start) * 1000

        print_host(ttl, addr, t)
        if addr:
            if addr[0] == dst_ip:
                break

        sender.close()
        receiver.close()


if __name__ == "__main__":
    dest_name = get_dest_host_from_argv()

    traceroute(dest_name)
