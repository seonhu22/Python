import time
import FactorySimulatorInterface
import DatabaseInterface

# global variables
server_ip_address = '127.0.0.1'
server_port_number = 6340
number_of_AGV = 7
current_job = 0
loop_time_seconds = 1


# function name : get_target_position
# parameters : AGV_number : 움직일 AGV 번호, job_id : 현재 이동 예정인 제품의 S/N
# return : target_position
# comments :
def get_target_position(AGV_number, job_id):
    target_position = str()
    current_product_type = str()
    target_position_list = ['HOME,O', 'F-A0,I', 'F-B0,I', 'F-C1,I', 'F-C2,I','F-D0,I', 'F-E0,I', 'STRG,I']

    for job_list in DatabaseInterface.g_job_list:
        try:
            job_list.index(job_id)
            current_product_type = job_list[1]
            break

        except ValueError:
            continue

    for product_type in DatabaseInterface.g_product_type:
        try:
            product_type.index(current_product_type)
            if AGV_number == 0:
                target_position = target_position_list[product_type[1]]
                print(target_position)

            for jj in range(11):
                if jj % 2 != 0:
                    if AGV_number == product_type[jj]:
                        if jj + 2 > 10 or product_type[jj + 2] is None:
                            target_position = target_position_list[7]

                        else:
                            target_position = target_position_list[product_type[jj + 2]]

        except ValueError:
            continue

    return target_position


# function name : init_variables
# parameters : none
# return : none
# comments :
def init_variables():
    DatabaseInterface.init_db("SmartFactory.db")
    DatabaseInterface.get_db_data()

    FactorySimulatorInterface.init_socket(server_ip_address, server_port_number)
    FactorySimulatorInterface.set_number_of_AGV(number_of_AGV)


# function name : exit_program
# parameters : none
# return : none
# comments :
def exit_program():
    DatabaseInterface.close_db()
    FactorySimulatorInterface.close_socket()


# main function
init_variables()
reference_position = ['HOME,O', 'F-A0,O', 'F-B0,O', 'F-C1,O', 'F-C2,O','F-D0,O', 'F-E0,O']

while True:
    current_time = time.time()


    # AGV 상태 출력
    agv_stat = FactorySimulatorInterface.get_current_states("AGV_STAT").split(',')

    print("AGV\tStatus\tPos1\tPos2\tSOC\tsn")
    for i in range(number_of_AGV):
        for mystr in agv_stat[i * 6 + 1:i * 6 + 7]:
            print(mystr, '\t', end="")
        print()
    print()

    # Facility 상태 출력
    facility_stat = FactorySimulatorInterface.get_current_states("FCT_STAT").split(',')

    print("설비\t상태\t입상태\t입AGV\t입예약\t출상태\t출AGV\t출예약\t입버퍼\t제품수\tjobid\t출버퍼\t제품수\tjobid")

    for i in range(9):
        for mystr in facility_stat[i * 14 + 1:i * 14 + 15]:
            print(mystr, '\t', end="")
        print()
    print()

    # 6개의 AGV를 구동하는 알고리즘
    # print("상태\tAGV\tPOS")
    for i in range(number_of_AGV):
        none_job_id = '000000'
        # current_job_id 계산 시 F-C2, F-C3 검색 제외
        current_job_id = str(facility_stat[(i + 2 if i > 3 else i) * 15 + 14].split(':')[0])  # F-C2, F-C3 검색 제외
        total_job_size = len(DatabaseInterface.g_job_list)

        agv_name = 'AGV' + str(i + 1).zfill(2)
        agv_status = str(agv_stat[i * 6 + 2])

        # agv_current_pos : 'HOME,o','F-B0,I" 처럼 표현함 // 현재위치
        agv_current_pos = str(agv_stat[i * 6 + 3] + ',' + agv_stat[i * 6 + 4])

        # agv_reference_pos : 위에서 정의되어 있음 (하나하나씩) 이에 따라 AGV 레퍼런스 정해짐 // 가야할 위치
        agv_reference_pos = str(reference_position[i])

        agv_target_pos = get_target_position(i, current_job_id)


        # facility_current_output_buffer 계산 시 F-C2, F-C3 검색 제외
        facility_current_output_buffer = str(facility_stat[(i + 2 if i > 3 else i) * 15 + 14])
        print("--------------" + facility_current_output_buffer + "--------------")

        # AGV 이동 명령을 저장하기 위한 변수
        command = ''

        if agv_status == 'I':
            if agv_current_pos != agv_reference_pos:
                command = agv_name + ',' + none_job_id + ',' + agv_reference_pos
                FactorySimulatorInterface.set_AGV_position(command)
                print('Reset' + '\t' + agv_name + '\t' + agv_reference_pos)

            else:
                if agv_name == 'AGV01' and current_job < total_job_size:
                    current_job_id = str(DatabaseInterface.g_job_list[current_job][0])
                    agv_target_pos = get_target_position(i, current_job_id)

                    # command 예: 'AGV01,A00001,F-A0,I'
                    command = agv_name + ',' + current_job_id + ',' + agv_target_pos
                    error = FactorySimulatorInterface.set_AGV_position(command)

                    print('Move' + '\t' + agv_name + '\t' + agv_reference_pos)
                    # 9000; error 없음
                    # 9203; 이동시키려는 제품이 현재 위치에 없음

                    if (error == "'AGV_CTRL,9000'") | (error == "'AGV_CTRL,9203'"):
                        current_job += 1

                else:
                    if facility_current_output_buffer != '00':
                        command = agv_name + ',' + current_job_id + ',' + agv_target_pos
                        FactorySimulatorInterface.set_AGV_position(command)


    # adjust loop time to the loop_time_seconds
    while time.time() - current_time < loop_time_seconds:
        time.sleep(0.05)
