def find_parent(x):     # x�� ���� root node ã�� �Լ�
    if x==friends[x]:
        return x
    else:               # �� ���� ����� value�� ��� root node�� �ٲ���. ���� Ŀ���� ��ȸ�ϴ� �ð��� �پ��.
        root_x=find_parent(friends[x])   
        friends[x]=root_x
        return friends[x]


def union(x,y):
    root_x=find_parent(x)  # x, y�� root node�� ã��
    root_y=find_parent(y)

    # x, y�� root node�� ���� ������
    # y�� root node�� x�� root node�� �ڽ��� �ǵ��� ��
    # �׸��� root_x�� ģ�� ���� root_y�� ģ�� ���� ����
    
    if root_x!=root_y:
        friends[root_y]=root_x
        number[root_x]+=number[root_y]

for i in range(int(input())):
    friends = {}
    number = {}
    for j in range(int(input())):
        x,y=input().split()
        if x not in friends:
            friends[x]=x
            number[x]=1
        if y not in friends:
            friends[y]=y
            number[y]=1
        union(x,y)
        # ���� �Լ����� x, y�� root node�� ���� ������
        # x�� root node�� y�� root node�� �ǵ��� �߱� ������
        # x�� root node�� ���� ã�Ƽ� ������ �����
        print(number[find_parent(x)])
