import random
import string
outfile=open('/home/tk/coding2/db/random/department.txt','w')
dpt_name=random.sample(range(1,5),4)
dpt_num=random.sample(range(3,8),4)
for i in range(4):
    outfile.write(str(dpt_name[i])+'\t')
    outfile.write(str(dpt_num[i])+'\n')
outfile.close()

outfile=open('/home/tk/coding2/db/random/employee.txt','w')
id=random.sample(range(1,25),24)
phone=random.sample(range(111111,222222),24)
for i in range(dpt_num[0]):
    name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))
    age=random.randint(20,30)
    salary=random.randrange(3000,6000,500)
    in_dpt=dpt_name[0]
    outfile.write(str(id[i])+'\t')
    outfile.write(str(name)+'\t')
    outfile.write(str(age)+'\t')
    outfile.write(str(salary)+'\t')
    outfile.write(str(phone[i])+'\t')
    outfile.write(str(in_dpt)+'\n')
for i in range(dpt_num[0],dpt_num[0]+dpt_num[1]):
    name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))
    age=random.randint(20,30)
    salary=random.randrange(3000,6000,500)
    in_dpt=dpt_name[1]
    outfile.write(str(id[i])+'\t')
    outfile.write(str(name)+'\t')
    outfile.write(str(age)+'\t')
    outfile.write(str(salary)+'\t')
    outfile.write(str(phone[i])+'\t')
    outfile.write(str(in_dpt)+'\n')
for i in range(dpt_num[1]+dpt_num[0],dpt_num[0]+dpt_num[2]+dpt_num[1]):
    name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))
    age=random.randint(20,30)
    salary=random.randrange(3000,6000,500)
    in_dpt=dpt_name[2]
    outfile.write(str(id[i])+'\t')
    outfile.write(str(name)+'\t')
    outfile.write(str(age)+'\t')
    outfile.write(str(salary)+'\t')
    outfile.write(str(phone[i])+'\t')
    outfile.write(str(in_dpt)+'\n')
for i in range(
 dpt_num[0]+dpt_num[1]+dpt_num[2],dpt_num[0]+dpt_num[1]+dpt_num[2]+dpt_num[3]):
    name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))
    age=random.randint(20,30)
    salary=random.randrange(3000,6000,500)
    in_dpt=dpt_name[3]
    outfile.write(str(id[i])+'\t')
    outfile.write(str(name)+'\t')
    outfile.write(str(age)+'\t')
    outfile.write(str(salary)+'\t')
    outfile.write(str(phone[i])+'\t')
    outfile.write(str(in_dpt)+'\n')
outfile.close()
