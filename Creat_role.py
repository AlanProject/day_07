#-*- coding:utf-8 -*-
#/usr/bin/env python
class create_role(object):
    def __init__(self,name,LV,HP,ATK,DEF,PS,EXP):
        self.name = name
        self.LV = LV
        self.HP = HP
        self.EXP = EXP
        self.ATK = ATK
        self.DEF = DEF
        self.PS = PS
    def role(self):
        print ''.ljust(20,'-')
        print '''
        职业：%s
        等级：%d
        血量：%d
        攻击：%d
        防御：%d
        体力：%d
        经验：%d
        '''%(self.name,self.LV,self.HP,self.ATK,self.DEF,self.PS,self.EXP)
        print ''.ljust(20,'-')
if __name__ == '__main__':

    print ''.ljust(20,'=')
    print '''
    1.战士
    2.魔法师
        '''
    print ''.ljust(20,'=')
    number =  int(raw_input('请输入要创建的角色：'))
    if number == 1:
        role = create_role('战士',1,100,500,100,120,100)
        role.role()
    elif number == 2:
        role = create_role('魔法师',1,150,120,300,200,120)
        role.role()
    else:
        pass
