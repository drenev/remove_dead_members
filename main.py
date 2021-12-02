import vk_api
access_token = 'тут должен быть OAuth токен'
group_id= тут должен быть ID группы (целое число)
group_id = 'тут должен быть ID группы (целое число)'
session = vk_api.VkApi(token=access_token)
vk = session.get_api()


def get_members(groupid):
    current_group = vk.groups.getMembers(group_id=groupid)
    members_list = current_group["items"]
@@ -12,9 +13,11 @@ def get_members(groupid):
        members_list = members_list + vk.groups.getMembers(group_id=groupid, v=5.92, offset=i*1000)["items"]
    return members_list


def create_members_list(group_id):
    save_list(get_members(group_id), "members_list.txt")


def save_list(list, filename):
    with open(filename, "w") as file:
        for item in list:
@@ -23,33 +26,39 @@ def save_list(list, filename):
            else:
                file.write(str(item) + ",")


def generate_list(filename):
    file = open(filename, 'r')
    current_list = file.readline().split(',')
    return current_list


def create_dead_pages_list(user_ids):
    dead_pages_list = []
    for i in range (0, len(user_ids), 1000):
    for i in range(0, len(user_ids), 1000):
        part_of_the_list = (user_ids[i:i+1000])
        user_info = vk.users.get(user_ids=part_of_the_list)
        for x in range (0, len(part_of_the_list)):
        for x in range(0, len(part_of_the_list)):
            user_status = user_info[x].get('deactivated', 'exists')
            if user_status != "exists":
                dead_pages_list.append(user_info[x].get('id'))
    # save_list(dead_pages_list, 'dead_pages_list.txt') #эта строка сохраняет список id мёртвых подписчиков в txt файл(не обязательна)
    return dead_pages_list


def remove_user(user_id, group_id):
    vk.groups.removeUser(group_id=group_id, user_id=user_id)


def remove_user_from_list(list):
    for i in range (0, len(list)):
    for i in range(0, len(list)):
        remove_user(list[i])


def main():
    dead_pages_list = create_dead_pages_list(get_members(group_id))
    remove_user_from_list(dead_pages_list)
    print('Удалено '+ str(len(dead_pages_list)) + ' мёртвых подписчиков')
    print('Удалено ' + str(len(dead_pages_list)) + ' мёртвых подписчиков')


main()