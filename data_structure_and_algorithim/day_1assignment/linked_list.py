'''
Created on Apr 20, 2020

@author: amrit
'''
class Node:
    def __init__(self):
        self.__data=None
        self.__next=None
    def set_data(self,data):
        self.__data=data
    def get_data(self):
        return self.__data
    def set_next(self,next_node):
        self.__next=next_node
    def get_next(self):
        return self.__next
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    def set_head(self,head):
        self.__head=head
    def get_head(self):
        return self.__head
    def set_tail(self,tail):
        self.__tail=tail
    def get_tail(self):
        return self.__tail
    def add(self,data):
        new_node=Node()
        new_node.set_data(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()
    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None
    def insert(self,data,data_before):
        new_node=Node()
        new_node.set_data(data)
        if(data_before is None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if (new_node.get_next() is None):
                self.__tail=new_node
        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not found in the linked list")
    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if (node is self.__head):
                if(self.__head is self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
                node.set_next(None)
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
l1=LinkedList()
l1.insert("Apple",None)
l1.add("Hello")
l1.add("Amrit")
l1.insert("Lucky","Hello")
l1.delete("Apple")
l1.display()