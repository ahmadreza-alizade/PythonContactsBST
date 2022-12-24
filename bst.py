#creator : ahmadreza alizade fard
#stu_num : 9711150208
#name : notebookcontacts
#version : 1.0
#data structure : BST  binary-search-tree

def sorting_inorder_num(Root):
    name_list = []
    if Root is not None: 
        sorting_inorder_num(Root.leftChild) 
        name_list.append((Root.name, Root.num))
        print("{}:{}".format(Root.num, Root.name))
        sorting_inorder_num(Root.rightChild) 


def sorting_inorder_name(Root):
    global name_list
    if Root is not None: 
        sorting_inorder_name(Root.leftChild) 
        sorting_inorder_name(Root.rightChild) 
        name_list.append((Root.name, Root.num))
    return sorted(name_list)
name_list = []

def printPostorder(Root):   
    if Root: 
        printPostorder(Root.leftChild) 
        printPostorder(Root.rightChild) 
        print(Root.name, Root.num) 
  
def printPreorder(Root):   
    if Root: 
        print(Root.name, Root.num) 
        printPreorder(Root.leftChild) 
        printPreorder(Root.rightChild) 

class Contact:
    def __init__(self, num, name):
        self.num = num
        self.name = name
        self.leftChild = None
        self.rightChild = None
    
    def get(self):
        return self.num
    
    def set(self, num):
        self.num = num
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.num = name


    def getChildren(self):
        children = []
        if(self.leftChild != None):
            children.append(self.leftChild)
        if(self.rightChild != None):
            children.append(self.rightChild)
        return children
        
class Contacts:
    def __init__(self):
        self.root = None

    def setRoot(self, num, name):
        self.root = Contact(num, name)

    def insert(self, num, name):
        if(self.root is None):
            self.setRoot(num, name)
        else:
            self.insertContact(self.root, num, name)

    def insertContact(self, currentContact, num, name):
        if(num <= currentContact.num):
            if(currentContact.leftChild):
                self.insertContact(currentContact.leftChild, num, name)
            else:
                currentContact.leftChild = Contact(num, name)
        elif(num > currentContact.num):
            if(currentContact.rightChild):
                self.insertContact(currentContact.rightChild, num, name)
            else:
                currentContact.rightChild = Contact(num, name)

    def remove(self, num):
    # Case 1: Empty Tree
        if self.root == None:
            return False
        # Case 2: Deleting root node
        if self.root.num == num:
        # Case 2.1: Root node has no children
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
                return True
            # Case 2.2: Root node has left child
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
                return True
            # Case 2.3: Root node has right child
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.rightChild
                return True
            # Case 2.4: Root node has two children
            else:
                moveNode = self.root.rightChild
                moveNodeParent = None
                while moveNode.leftChild:
                    moveNodeParent = moveNode
                    moveNode = moveNode.leftChild
                self.root.num = moveNode.num
                if moveNode.num < moveNodeParent.num:
                    moveNodeParent.leftChild = None
                else:
                    moveNodeParent.rightChild = None
                return True		
        # Find node to remove
        parent = None
        node = self.root
        while node and node.num != num:
            parent = node
            if num < node.num:
                node = node.leftChild
            elif num > node.num:
                node = node.rightChild
        # Case 3: Node not found
        if node == None or node.num != num:
            return False
        # Case 4: Node has no children
        elif node.leftChild is None and node.rightChild is None:
            if num < parent.num:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True
        # Case 5: Node has left child only
        elif node.leftChild and node.rightChild is None:
            if num < parent.num:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return True
        # Case 6: Node has right child only
        elif node.leftChild is None and node.rightChild:
            if num < parent.num:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True
        # Case 7: Node has left and right child
        else:
            moveNodeParent = node
            moveNode = node.rightChild
            while moveNode.leftChild:
                moveNodeParent = moveNode
                moveNode = moveNode.leftChild
            node.num = moveNode.num
            if moveNode.rightnum:
                if moveNode.num < moveNodeParent.num:
                    moveNodeParent.leftChild = moveNode.rightChild
                else:
                    moveNodeParent.rightChild = moveNode.rightChild
            else:
                if moveNode.num < moveNodeParent.num:
                    moveNodeParent.leftChild = None
                else:
                    moveNodeParent.rightChild = None
            return True

    def search(self, num):
        return self.searchContact(self.root, num)#.name, self.searchContact(self.root, num).num 

    def searchContact(self, currentContact, num):
        if currentContact is None:
            return False
        elif num == currentContact.num:
            return currentContact
        elif num <= currentContact.num:
            return self.searchContact(currentContact.leftChild, num)
        else:
            return self.searchContact(currentContact.rightChild, num)

    def check_num_OR_name_root(self, num_ch, name_ch):
        return self.check_num_OR_name(self.root, num_ch, name_ch)

    def check_num_OR_name(self,current_node, num_ch, name_ch):
        if current_node is None:
            return False
        elif num_ch == current_node.num or name_ch == current_node.name:
            print("{}:{}".format(current_node.name, current_node.num))
        self.check_num_OR_name(current_node.leftChild, num_ch, name_ch)
        self.check_num_OR_name(current_node.rightChild, num_ch, name_ch)

    def check_num_AND_root(self, num_ch):
        return self.check_num_AND(self.root, num_ch)

    def check_num_AND(self,current_node, num_ch):
        if current_node is None:
            return False
        elif num_ch == current_node.num:
            print("{}:{}".format(current_node.name, current_node.num))
        self.check_num_AND(current_node.leftChild, num_ch)
        self.check_num_AND(current_node.rightChild, num_ch)

    def check_name_AND_root(self, name_ch):
        return self.check_name_AND(self.root, name_ch)

    def check_name_AND(self,current_node, name_ch):
        if current_node is None:
            return False
        elif name_ch == current_node.name:
            print("{}:{}".format(current_node.name, current_node.num))
        self.check_name_AND(current_node.leftChild, name_ch)
        self.check_name_AND(current_node.rightChild, name_ch)

    def search_name(self, name):
        return self.searchContact_name(self.root, name)#.name, self.searchContact_name(self.root, name).num 

    def searchContact_name(self, currentContact, name):
        if currentContact is None:
            return False
        elif name == currentContact.name:
            return currentContact
        else:
            self.searchContact_name(currentContact.leftChild, name)
            self.searchContact_name(currentContact.rightChild, name)

    def edit_num(self, number, new_num):
        self.search(number).num = new_num

    def edit_name(self, old_name, new_name):
        self.search_name(old_name).name = new_name

    def similarity_search_name(self, word):
        for el in list(set(sorting_inorder_name(self.root))):
            if el[0].startswith(word):
                print("{}:{}".format(el[0], el[1]))

    def conectivity_name(self, fst_name, scnd_name):
        fst_name = self.search_name(fst_name)
        scnd_name = self.search_name(scnd_name)
        if (scnd_name in fst_name.getChildren()) or (fst_name in scnd_name.getChildren()):
            return " Yes they have conectivity "
        else:
            return " No they havent any conectivity"

# this is out of class
my_contacts = Contacts()
#print(my_contacts.root)
#my_contacts.insert(1, "ahmad")
#print(my_contacts.root.num)
#print(my_contacts.root.name)
my_contacts.insert(2, "ahmadreza")
my_contacts.insert(2, "alireza")
my_contacts.insert(2, "ali")
my_contacts.insert(33, "mmd")
my_contacts.insert(444, "ali")
my_contacts.insert(5555, "fateme")
my_contacts.insert(66666, "ali")
my_contacts.insert(7777777, "korosh")
my_contacts.insert(888888888, "mohadese")
my_contacts.insert(99999999999, "leila")

sorting_inorder_num(my_contacts.root)
print("-------------------------------")
for el in sorting_inorder_name(my_contacts.root):
    print("{}:{}".format(el[0], el[1]))


#print(my_contacts.remove(2))
print("----------------------------------------------")
#my_contacts.similarity_search_name("k")
#my_contacts.conectivity_name("sara", "zahra")
#print(my_contacts.check_num_AND_root(2))
#print(my_contacts.check_name_AND_root("ali"))
my_contacts.check_num_OR_name_root(2, "ali")

#print(my_contacts.search(1).name)
#print(my_contacts.search_name("ahmad").num)

#my_contacts.edit_name("ahmad", "hyden")
#my_contacts.edit_num(1, 9370550660)

#print(my_contacts.search(937))
#print(my_contacts.search_name("ahmad"))

